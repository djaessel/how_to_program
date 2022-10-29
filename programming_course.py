#!/usr/bin/python3

import os
import sys


class ConsoleArgs:
    current_run_mode = 0x10
    save_file = ".settings"

    modes = {
        "beginner":     0x10,
        "advanced":     0x20,
        "hooked":       0x30,
        }
    info_level = {
        "standard":     0x00,
        "bonus":        0x01,
        "extra_bonus":  0x02,
        }

    @staticmethod
    def read_saved_data():
        if os.path.exists(ConsoleArgs.save_file):
            with open(ConsoleArgs.save_file, "rb") as f:
                bdata = f.read()
                mai = int.from_bytes(bdata, "big")
                ConsoleArgs.set_run_mode_val(mai)

    @staticmethod
    def save_data():
        with open(ConsoleArgs.save_file, "wb") as f:
            run_mode = ConsoleArgs.get_run_mode() & 0xFF
            run_mode_bdata = run_mode.to_bytes(1, "big")
            f.write(run_mode_bdata)

    @staticmethod
    def init_data():
        ConsoleArgs.read_saved_data()
        run_mode = ConsoleArgs.get_run_mode()
        default_mode = (run_mode & 0xF0) >> 4
        default_info = (run_mode & 0x0F)

        max_mode = 123456789
        mode_int = 0
        while max_mode < mode_int or mode_int < 1:
            mode_int = 0

            print()
            print("Select a mode:")
            for key in ConsoleArgs.modes:
                print("-", key, "=", ConsoleArgs.modes[key] >> 4)
                max_mode = ConsoleArgs.modes[key] >> 4

            mode_s = input(f"Mode [{default_mode}]: ")
            if len(mode_s) == 0:
                mode_int = default_mode
            elif mode_s.isdigit():
                mode_int = int(mode_s)
            else:
                print("Invalid input! Try again.")

        max_info_level = 123456789
        info_level_int = -1
        while max_info_level < info_level_int or info_level_int < 0:
            info_level_int = -1

            print()
            print("Select info level:")
            for key in ConsoleArgs.info_level:
                print("-", key, "=", ConsoleArgs.info_level[key])
                max_info_level = ConsoleArgs.info_level[key]
            
            info_level_s = input(f"Info Level [{default_info}]: ")
            if len(info_level_s) == 0:
                info_level_int = default_info
            elif info_level_s.isdigit():
                info_level_int = int(info_level_s)
            else:
                print("Invalid input! Try again.")

        run_mode = (mode_int << 4) | info_level_int
        ConsoleArgs.set_run_mode_val(run_mode)
        ConsoleArgs.save_data()


    @staticmethod
    def handle_arguments(argc, argv):
        if argc > 0:
            for arg in argv:
                if arg.startswith("--mode=") or arg.startswith("-m="):
                    mode = arg.split("=")[1]
                    ConsoleArgs.set_run_mode(mode)
                elif arg.startswith("--info-level=") or arg.startswith("-i="):
                    info_l = arg.split("=")[1]
                    ConsoleArgs.set_run_mode(info_level=info_l)

    @staticmethod
    def set_run_mode_val(val):
        if type(val) == type(0):
            ConsoleArgs.current_run_mode = val
            return True
        return False

    @staticmethod
    def set_run_mode(mode="", info_level="standard"):
        if len(mode) == 0 and info_level in ConsoleArgs.info_level.keys():
            ConsoleArgs.current_run_mode |= ConsoleArgs.info_level[info_level]
        elif mode in ConsoleArgs.modes.keys() and info_level in ConsoleArgs.info_level.keys():
            ConsoleArgs.current_run_mode = ConsoleArgs.modes[mode] | ConsoleArgs.info_level[info_level]

    @staticmethod
    def get_run_mode():
        return ConsoleArgs.current_run_mode


class TaskManager:
    base_dir = "./Uebungsaufgaben"
    tasks = []
    current_task_index = -1

    @staticmethod
    def print_available_tasks():
        print("Available tasks:")
        
        TaskManager.tasks = []
        task_dir = os.listdir(TaskManager.base_dir)
        for i in range(len(task_dir)):
            if os.path.isdir(TaskManager.base_dir + "/" + task_dir[i]):
                print("", len(TaskManager.tasks), ":", task_dir[i].replace("_", " "))
                TaskManager.tasks.append(task_dir[i])
        print()

    @staticmethod
    def select_task():
        default_index = 0
        cur_index = TaskManager.current_task_index
        while cur_index < 0 or cur_index >= len(TaskManager.tasks):
            TaskManager.print_available_tasks()

            cur_index = -1
            current_task = input("Select task [0]: ")
            if current_task.isdigit():
                cur_index = int(current_task)
            elif len(current_task) == 0:
                cur_index = default_index
            else:
                print("Invalid input! Try again.")

        TaskManager.current_task_index = cur_index
        print(f'"{TaskManager.get_cur_task(True)}"', "selected!")
        print()

    @staticmethod
    def get_cur_task(fixed=False):
        cur_index = TaskManager.current_task_index
        if cur_index >= 0 and cur_index < len(TaskManager.tasks):
            cur_task = TaskManager.tasks[cur_index]
            if fixed:
                cur_task = cur_task.replace("_", " ")
            return cur_task

    @staticmethod
    def get_task_path(task_name):
        return TaskManager.base_dir + "/" + task_name

    @staticmethod
    def read_task_info(path):
        lines = []
        # TODO: make mode and info level specific
        with open(path, "r") as f:
            data_len = 1
            while data_len > 0:
                line = f.readline()
                data_len = len(line)
                if data_len > 0:
                    lines.append(line.rstrip("\n"))
        return lines

    @staticmethod
    def show_task_info():
        cur_task = TaskManager.get_cur_task()
        info_path = TaskManager.get_task_path(cur_task) + "/Aufgabe.txt"
        if os.path.exists(info_path):
            task_info = TaskManager.read_task_info(info_path)
            print("Task description:")
            for ti in task_info:
                print(ti)
            print()


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
    ConsoleArgs.handle_arguments(argc, argv)

    print_welcome_message()

    ConsoleArgs.init_data()

    # TODO: add code
    print()
    print("THIS IS WORK IN PROGRESS!")
    print()

    TaskManager.select_task()
    TaskManager.show_task_info()



# Programstart
argc = len(sys.argv)
argv = []
if argc > 1:
    argv = sys.argv[1:]

main_program(argc, argv)

