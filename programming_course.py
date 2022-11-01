#!/usr/bin/python3

import os
import sys
import shutil

from console_args import ConsoleArgs as c_args
from task_manager import TaskManager as t_man
from programming_videos import VideoTutorials as vid_tuts


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


def handle_options():
    options = [
        "Video Tutorials",
        "Practicing tasks",
        "EXIT",
    ]

    default_option = 0
    option_int = default_option
    while option_int <= 0 or option_int > len(options):
        print()
        print("Available options:")
        for i, option in enumerate(options):
            print("", i, option)
        print()
        option = input(f"What do you want to do? [{default_option}]: ")
        
        if len(option) == 0:
            option = "0"
        
        if option.isdigit():
            option_int = int(option)
        else:
            option_int = -1
        
        if option_int == 0:
            while vid_tuts.video_wheel():
                another_video = input("Do you want to watch another video? [y/N]: ")

                if len(another_video) == 0:
                    another_video = "n"

                if not another_video.lower() in ["y", "j"]:
                    break
        elif option_int == 1:
            while t_man.task_wheel():
                change_mode_or_info = input("Do you want to change the mode or info level? [y/N] ").lower()
                if change_mode_or_info in ["y", "j"]:
                    c_args.init_data(reset=True)
        elif option_int == 2:
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid option! Please try again.")


def main_program(argc, argv):
    # TODO: make object and give object to other classes and functions
    c_args.handle_arguments(argc, argv)

    print_welcome_message()

    c_args.init_data()

    handle_options()


# Programstart
argc = len(sys.argv) - 1
argv = []
if argc > 0:
    argv = sys.argv[1:]

main_program(argc, argv)

