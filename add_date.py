import os
import argparse
from datetime import datetime

def add_date_to_filenames(folder_path: str, dry_run: bool = False) -> None:
    """Prefix each file in *folder_path* with today's date (YYYY-MM-DD).

    Args:
        folder_path: Path to the directory containing files to rename.
        dry_run: If True, only prints the intended rename operations without
            performing them.
    """
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Directory not found: {folder_path}")

    today_str = datetime.now().strftime("%Y-%m-%d")
    for entry in os.listdir(folder_path):
        old_path = os.path.join(folder_path, entry)
        # Skip subdirectories
        if not os.path.isfile(old_path):
            continue
        # Skip files that already start with the date
        if entry.startswith(f"{today_str}_"):
            continue
        new_name = f"{today_str}_{entry}"
        new_path = os.path.join(folder_path, new_name)
        if dry_run:
            print(f"[DRY RUN] Would rename: {old_path} -> {new_path}")
        else:
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")


def parse_args():
    parser = argparse.ArgumentParser(description="Add today's date to filenames in a folder.")
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default=os.path.join(os.getcwd(), "dates"),
        help="Target directory (default: ./dates relative to current working directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be renamed without making changes",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    add_date_to_filenames(args.directory, args.dry_run)
