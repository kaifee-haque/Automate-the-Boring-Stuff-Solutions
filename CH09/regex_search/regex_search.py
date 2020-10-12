#! python3
"""Searches every text file in a directory for a string that matches a given
regular expression."""


import os, re
from pathlib import Path


files = os.listdir(Path.cwd())

for name in files:
    if name[-4:] != ".txt":
        files.remove(name)

pattern = re.compile(input("Please enter a regular expression: "))

for name in files:
    file = open(name)
    text = file.read()
    file.close()
    matches = pattern.findall(text)
    if matches != None:
        for match in matches:
            print(f"Result from {name}: {match}")
