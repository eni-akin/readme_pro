import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package_release', ROOT/'scripts/package_release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def test_archive_inventory_and_reproducibility(self):
        with tempfile.TemporaryDirectory() as temporary:
            first, digest = release.build(ROOT,Path(temporary)/'first')
            second, repeat = release.build(ROOT,Path(temporary)/'second')
            self.assertEqual(digest,repeat)
            self.assertEqual(first.read_bytes(),second.read_bytes())
            with ZipFile(first) as archive:
                self.assertIn('readme-pro/plugin.json',archive.namelist())
                self.assertTrue(all(name.startswith('readme-pro/') for name in archive.namelist()))
                self.assertFalse(any('/.agents/' in name or '/scripts/' in name or '/.git/' in name for name in archive.namelist()))

    def test_invalid_metadata_and_escaping_icon_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)/'source'
            shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('dist','__pycache__','.git'))
            original = json.loads((root/'plugin.json').read_text())
            for key, value in [('shortDescription','x'*31),('logo','../outside.png')]:
                manifest = json.loads(json.dumps(original))
                manifest['extensions']['com.openai']['interface'][key] = value
                (root/'plugin.json').write_text(json.dumps(manifest))
                with self.subTest(key=key), self.assertRaises(ValueError):
                    release.validate(root)


if __name__ == '__main__':
    unittest.main()
