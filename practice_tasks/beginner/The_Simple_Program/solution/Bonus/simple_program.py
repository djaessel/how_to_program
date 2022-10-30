import sys


debug_mode = False
info_message = True


def multiply(a, b):
    return exec_code(f"""{a} * {b}""")


def add(a, b):
    return exec_code(f"""{a} + {b}""")


def sub(a, b):
    return exec_code(f"""{a} - {b}""")


def div(a, b):
    data = exec_code(f"""
global x
x = 0
if {b} != 0:
    x = {a} / {b}
""")
    return x


def str_merge(text1, text2):
    return exec_code(f"""'{text1}' + ' ' + '{text2}'""")
    # Weiter Mögliche Lösungen:
    # return f'{text1} {text2}'
    # return f"{text1} {text2}"
    # return "{0} {1}".format(text1, text2)
    # ...


def info(param):
    exec_code(f"""
if {info_message}:
    print('New Info:', '{param}')
else:
    print('{param}')
    """)


def exec_code(code):
    if debug_mode:
        print(code)

    result = ""
    try:
        result = eval(code)
    except:
        exec(code)
    return result


# Programstart

exec_code("""
argc = len(sys.argv)
if argc > 1:
    for i in range(1, argc):
        if sys.argv[i] == "--no-info-msg":
            global info_message
            info_message = False
        elif sys.argv[i] == "--debug":
            global debug_mode
            debug_mode = True
""")

exec_code("print(multiply(2, 3))")

exec_code("print(add(12, 12))")

exec_code("print(sub(12.5, 12))")

exec_code("print(div(8, 2))")
exec_code("print(div(3, 0))")

exec_code('print(str_merge("Hello", "World"))')

exec_code('info("The adventure begins!")')
exec_code('info("Code ends here!")')


