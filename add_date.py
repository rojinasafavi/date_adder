import argparse
import os
import sys
from datetime import date

def add_date_to_filenames(folder: str, dry_run: bool = False):
    """Rename files in *folder* by prefixing today's date (YYYY-MM-DD).

    Args:
        folder: Path to the target directory.
        dry_run: If True, only print the intended renames without performing them.
    """
    # Resolve absolute path
    folder_path = os.path.abspath(folder)
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        sys.exit(1)

    today_str = date.today().isoformat()  # YYYY-MM-DD

    for entry in os.listdir(folder_path):
        entry_path = os.path.join(folder_path, entry)
        # Skip subdirectories
        if os.path.isdir(entry_path):
            continue
        # Skip if already prefixed with a date pattern (basic check)
        if entry.startswith(today_str + "_"):
            continue
        new_name = f"{today_str}_{entry}"
        new_path = os.path.join(folder_path, new_name)
        if dry_run:
            print(f"Would rename: {entry} -> {new_name}")
        else:
            try:
                os.rename(entry_path, new_path)
                print(f"Renamed: {entry} -> {new_name}")
            except Exception as e:
                print(f"Failed to rename '{entry}': {e}")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Add today's date (YYYY-MM-DD) to the beginning of every filename in a folder."
    )
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default=".",
        help="Target directory (default: current working directory).",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="Show what would be renamed without making changes.",
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    add_date_to_filenames(args.directory, args.dry_run)
