#!/usr/bin/python3

import random


def readWords(filePath):
    words = []
    with open(filePath) as wordsFile:
        for word in wordsFile:
            words.append(word.rstrip('\n'))
    return words


def print_places(word, letter_found):
    print("Guess:", end=" ")
    for i in range(len(word)):
        if word[i] == " ":
            print(" ", end=" ")
        else:
            print(letter_found[i], end=' ')
    print()
    print("      ", end=' ')
    for i in range(len(word)):
        if word[i] == " ":
            print(" ", end=" ")
        else:
            print("_", end=' ')
    print()
    print()


def print_hangman(val):
    FULL_LENGTH = 17
    xy = [1,1,1,1,1,1,1,1]
    if val > 0:
        xy[7] = FULL_LENGTH
    if val > 1:
        for i in range(len(xy) - 1):
            xy[i] = 6
    if val > 2:
        xy[0] = FULL_LENGTH
    if val > 3:
        for i in range(len(xy)):
            xy[i] += 1
    if val > 4:
        xy[1] = FULL_LENGTH
    if val > 5:
        xy[2] = FULL_LENGTH
    if val > 6:
        xy[3] = 13
    if val > 7:
        xy[3] += 1
        xy[4] = xy[3]
    if val > 8:
        xy[3] = FULL_LENGTH
        xy[4] = FULL_LENGTH
    if val > 9:
        xy[5] = 13
    if val > 10: # final chances
        for i in range(len(xy)):
            xy[i] = FULL_LENGTH

    print("HANGMAN:")
    print("      _______    "[0:xy[0]])
    print("     |/      |   "[0:xy[1]])
    print("     |      (_)  "[0:xy[2]])
    print("     |      \|/  "[0:xy[3]])
    print("     |       |   "[0:xy[4]])
    print("     |      / \  "[0:xy[5]])
    print("     |           "[0:xy[6]])
    if val > 1:
        print("  ___|___        "[0:xy[7]])
    else:
        print("  _______        "[0:xy[7]])


def hangmanGame(words):
    hangman_val = 0
    cur_word = random.choice(words)
    # max_chances = len(cur_word) + 2
    max_chances = 11
    cur_letter_found = []
    for i in range(len(cur_word)):
        cur_letter_found.append(" ")

    not_done = True
    while not_done:
        print_places(cur_word, cur_letter_found)
        print_hangman(hangman_val)
        
        print()
        print("You have", (max_chances - hangman_val), "chance(s) left")
        letter = input("What letter or what's the word? ")
        letter = letter.lower()
        if letter == cur_word:
            # found word
            for i in range(len(cur_word)):
                cur_letter_found[i] = cur_word[i]
        else:
            if letter in cur_word:
                # guessed a letter
                posi = cur_word.find(letter)
                while posi >= 0:
                    cur_letter_found[posi] = letter
                    posi = cur_word.find(letter, posi + 1)
            else:
                # incorrect letter guess
                hangman_val += 1
        
        not_done = False
        for i in range(len(cur_word)):
            if cur_letter_found[i] == " " and cur_word[i] != " ":
                not_done = True

        if hangman_val > max_chances:
            not_done = False


    print_places(cur_word, cur_letter_found)
    print_hangman(hangman_val)
    print()
    if hangman_val <= max_chances:
        print("You found it!")
    else:
        print("You lost!", "The word was:", cur_word)

    yes = input("Want another round? [Y/n]")
    return len(yes) == 0 or yes.lower() in ["y", "j"]


if __name__ == "__main__":
    words = readWords("words.txt")
    while hangmanGame(words):
        pass
    print("Bye!")

