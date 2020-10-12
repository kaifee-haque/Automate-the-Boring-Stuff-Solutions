#! python3
"""Walks through a folder tree and copies every file with a given extensison
to a new folder."""


import os, sys, shutil
from pathlib import Path


def main(args):
    """Walks through the current working directory and copies files with a given extension."""
    
    for folder, subfolders, files in os.walk(Path.cwd()):
        for file in files:
            if file[(-1) * len(args[2]):] == args[1]:
                if not Path.exists(Path(Path.cwd(), args[2])):
                    os.mkdir(Path(Path.cwd(), args[2]))
                shutil.copy(Path(Path.cwd(), file), Path(Path.cwd(), args[2]))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python selective_copy,py <file extension> <new folder>")
        print("Example python selective_copy,py .txt text_files")
        sys.exit()
    else:
        main(sys.argv)
