# Date Adder

A small Python utility that prefixes each file in a specified directory with today's date (YYYY-MM-DD). It includes a dry‑run option to preview changes without actually renaming files.

## Features

- Adds the current date to the beginning of filenames.
- Optional dry‑run mode for previewing changes.
- Handles errors gracefully.

## Usage

```bash
python add_date.py --folder dates
# With dry‑run
python add_date.py --folder dates --dry-run
```

## Requirements

- Python 3.6 or newer.

## License

MIT License