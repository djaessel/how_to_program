import sys


info_message = True


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    if b == 0:
        return 0
    return a / b


def str_merge(text1, text2):
    return text1 + " " + text2
    # Weiter Mögliche Lösungen:
    # return f'{text1} {text2}'
    # return f"{text1} {text2}"
    # return "{0} {1}".format(text1, text2)
    # ...


def info(param):
    if info_message:
        print("New Info:", param)
    else:
        print(param)


# Programstart
info_message = True

argc = len(sys.argv)
if argc > 1:
    for i in range(1, argc):
        if sys.argv[i] == "--no-info-msg":
            info_message = False


print(multiply(2, 3))

print(add(12, 12))

print(sub(12.5, 12))

print(div(8, 2))
print(div(3, 0))

print(str_merge("Hello", "World"))

info("The adventure begins!")
info("Code ends here!")


