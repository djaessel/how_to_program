import sys


def handle_number(num_text):
    try:
        num = int(num_text)
    except:
        print("Only whole numbers allowed!")
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
        num2 = int(num1 / num2)
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
    
    last_command = ""
    func_text = 0
    last_num = 0
    while last_command != "x":
        num = "NaN"
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

