#! python3
"""A mad libs game where the keywords in a text file are replaced by words
chosen by the user."""

import re

madlibs = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")

sentence = open("sentence.txt")
text = sentence.read()
sentence.close()

matches = madlibs.findall(text)

for word in matches:
    if word[0] in ["AEIOUaeiou"]:
        article = "an"
    else:
        article = "a"
    new_word = input(f"Enter {article} {word}: ")
    text = text.replace(word, new_word, 1)

print(text)
sentence = open("sentence.txt", "w")
sentence.write(text)
sentence.close()
