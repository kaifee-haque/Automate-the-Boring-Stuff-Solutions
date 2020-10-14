#! python3
"""Walks through a folder tree and prints every file greater than or equal to
a specified size in megabytes."""


import os, sys
from pathlib import Path


def main(args):
    """Walks through the current working directory and prints the absolute path of every
    file greater than or equal to args[1]."""
    
    for folder, subfolders, files in os.walk(Path.cwd()):
        for file in files:
            if os.path.getsize(Path(Path.cwd(), file)) >= int(args[1]) * 1000000:
                print(Path(Path.cwd(), file))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_big_files.py <size>")
        print("Example python find_big_files.py 100")
        sys.exit()
    else:
        main(sys.argv)
