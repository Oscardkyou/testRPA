import os
import shutil
import random
import string

from constants import *

_MAX_ = 100

def make_dir() -> None:
    random_sequence = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))

    all_extensions = (
        IMAGES + TEXT + VIDEO + AUDIO + APPLICATIONS + CODE +
        INSTALL + COMPRESSED + DOCUMENTS + OTHER
    )
    random_extension = random.choice(all_extensions)

    file_name = random_sequence + random_extension

    with open(file_name, "w") as f:
        pass

    shutil.move(file_name, os.path.join(TARGET_DIR, file_name))

def establish() -> None:
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

def delete_dir() -> None:
    shutil.rmtree(TARGET_DIR)

def run_test() -> None:
    establish()
    for _ in range(_MAX_):
        make_dir()

