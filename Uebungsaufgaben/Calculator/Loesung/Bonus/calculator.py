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
        else:
            print("Invalid function!")
            success = False
    else:
        success = False
    return success


def exit_calc():
    print("Exiting calculator...")
    sys.exit()


def main_program():
    print("## Calculator ##")
    print("################")
    
    func_ignore_cases = ["\\"]

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


# Start main program
main_program()

