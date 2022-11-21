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
        # shell_command = f"start cmd /k \"{command}\""
        shell_command = f"start /B \"{command}\""
        os.system(shell_command)
    else:
        print("ERROR: Unknown operating system!")
        print("Please open the terminal manually")
        print(f"Example command: {command}")


def open_file_browser(path):
    path = path.replace('\\', '\\\\').replace('"', '\\"')
    if sys.platform.startswith("linux"):
        # this only works on Ubuntu or other linux with nautilus installed!!!
        # shell_command = f"gnome-open {path}"
        shell_command = f"thunar {path}"
        x = os.system(shell_command)
        if x != 0:
            shell_command = f"nautilus {path}"
            os.system(shell_command) # maybe add more checks

    elif sys.platform == "win32":
        shell_command = f"start {path}"
        # shell_command = f"explorer {path}"
        os.system(shell_command)
    else:
        print("ERROR: Unknown operating system!")
        print("Please open the file explorer manually")


def open_url(url):
    success = False
    if url.startswith("http://") or url.startswith("https://"):
        os.system(f"firefox {url}")
        success = True
    else:
        print("Can't open url:", url)
        print("Only http or https urls allowed!")
    return success


