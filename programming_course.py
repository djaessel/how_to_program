#!/usr/bin/python3

import os
import sys
import shutil

from console_args import ConsoleArgs as c_args
from task_manager import TaskManager as t_man


def print_welcome_message():
    welcome_file = ".welcome_message"
    if os.path.exists(welcome_file):
        with open(welcome_file, "r") as f:
            data_len = 1
            while data_len > 0:
                line = f.readline()
                data_len = len(line)
                if data_len > 0:
                    print(line.rstrip('\n'))
    else:
        print("Hello!\n")


def main_program(argc, argv):
    # TODO: make object and give object to other classes and functions
    c_args.handle_arguments(argc, argv)

    print_welcome_message()

    c_args.init_data()

    while t_man.task_wheel():
        change_mode_or_info = input("Do you want to change the mode or info level? [y/N] ").lower()
        if change_mode_or_info in ["y", "j"]:
            c_args.init_data(True)


# Programstart
argc = len(sys.argv) - 1
argv = []
if argc > 0:
    argv = sys.argv[1:]

main_program(argc, argv)

