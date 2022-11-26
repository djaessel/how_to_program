#!/usr/bin/python3

import re
import sys


def readFilterCharacters(filepath):
    chars = []
    with open(filepath) as f:
        for line in f:
            chars.extend(line.rstrip('\n').split('\t'))
    return chars
    

# def filterChar(text, chars):
#     if len(chars) <= 0:
#         return text
#
#     resText = ""
#     for i in range(len(text)):
#         if text[i] != chars[0]:
#             resText += text[i]
#     chars = chars[1:]
#
#     if len(chars) > 0:
#         resText = filterChar(resText, chars)
#
#     return resText


def filterCharNew(text, regex):
    resText = re.sub(regex, "", text)
    return resText

    
def fixFile(to_be_filtered_file):
    with open(to_be_filtered_file) as ff:
        to_be_filtered = ff.read()

    # filter_chars = readFilterCharacters("filter_characters.txt")
    # filtered_text = filterChar(to_be_filtered, filter_chars)
    filtered_text = filterCharNew(to_be_filtered, '[^0-9A-Za-z :.,]')
    return filtered_text


def decode_roman(text, rotation):
    resText = ""

    for i in range(len(text)):
        lower = ord(text[i]) <= ord('Z')
        x = ord(text[i]) + rotation
        if lower and x > ord('Z'):
            x = rotation - (ord('Z') - ord(text[i]))
            x = ord('A') + x
        elif x > ord('z'):
            x = rotation - (ord('z') - ord(text[i]))
            x = ord('a') + x

        resText += chr(x)

    return resText


def try_roman_decryption(text):
    cur_decoded_text = ""
    for i in range(ord('Z') - ord('A')):
        cur_decoded_text = decode_roman(text, i)
        print("Original:", text)
        print("Decoded:", cur_decoded_text)
        print("Current rotation:", i)
        okay = input("Is okay? [Y/n] ")
        if len(okay) == 0 or okay.lower() == "y":
            break
    return cur_decoded_text


if __name__ == "__main__":
    filex = "testfile1.txt"
    if len(sys.argv) > 1:
        filex = sys.argv[1]

    text = fixFile(filex).rstrip("\n")
    text = try_roman_decryption(text)

    print("Saving", text, "into file")
    with open("modified_" + filex, "w") as f:
        f.write(text + "\n")
        


