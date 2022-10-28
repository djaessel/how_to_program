import sys


def handle_arguments(argc, argv):
    if argc > 0:
        for arg in argv:
            if arg.startswith("--mode="):
                mode = arg.split("=")[1]


def print_welcome_message():
    print()
    print("############################################################")
    print("# || || ||   ||||   ||     ||||   ||||||   ||||||||   |||| #")
    print("# || || ||   ||     ||     ||     ||  ||   || || ||   ||   #")
    print("# || || ||   ||||   ||     ||     ||  ||   || || ||   |||| #")
    print("# || || ||   ||     ||     ||     ||  ||   || || ||   ||   #")
    print("# ||||||||   ||||   ||||   ||||   ||||||   || || ||   |||| #")
    print("############################################################")
    print()
    print("Hello programmer and welcome to the course!")


def main_program(argc, argv):
    handle_arguments(argc, argv)
    print_welcome_message()

    # TODO: add code
    print("THIS IS WORK IN PROGRESS!")

# Programstart
argc = len(sys.argv)
argv = []
if argc > 1:
    argv = sys.argv[1:]

main_program(argc, argv)

