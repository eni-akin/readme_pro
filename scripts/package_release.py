#!/usr/bin/env python3
"""Validate and package the skills-only release. Requires requirements-dev.txt."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import tempfile
from urllib.parse import urlsplit
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

import yaml

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(root):
    manifest = json.loads((root / 'plugin.json').read_text())
    require(manifest.get('$schema') == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'Wrong plugin schema')
    require(manifest.get('name') == 'readme-pro', 'Unexpected plugin identity')
    require(re.fullmatch(r'\d+\.\d+\.\d+', manifest.get('version', '')), 'Expected a stable semantic version')
    require(manifest.get('license') == 'MIT', 'Expected MIT license')
    require(not any(manifest.get(key) is not None for key in ('apps', 'mcpServers', 'skills', 'interface')), 'Invalid portable fields')
    extension = manifest['extensions']['com.openai']
    require(extension.get('apps') is None, 'Public upload cannot contain app bindings')
    interface = extension['interface']
    for key, limit in [('displayName',30), ('shortDescription',30), ('longDescription',4000), ('developerName',80)]:
        value = interface.get(key)
        require(isinstance(value,str) and value.strip() and len(value) <= limit, f'Invalid {key}')
        require(not any(ord(c) < 32 and c != '\n' for c in value), f'Control character in {key}')
        require(key == 'longDescription' or '\n' not in value, f'{key} must be one line')
    require(interface['category'] == 'Developer Tools', 'Unexpected category')
    require(interface['developerName'] == manifest['author']['name'], 'Publisher metadata differs')
    prompts = interface['defaultPrompt']
    require(isinstance(prompts,list) and 1 <= len(prompts) <= 3, 'Expected one to three prompts')
    require(all(isinstance(p,str) and p.strip() and len(p)<=128 and '\n' not in p and '@' not in p for p in prompts), 'Invalid starter prompt')
    require(len({' '.join(p.split()).casefold() for p in prompts}) == len(prompts), 'Duplicate prompts')
    for key in ('websiteURL','supportURL','privacyPolicyURL','termsOfServiceURL'):
        value = interface[key]
        parsed = urlsplit(value)
        require(parsed.scheme == 'https' and parsed.hostname and not parsed.username and not parsed.password and len(value)<=1024, f'Invalid {key}')
    require(extension['review'].get('commerce') is False, 'Expected free release')
    require(extension['publication'].get('countries') == [], 'Expected no country restrictions')
    for key in ('logo', 'composerIcon'):
        path = (root / interface[key]).resolve()
        require(path.is_relative_to(root.resolve()) and path.is_file(), f'Missing or escaping {key}')
        data = path.read_bytes()
        require(data[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', data[16:24]) == (1024,1024), 'Icon must be a 1024px square PNG')
        require(len(data) <= 5*1024*1024, 'Icon exceeds 5 MiB')
    skills = sorted((root/'skills').glob('*/SKILL.md'))
    require([p.parent.name for p in skills] == ['readme-pro'], 'Expected exactly one skill')
    skill = skills[0]
    text = skill.read_text()
    match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    require(match is not None, 'Missing skill frontmatter')
    frontmatter = yaml.safe_load(match.group(1))
    require(frontmatter.get('name') == skill.parent.name and isinstance(frontmatter.get('description'),str) and frontmatter['description'].strip(), 'Invalid skill metadata')
    require('[TODO:' not in text, 'Unfinished skill')
    metadata = yaml.safe_load((skill.parent/'agents/openai.yaml').read_text())
    require(metadata['interface']['display_name'] == interface['displayName'], 'Skill display name differs')
    require(metadata.get('policy',{}).get('allow_implicit_invocation', True) is True, 'Implicit invocation changed')
    require(not metadata.get('dependencies'), 'Unexpected skill dependencies')
    require((skill.parent/'LICENSE').read_bytes() == (root/'LICENSE').read_bytes(), 'Portable license differs')
    for target in re.findall(r'\]\((references/[^)#]+)(?:#[^)]*)?\)', text):
        path = (skill.parent/target).resolve()
        require(path.is_relative_to(skill.parent.resolve()) and path.is_file(), f'Missing skill reference: {target}')
    catalog_path = root/'.agents/plugins/marketplace.json'
    if catalog_path.exists():
        catalog = json.loads(catalog_path.read_text())
        require(catalog['name'] == 'eni-akin' and len(catalog['plugins']) == 1, 'Invalid marketplace identity')
        entry = catalog['plugins'][0]
        require(entry['name'] == manifest['name'] and entry['source'] == {'source':'local','path':'./'}, 'Catalog source differs')
        require(entry['policy'] == {'installation':'AVAILABLE','authentication':'ON_INSTALL'} and entry['category'] == interface['category'], 'Catalog policy differs')
    files = [root/'plugin.json', root/'LICENSE', root/'assets/icon.png', *sorted((root/'skills/readme-pro').rglob('*'))]
    for path in files:
        require(not path.is_symlink(), f'Symlink excluded from release: {path}')
    files = [p for p in files if p.is_file()]
    require(all(p.name != '.DS_Store' and '__pycache__' not in p.parts and p.suffix != '.pyc' for p in files), 'Unexpected generated skill file')
    return manifest, files


def build(root, destination):
    manifest, files = validate(root)
    destination.mkdir(parents=True, exist_ok=True)
    name = f"{manifest['name']}-{manifest['version']}"
    archive = destination/f'{name}.zip'
    require(not archive.exists(), f'Refusing to overwrite {archive}; use a fresh output directory')
    with ZipFile(archive,'w',compression=ZIP_DEFLATED) as output:
        for path in sorted(files):
            info = ZipInfo(f"{manifest['name']}/{path.relative_to(root).as_posix()}", date_time=(2026,1,1,0,0,0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            output.writestr(info,path.read_bytes())
    with tempfile.TemporaryDirectory(prefix='readme-pro-archive-') as temporary:
        with ZipFile(archive) as output:
            expected = {f"{manifest['name']}/{p.relative_to(root).as_posix()}" for p in files}
            require(set(output.namelist()) == expected and output.testzip() is None, 'Archive inventory or CRC failed')
            output.extractall(temporary)
        extracted = Path(temporary)/manifest['name']
        _, unpacked = validate(extracted)
        require(all(p.read_bytes() == (root/p.relative_to(extracted)).read_bytes() for p in unpacked), 'Extracted files differ')
    checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
    (destination/f'{name}.sha256').write_text(f'{checksum}  {archive.name}\n')
    return archive, checksum


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT/'dist')
    args = parser.parse_args()
    archive, checksum = build(ROOT,args.output_dir.resolve())
    print(f'{archive}\nSHA-256: {checksum}')
