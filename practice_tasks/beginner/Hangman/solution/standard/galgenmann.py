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
    print("HANGMAN: ", val)
    # TODO: actually draw hangman based on value


def hangmanGame(words):
    hangman_val = 0
    cur_word = random.choice(words)
    cur_letter_found = []
    for i in range(len(cur_word)):
        cur_letter_found.append(" ")

    not_done = True
    while not_done:
        print_places(cur_word, cur_letter_found)
        print_hangman(hangman_val)
        
        letter = input("What letter? ")
        letter = letter.lower()
        if letter in cur_word:
            posi = cur_word.find(letter)
            while posi >= 0:
                cur_letter_found[posi] = letter
                posi = cur_word.find(letter, posi + 1)
        else:
            hangman_val += 1
        
        not_done = False
        for i in range(len(cur_word)):
            if cur_letter_found[i] == " " and cur_word[i] != " ":
                not_done = True


    print_places(cur_word, cur_letter_found)
    print_hangman(hangman_val)
    print("You found it!", cur_word)


if __name__ == "__main__":
    words = readWords("words.txt")
    hangmanGame(words)

