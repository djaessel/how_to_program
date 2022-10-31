import os
import sys


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


def open_file_browser(path):
    path = path.replace('\\', '\\\\').replace('"', '\\"')
    if sys.platform.startswith("linux"):
        # this only works on Ubuntu or other linux with nautilus installed!!!
        # shell_command = "gnome-open {path}"
        shell_command = "nautilus {path}"
        print(shell_command)
        os.system(shell_command)
    elif sys.platform == "win32":
        shell_command = "start {path}"
        # shell_command = "explorer {path}"
        os.system(shell_command)
    else:
        print("ERROR: Unknown operating system!")
        print("Please open the file explorer manually")


