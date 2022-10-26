import os
#import subprocess


last_command = ""
while last_command != "exit":
    print()
    last_command = input("> ")
    #subprocess.Popen(last_command, shell=True)
    os.system(last_command)

