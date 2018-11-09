#!/usr/bin/python

import re

charset = {"B": 1, "c": 1, "e": 7, "E": 1, "F": 1, "g": 1, "i": 3, "n": 3, "r": 4, "s": 1, "S": 1, "t": 5, "u": 3, "U": 1, "y": 1}
mask = ",@@@@,@@@@@@@,@@@@@@@@,@@@@@,@@@@@"

corpus = dict()
with open("20k.txt") as file:
    for line in file:
        word = line.rstrip()
        if len(word) not in corpus:
            corpus[len(word)] = []
        corpus[len(word)].append(word.capitalize())

def find_words(mask, charset, words):
    pattern = re.compile("^,@+")
    matches = pattern.match(mask)

    if not matches:
        words.insert(3, "4")
        print ''.join(words)
        return

    match = matches.group(0)

    for word in corpus[len(match)]:
        cs = charset.copy()
        flg = True
        for c in word:
            if c in cs:
                cs[c] -= 1
                if cs[c] == 0:
                    del cs[c]
            else:
                flg = False
                break
        if flg:
            ws = list(words)
            ws.append(word)
            find_words(pattern.sub("", mask), cs, ws)

find_words(mask, charset, [])

