#! python3
import sys, pyperclip, shelve, pprint
from pathlib import Path

shelf_file = shelve.open("clip")
if len(shelf_file) == 0:
    entries = {"reaches": """--it reaches out it reaches out it reaches out it reaches out--
One hundred and thirteen times a second, nothing answers and it reaches out.
It is not conscious, though parts of it are.
There are structures within it that were once separate organisms; aboriginal, evolved, and complex.
It is designed to improvise, to use what is there and then move on.
Good enough is good enough, and so the artifacts are ignored or adapted.
The conscious parts try to make sense of the reaching out. Try to interpret it.""",
           "book": """It was a real book— onionskin pages bound in what might have been
actual leather. Miller had seen pictures of them before; the idea of that
much weight for a single megabyte of data struck him as decadent."""}
    shelf_file["entries"] = entries
    shelf_file.close()
else:
    entries = shelf_file["entries"]

if __name__ != "__main__":
    print("Program must be executed from the command line.")
    sys.exit()

if (len(sys.argv) < 3 and sys.argv[1] != "list") or len(sys.argv) > 4:
    print("""Usage:
To copy an entry: python multiclip.py copy <keyphrase>
To add an entry: python multiclip.py add <keyphrase> <text>
To remove an entry: python multiclip.py delete <keyphrase>
To clear the clipboard: python multiclip.py delete <keyphrase>
To list all entries: python multiclip.py list""")
    sys.exit()

command = sys.argv[1]
if len(sys.argv) > 2:
    keyphrase = sys.argv[2]
if len(sys.argv) == 4:
    text = sys.argv[3]

if command == "copy":
    if keyphrase in entries:
        pyperclip.copy(entries[keyphrase])
    else:
        print(f"No entry named {keyphrase} exists.")

elif command == "add" and len(sys.argv) == 4:
    entries[keyphrase] = text
    shelf_file = shelf_file = shelve.open("clip")
    shelf_file["entries"] = entries
    shelf_file.close()

elif command == "delete":
    del entries[keyphrase]
    shelf_file = shelf_file = shelve.open("clip")
    shelf_file["entries"] = entries
    shelf_file.close()

elif command == "list":
    pprint.pprint(entries)
