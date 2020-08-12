#! python3
import re
import sys

whitespace_a = re.compile(r"\s*")
whitespace_l = re.compile(r"^\s*")
whitespace_r = re.compile(r"\s*$")

def restrip(string, mode = "a"):
    if mode == "a":
        return whitespace_a.sub("", string)
    elif mode == "l":
        return whitespace_l.sub("", string)
    elif mode == "r":
        return whitespace_r.sub("", string)

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ["a", "l", "r"]:
        print("Usage: python regex_strip <a/l/r> <string>")
        sys.exit()
    else:
        print(restrip(sys.argv[2]))
    
