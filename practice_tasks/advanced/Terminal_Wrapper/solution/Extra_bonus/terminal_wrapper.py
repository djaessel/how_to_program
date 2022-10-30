import os
#import subprocess

invalid_commands = {
    "shutdown",
    "reboot",
    "logout",
    "exit",
    }

exit_commands = {
    "exit",
    "logout",
    }


def is_exit_command(command):
    return (command in exit_commands)


def command_valid(command):
    valid = True
    for c in invalid_commands:
        if command.strip().startswith(c):
            valid = False
    return valid


last_command = ""
while not is_exit_command(last_command):
    print()
    last_command = input("> ")
    if command_valid(last_command):
        #subprocess.Popen(last_command, shell=True)
        os.system(last_command)
    elif not is_exit_command(last_command):
        print(f"{last_command} is not a valid command!")

