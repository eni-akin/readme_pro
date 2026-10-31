# Editorial examples

These fictional examples illustrate editing choices. They are not generated claims about a real project or templates the agent must reproduce. A real run must derive names, commands, and behavior from that repository.

## CLI: show a useful result

Before:

````markdown
# LineCount
A powerful next-generation Python tool.

## Tech stack
Python

## Getting started
Run the script.
````

After, given a fictional repository whose `linecount.py` counts newline-terminated lines and has no third-party dependencies:

````markdown
# LineCount

Count lines in a text file from the terminal using Python's standard library.

## Quick start

From the repository root, with Python 3 installed:

```sh
printf 'alpha\nbeta\n' > sample.txt
python3 linecount.py sample.txt
```

Expected output:

```text
2
```

## Limitations

Counts newline characters; a final line without a trailing newline is not counted.
````

The revision replaces generic praise with behavior, gives a reproducible first task, and makes a consequential edge case visible. The file creation is explicit and uses a disposable example filename.

## Application: make evidence and prerequisites visible

Before:

````markdown
# TaskBoard
React! SQLite! Docker! The ultimate productivity app.

## Roadmap
- Collaboration
- Authentication
- Notifications
````

After, given a fictional repository with an existing screenshot and setup guide that establish local-only storage:

````markdown
# TaskBoard

A local task board for organizing personal work into columns.

![Tasks grouped into planned, active, and completed columns](docs/assets/board.png)

## What you can do

- Create and move tasks between columns.
- Keep tasks in a local SQLite database.

## Run locally

Follow the [setup guide](docs/setup.md) for prerequisites, database initialization,
and startup commands. The guide includes a sample board to confirm setup worked.

## Limitations

Designed for one local user. Authentication and shared boards are not implemented.
````

The revision puts the visible workflow first, links established setup details, and distinguishes current behavior from possible future work. If the image or guide did not exist, the agent would need to create justified supporting material or report the gap rather than emitting these links.
