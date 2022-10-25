import os
#import sys
import shutil
from datetime import datetime


echo_mode = True # bad habit to do it here, but works


def command_cd(command_data):
    l = len(command_data)
    if l == 2:
        path = command_data[1]
        if os.path.exists(path) and os.path.isdir(path):
            os.chdir(path)
    elif l == 1:
        current_directory = os.getcwd()
        print(current_directory)
    else:
        print("Das System kann den angegebenen Pfad nicht finden.")


def command_cls():
    #os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    print("\033c", end='') # COOL you found it! :) - If not, then it is okay as well.


def file_size_output(size):
    s = str(size)
    l = len(s)
    li = list(s)
    if l > 3:
        li.insert(l - 3, '.')
    if l > 6:
        li.insert(l - 6, '.')
    if l > 9:
        li.insert(l - 9, '.')
    if l > 12:
        li.insert(l - 12, '.')
    if l > 15:
        li.insert(l - 15, '.')
    return "".join(li)


def empty_size_output(max_size):
    x = len(max_size)
    empty_output = ""
    for i in range(x):
        empty_output += " "
    return empty_output


def command_dir():
    path = os.getcwd()
    entries = os.listdir(path)

    biggest_size = 0
    for entry in entries:
        whole_path = path + "/" + entry
        if os.path.isfile(whole_path):
            file_size = os.path.getsize(whole_path)
            if file_size > biggest_size:
                biggest_size = file_size

    biggest_size_out = file_size_output(biggest_size)

    for entry in entries:
        whole_path = path + "/" + entry
        modified_time = os.path.getmtime(whole_path)
        dt_object = datetime.fromtimestamp(modified_time)
        time_string = str(dt_object).split(".")[0]
        time_string = time_string.replace("-", ".")
        if os.path.isdir(whole_path):
            empty_size = empty_size_output(biggest_size_out)
            print(time_string, "   ", "<DIR>", "\t", empty_size, entry)
        else:
            file_size = os.path.getsize(whole_path)
            file_size_out = file_size_output(file_size)
            print(time_string, "   ", "\t", file_size_out, entry)


def command_echo(command_data):
    l = len(command_data)
    global echo_mode # :O BAD! BAD! BAD! But hey, it works :D
    if l > 2:
        output = ""
        for i in range(1, len(command_data)):
            output += command_data[i] + " "
        output = output.rstrip()
        print(output)
    elif l == 1:
        if echo_mode:
            print("ECHO ist eingeschaltet (ON).")
        else:
            print("ECHO ist ausgeschaltet (OFF).")
    elif l == 2:
        data = command_data[1]
        if data == "on":
            echo_mode = True
        elif data == "off":
            echo_mode = False
        else:
            print(data)


#def command_exit():
# TODO: write code to execute before exit


def print_help_info(command, info):
    extra_info = ""
    if len(info) > 60:
        extra_info = info[60:].lstrip()
        info = info[:60]
    print(command, "\t\t", info)
    if len(extra_info) > 0:
        print("\t\t", extra_info)


def command_help():
    print_help_info("CD", "Zeigt den Namen des aktuellen Verzeichnisses an bzw. ändert diesen.")
    print_help_info("CLS", "Löscht den Bildschirminhalt.")
    print_help_info("DIR", "Listet die Dateien und Unterverzeichnisse eines Verzeichnisses auf.")
    print_help_info("ECHO", "Zeigt Meldungen an bzw. schaltet die Befehlsanzeige ein oder aus.")
    print_help_info("EXIT", "Beendet das Programm CMD.EXE (Befehlsinterpreter).")
    print_help_info("HELP", "Zeigt Hilfeinformationen zu Windows-Befehlen an.")
    print_help_info("MOVE", "Verschiebt ein oder mehrere Dateien von einem Verzeichnis in ein anderes.")


def command_move(command_data):
    l = len(command_data)
    if l == 3:
        old_path = command_data[1]
        new_path = command_data[2]
        if os.path.exists(old_path):
            shutil.move(old_path, new_path)
            print("\t\t", "1 Datei(en) verschoben.")
        else:
            print("Das System kann die angegebene Datei nicht finden.")
    elif l == 2:
        old_path = command_data[1]
        if os.path.exists(old_path):
            # shutil.move(old_path, old_path)
            print("\t\t", "1 Datei(en) verschoben.")
        else:
            print("Das System kann die angegebene Datei nicht finden.")
    else:
        print("Syntaxfehler.")


def handle_command(command_line):
    command_data = command_line.split()
    command = command_data[0].lower()

    if command == "cd":
        command_cd(command_data)
    elif command == "cls":
        command_cls()
    elif command == "dir":
        command_dir()
    elif command == "echo":
        command_echo(command_data)
#    elif command == "exit":
#        command_exit() # not necessary to do something here
    elif command == "help":
        command_help()
    elif command == "move":
        command_move(command_data)

    print()


def main_program():
    print()

    last_command = ""
    while last_command != "exit":
        if echo_mode:
            current_path = os.getcwd()
            last_command = input(current_path + "> ")
        else:
            last_command = input("")

        handle_command(last_command)


# Start des Programms
main_program()

