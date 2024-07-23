import os
import shutil
import sys
from typing import List
from tqdm import tqdm

from constants import *

def get_extension(file_name: str) -> str:
    return "." + file_name.split(".")[-1].lower()

def move_file(subcategory_dir: str, file: str) -> None:
    if not os.path.exists(os.path.join(TARGET_DIR, subcategory_dir)):
        os.makedirs(os.path.join(TARGET_DIR, subcategory_dir))

    source_path = os.path.join(TARGET_DIR, file)
    destination_path = os.path.join(TARGET_DIR, subcategory_dir, os.path.basename(file))
    shutil.move(source_path, destination_path)

def organize_files(files: List[str]) -> None:
    for file in tqdm(files, desc="\n[organizing files]", unit="file"):
        if file.lower() != MAKEFILE:
            extension = get_extension(file)
        else:
            extension = "Makefile"

        for extensions, category in file_extensions.items():
            if extension in extensions:
                subdir_name = category
                move_file(subdir_name, file)
                break
        else:
            move_file(OTHER_STR, file)

def establish_current_dir() -> List[str]:
    try:
        with os.scandir(TARGET_DIR) as entries:
            return [entry.name for entry in entries if entry.is_file()]
    except FileNotFoundError:
        print(ERROR_MSG)
        sys.exit(1)

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python main.py /path/to/your/folder")
        sys.exit(1)

    global TARGET_DIR
    TARGET_DIR = sys.argv[1]

    files = establish_current_dir()
    organize_files(files)
    print("File organization complete.")

if __name__ == "__main__":
    main()

