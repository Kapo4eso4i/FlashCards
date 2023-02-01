#!/usr/bin/env python


with open('./data/ro_50k.txt','r') as file:
    result = open("./data/ro_redacted", "w")
    for line in file:
        word = line.split(" ")[0]
        if len(word) >= 4:
            result.write(f"{word}\n")
    result.close()