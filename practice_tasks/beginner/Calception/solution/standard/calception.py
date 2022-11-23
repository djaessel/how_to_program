#!/usr/bin/python3


def readFilterCharacters(filepath):
    chars = []
    with open(filepath) as f:
        for line in f:
            chars.extend(line.rstrip('\n').split('\t'))
    return chars
    

def filterChar(text, chars):
    if len(chars) <= 0:
        return text

    resText = ""
    for i in range(len(text)):
        if text[i] != chars[0]:
            resText += text[i]
    chars = chars[1:]

    if len(chars) > 0:
        resText = filterChar(resText, chars)

    return resText

    
def fixFile(to_be_filtered_file):
    with open(to_be_filtered_file) as ff:
        to_be_filtered = ff.read()

    filter_chars = readFilterCharacters("filter_characters.txt")
    filtered_text = filterChar(to_be_filtered, filter_chars)
    return filtered_text


if __name__ == "__main__":
    text = fixFile("testfile1.txt")
    with open("modified_testfile1.txt", "w") as f:
        f.write(text + "\n")
        


