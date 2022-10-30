import os
#import subprocess

invalid_commands = [
    "shutdown",
    "reboot",
    "logout",
    "exit",
]

def command_valid(command):
    valid = True
    for c in invalid_commands:
        if command.strip().startswith(c):
            valid = False
    return valid


last_command = ""
while last_command != "exit" and last_command != "logout":
    print()
    last_command = input("> ")
    if command_valid(last_command):
        #subprocess.Popen(last_command, shell=True)
        os.system(last_command)

