#!/usr/bin/python3

import os
import shutil


def get_info_modes():
    return [
        "standard",
        "bonus",
        "extra_bonus",
    ]


def get_modes():
    base_dir = "./"
    folders = os.listdir(base_dir)
    for mode in folders:
        if not os.path.isdir(base_dir + mode):
            folders.remove(mode)
    return folders


def list_modes():
    print("Available modes:")
    modes = get_modes()
    for i, mode in enumerate(modes):
        print("", i, ":", mode)


def select_mode():
    list_modes()
    modes = get_modes()

    mode = ""
    mode_int = -1
    if len(modes) > 0:
        mode = input("Select modes [0]: ")

        if len(mode) == 0:
            mode = "0"

        mode_int = -1
        if mode.isdigit():
            mode_int = int(mode)

        if 0 <= mode_int < len(modes):
            selected_mode = modes[mode_int]
            print(f"Selected {selected_mode}!")
        else:
            print("Invalid input! Please try again.")

    return mode_int


def set_task_name():
    task_name = ""
    while len(task_name) == 0:
        task_name = input("Enter task name: ")
        
        if task_name.isdigit() or task_name[0].isdigit():
            task_name = ""

        task_name = task_name.replace(" ", "_")

    return task_name


def set_program_name():
    name = ""
    while len(name) == 0:
        name = input("Enter program name: ")
        
        if name.isdigit() or name[0].isdigit():
            name = ""

    return name.lower().replace(" ", "_")

def create_folders_and_files(name, program_name, mode):
    info_modes = get_info_modes()
    if not os.path.exists(name):
        base_folder = "./" + mode + "/" + name
        base_solution_folder = base_folder + "/solution"
        os.mkdir(base_folder)
        os.mkdir(base_solution_folder)
        for mode in info_modes:
            os.mkdir(base_solution_folder + "/" + mode)

        with open(base_folder + "/task.txt", "w") as f:
            f.write("Empty Note\n")

        task_files_folder = base_folder + "/task_files"
        os.mkdir(task_files_folder)

        program_file_path = task_files_folder + "/" + program_name + ".py"
        with open(program_file_path, "w") as f:
            f.write("#!/usr/bin/python3\n")
            f.write("\n")
            f.write('if __name__ == "__main__":\n')
            f.write("    # TODO: your code goes here :)\n")
            f.write("    pass\n")
            f.write("\n")

        for mode in info_modes:
            sol_dir = base_solution_folder + "/" + mode
            shutil.copy(program_file_path, sol_dir)
    else:
        print(name, "already exists!")


def main():
    mode = ""
    while mode == "":
        mode = select_mode()

    task_name = set_task_name()
    program_name = set_program_name()

    modes = get_modes()
    create_folders_and_files(task_name, program_name, modes[mode])

    print("Done")


main()

