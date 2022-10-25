import sys
import math


def handle_number(numText):
    try:
        num = float(numText)
    except:
        print("Only numbers allowed!")
        num = "NaN"
    return num


def handle_function(num1, num2, func):
    if func == "+":
        num2 = num1 + num2
    elif func == "-":
        num2 = num1 - num2
    elif func == "*":
        num2 = num1 * num2
    elif func == "/":
        num2 = num1 / num2
    elif func == "^":
        num2 = num1 ** num2
    elif func == "\\":
        num2 = math.sqrt(num1)
    elif func == "c":
        num2 = 0
    else:
        print("Invalid function!")

    return num2


def check_function(func):
    success = True
    if func != 0:
        if func == "+":
            print("Add!")
        elif func == "-":
            print("Subtract!")
        elif func == "*":
            print("Multiply!")
        elif func == "/":
            print("Divide!")
        elif func == "^":
            print("Power!")
        elif func == "\\":
            print("Square root!")
        elif func == "c":
            print("Clearing!")
        else:
            print("Invalid function!")
            success = False
    else:
        success = False
    return success


def exit_calc():
    print("Exiting calculator...")
    sys.exit()


def run_file(filename):
    commands = []
    with open(filename, "r") as f:
        dataLen = 1
        while dataLen > 0:
            line = f.readline().rstrip("\n")
            dataLen = len(line)
            if dataLen > 0:
                commands.append(line)


    func_ignore_cases = ["\\"]
    num_ignore_cases = ["c"]

    cur_index = 0
    last_command = ""
    func_text = 0
    last_num = 0
    while last_command != "x":
        num = "NaN"
        if not func_text in func_ignore_cases:
            while num == "NaN":
                # num_text = input("Enter a number: ")
                print(commands[cur_index])
                num_text = commands[cur_index]
                if num_text != "x":
                    num = handle_number(num_text)
                else:
                    exit_calc()
                cur_index = cur_index + 1

        if func_text != 0:
            last_num = handle_function(last_num, num, func_text)
            print("Result:", last_num)
        else:
            last_num = num

        func_text = 0
        while not check_function(func_text):
            # func_text = input("Function: ")
            print(commands[cur_index])
            func_text = commands[cur_index]
            if func_text == "x":
                exit_calc()
            cur_index = cur_index + 1

        if func_text in num_ignore_cases:
            last_num = handle_function(last_num, num, func_text)
            if func_text == "c":
                func_text = 0




def main_program():
    print("## Calculator ##")
    print("################")
    txt = input("Run file [y/N]: ").lower()
    if txt == "y":
        filename = input("Enter file name: ")
        run_file(filename)
    else:
        default_program()


def default_program():
    func_ignore_cases = ["\\"]
    num_ignore_cases = ["c"]

    last_command = ""
    func_text = 0
    last_num = 0
    while last_command != "x":
        num = "NaN"
        if not func_text in func_ignore_cases:
            while num == "NaN":
                num_text = input("Enter a number: ")
                if num_text != "x":
                    num = handle_number(num_text)
                else:
                    exit_calc()

        if func_text != 0:
            last_num = handle_function(last_num, num, func_text)
            print("Result:", last_num)
        else:
            last_num = num

        func_text = 0
        while not check_function(func_text):
            func_text = input("Function: ")
            if func_text == "x":
                exit_calc()

        if func_text in num_ignore_cases:
            last_num = handle_function(last_num, num, func_text)
            if func_text == "c":
                func_text = 0



# Start main program
main_program()

