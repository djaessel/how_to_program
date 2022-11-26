import sys
import random


def readInvalidChars(filePath):
    charies = []
    with open(filePath) as f:
        for line in f:
            charies.extend(line.rstrip("\n").split("\t"))
    return charies


def romanize(text, rotation=0):
    if rotation <= 0:
        rotation = random.choice([i for i in range(ord('B'), ord('Z'))]) - ord('A')

    print(f'Romanizing: "{text}" with', rotation, "into", end=" ")

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

    print('"' + resText + "'")

    return resText, rotation


def deromanize():
    # TODO: create
    pass


def confuse(text, invalid_chars):
    resText = ""
    print(f'Confusing "{text}" into')
    for i in range(0, len(text)):
        n = ""
        for ran in range(random.choice([1,2,3,5,7,9,10,11,12,13,15,19,20])):
            n += random.choice(invalid_chars)
        n += text[i]
        for ran in range(random.choice([1,2,3,5,7,9,10,11,12,13,15,19,20])):
            n += random.choice(invalid_chars)
        resText += n
    print('"' + resText + '"')
    return resText


def saveText(filePath, text):
    with open(filePath, "w") as f:
        f.write(text + "\n")


def main(args):
    cur_text = "NO_TEXT_FOUND"
    if len(args) > 0:
        cur_text = args[0]
    cc = readInvalidChars("filter_characters.txt")
    cur_text, used_rotation = romanize(cur_text)
    cur_text = confuse(cur_text, cc)
    saveText("output.txt", cur_text)


main(sys.argv[1:])

