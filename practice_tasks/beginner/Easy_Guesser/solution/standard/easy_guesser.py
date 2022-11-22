#!/usr/bin/python3
import random


def guessLetter(guess_start='A', guess_end='Z'):
    cx = random.choice([c for c in range(ord(guess_start), ord(guess_end) + 1)])
    return chr(cx)


def main():
    start_c = 'A'
    end_c = 'Z'
    
    upper = input("Is it an upper case letter? [y/n]: ")
    if upper.lower() != "y" and len(upper) > 0:
        start_c = 'a'
        end_c = 'z'

    while True:
        c = guessLetter(start_c, end_c)
        print("Is your letter", c, "?", end='')
        yes = input("[y/n] ")
        if len(yes) == 0 or yes.lower() == "y":
            break

        yes = input("Comes your letter before this one? [y/n] ")
        if len(yes) == 0 or yes.lower() == "y":
            end_c = chr(ord(c) - 1)
        else:
            start_c = chr(ord(c) + 1)

    print("YAY! I guessed it!")
    yes = input("Want another run? [y/n] ")
    if len(yes) == 0 or yes.lower() == "y":
        main()
    else:
        print("BYE!")


main()

