#!/usr/bin/python3

import os
import sys
import shutil


task_file = "task.txt"
solution_dir = "solution"
task_files_dir = "task_files"
working_dir = "./working_area"


def dir_list_command():
    if sys.platform.startswith("linux") or sys.platform == "darwin":
        # Linux and OS X
        return "ls -l"
    elif sys.platform == "win32":
        # Windows
        return "dir"
    else:
        return ""


def open_coding_terminal(command):
    command = command.replace('\"', '\\\"')
    if sys.platform.startswith("linux"):
        # Linux
        shell_command = f'gnome-terminal -- bash -c "{command}; exec bash -i"'
        os.system(shell_command)
    elif sys.platform == "win32":
        # Windows
        shell_command = f"start cmd /k \"{command}\""
        os.system(shell_command)
    else:
        print("ERROR: Unknown operating system!")
        print("Please open the terminal manually")
        print(f"Example command: {command}")


class ConsoleArgs:
    save_file = ".settings"

    default_run_mode = 0x00
    current_run_mode = default_run_mode

    mode_argument = False
    info_argument = False

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
    def init_data(reset=False):
        if reset:
            ConsoleArgs.mode_argument = False
            ConsoleArgs.info_argument = False

        if ConsoleArgs.current_run_mode == ConsoleArgs.default_run_mode:
            ConsoleArgs.read_saved_data()
            run_mode = ConsoleArgs.get_run_mode()
            default_mode = (run_mode & 0xF0) >> 4
            default_info = (run_mode & 0x0F)
            mode_int = 0
            info_level_int = -1
            
            if not ConsoleArgs.mode_argument:
                max_mode = 123456789
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
            
            if not ConsoleArgs.info_argument:
                max_info_level = 123456789
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
                
            if mode_int > 0 and info_level_int >= 0:
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
                    ConsoleArgs.mode_argument = True
                elif arg.startswith("--info-level=") or arg.startswith("-i="):
                    info_l = arg.split("=")[1]
                    ConsoleArgs.set_run_mode(info_level=info_l)
                    ConsoleArgs.info_argument = True

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

    @staticmethod
    def get_info_level():
        return ConsoleArgs.current_run_mode & 0x0F

    @staticmethod
    def get_info_level_name():
        name = "NOT_FOUND"
        user_mode = ConsoleArgs.get_info_level()
        for key, val in ConsoleArgs.info_level.items():
            if val == user_mode:
                name = key
        return name

    @staticmethod
    def get_user_mode():
        return (ConsoleArgs.current_run_mode & 0xF0) >> 4

    @staticmethod
    def get_user_mode_name():
        name = "NOT_FOUND"
        user_mode = ConsoleArgs.get_user_mode() << 4
        for key, val in ConsoleArgs.modes.items():
            if val == user_mode:
                name = key
        return name

class TaskManager:
    base_dir = "./practice_tasks"
    tasks = []
    current_task_index = -1

    @staticmethod
    def print_available_tasks():
        user_mode_name = ConsoleArgs.get_user_mode_name()
        print(f"Available tasks for {user_mode_name}:")
        
        TaskManager.tasks = []
        mode_base_dir = TaskManager.base_dir + "/" + ConsoleArgs.get_user_mode_name()
        task_dir = os.listdir(mode_base_dir)
        for i in range(len(task_dir)):
            if os.path.isdir(mode_base_dir + "/" + task_dir[i]):
                print("", len(TaskManager.tasks), ":", task_dir[i].replace("_", " "))
                TaskManager.tasks.append(task_dir[i])
        print()

    @staticmethod
    def select_task():
        default_index = 0
        cur_index = -1
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
        user_mode_name = ConsoleArgs.get_user_mode_name()
        return TaskManager.base_dir + "/" + user_mode_name + "/" + task_name

    @staticmethod
    def read_task_info(path):
        lines = []
        with open(path, "r") as f:
            data_len = 1
            access_granted = True
            while data_len > 0:
                line = f.readline()
                data_len = len(line)
                if data_len > 0:
                    info_level_check = line.strip().rstrip(":").replace(" ", "_").lower()
                    if info_level_check in ConsoleArgs.info_level.keys():
                        info_level = ConsoleArgs.get_info_level()
                        if info_level < ConsoleArgs.info_level[info_level_check]:
                            access_granted = False
                    if access_granted:
                        lines.append(line.rstrip("\n"))
        return lines

    @staticmethod
    def show_task_info():
        cur_task = TaskManager.get_cur_task()
        info_path = TaskManager.get_task_path(cur_task) + "/" + task_file
        if os.path.exists(info_path):
            task_info = TaskManager.read_task_info(info_path)
            print("Task description:")
            for ti in task_info:
                print(ti)
            print()

    @staticmethod
    def prepare_working_dir():
        allowed = True

        cur_task = TaskManager.get_cur_task()
        tf_dir = TaskManager.get_task_path(cur_task) + "/" + task_files_dir
        task_files = os.listdir(tf_dir)

        if not os.path.exists(working_dir):
            os.mkdir(working_dir)

        task_working_dir = working_dir + "/" + cur_task
        if not os.path.exists(task_working_dir):
            os.mkdir(task_working_dir)
        else:
            allowed = False
            print("Warning: Task already started!")
            overwrite = input("Do you want to overwrite? [y/N]: ")
            if overwrite.lower() in ["y", "j"]:
                allowed = True

        if allowed:
            print("Copying task files...", end='')
            for task_file in task_files:
                shutil.copy(tf_dir + "/" + task_file, task_working_dir)
            print("Done")
            print()
            
            # print("Execute the following command to start the task:")
            # print(f'cd "{task_working_dir}" && {dir_list_command()}')
            # print()
            # print("Now open the py file and start coding! :)")
            # print()

            print("Opening terminal for coding...", end='')
            open_coding_terminal(f'cd "{task_working_dir}" && {dir_list_command()}')
            print("Done")
            print()
            print("Now you can start coding! :)")
            print()

    @staticmethod
    def show_solutions():
        ready = False
        while not ready:
            ready = input("Ready for solutions? [Y/n/q]: ")
            if ready.lower() in ["y", "j"] or len(ready) == 0:
                info_level = ConsoleArgs.get_info_level()
                for key in ConsoleArgs.info_level:
                    if info_level >= ConsoleArgs.info_level[key]:
                        cur_task = TaskManager.get_cur_task()
                        sol_dir = TaskManager.get_task_path(cur_task) + "/" + solution_dir + "/"
                        sol_dir += key.capitalize()
                        if os.path.exists(sol_dir):
                            print(f"Opening terminal for {key} solution...", end='')
                            open_coding_terminal(f'cd "{sol_dir}" && {dir_list_command()}')
                            print("Done")
                ready = True
            elif ready.lower() == "q":
                # quit here
                ready = True
            else:
                ready = False
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


def task_wheel():
    # TODO: add code
    print()
    print("THIS IS WORK IN PROGRESS!")
    print("Plese report bugs and errors! Thanks! :)")
    print()

    TaskManager.select_task()
    TaskManager.show_task_info()
    TaskManager.prepare_working_dir()
    TaskManager.show_solutions()

    another = input("Run another task? [y/N] ")
    return another.lower() in ["y", "j"]


def main_program(argc, argv):
    # TODO: make object and give object to other classes and functions
    ConsoleArgs.handle_arguments(argc, argv)

    print_welcome_message()

    ConsoleArgs.init_data()

    while task_wheel():
        change_mode_or_info = input("Do you want to change the mode or info level? [y/N] ").lower()
        if change_mode_or_info in ["y", "j"]:
            ConsoleArgs.init_data(True)


# Programstart
argc = len(sys.argv) - 1
argv = []
if argc > 0:
    argv = sys.argv[1:]

main_program(argc, argv)

