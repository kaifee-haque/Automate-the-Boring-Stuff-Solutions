#! python3
"""
A version of the strip() function that uses regular expressions.
"""


import re
import sys


def restrip(string, mode = "a"):
    """Strips leading and/or trailing whitespace from a given string.

    Args:
        string: The string to be stripped.
        mode: Optional; All, leading, or trailing whitespace will be stripped
        depending on whether mode is equal to a, l, or r.

    Returns:
        A copy of the original string with the specified whitespace stripped.
    """
    
    whitespace_a = re.compile(r"\s*")
    whitespace_l = re.compile(r"^\s*")
    whitespace_r = re.compile(r"\s*$")
    
    if mode == "a":
        return whitespace_a.sub("", string)
    elif mode == "l":
        return whitespace_l.sub("", string)
    elif mode == "r":
        return whitespace_r.sub("", string)


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ["a", "l", "r"]:
        print("Usage: python regex_strip.py <a/l/r> <string>")
        sys.exit()
    else:
        print(restrip(sys.argv[2]))
    
