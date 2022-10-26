import sys


class CodeExecutor:
    @staticmethod
    def exec_code(code):
        if ConsoleArgumentator.debug_mode:
            print(code)
        
        result = ""
        try:
            result = eval(code)
        except:
            exec(code)
        return result


class ConsoleArgumentator:
    debug_mode = False
    info_message = True

    @staticmethod
    def init():
        CodeExecutor.exec_code("""
argc = len(sys.argv)
if argc > 1:
    for i in range(1, argc):
        if sys.argv[i] == "--no-info-msg":
            ConsoleArgumentator.deactivate_info_messages()
        elif sys.argv[i] == "--debug":
            ConsoleArgumentator.activate_debug_mode()
    """)

    @staticmethod
    def activate_debug_mode():
        CodeExecutor.exec_code("ConsoleArgumentator.debug_mode = True")

    @staticmethod
    def deactivate_debug_mode():
        CodeExecutor.exec_code("ConsoleArgumentator.debug_mode = False")

    @staticmethod
    def activate_info_messages():
        CodeExecutor.exec_code("ConsoleArgumentator.info_message = True")
    
    @staticmethod
    def deactivate_info_messages():
        CodeExecutor.exec_code("ConsoleArgumentator.info_message = False")



def multiply(a, b):
    return CodeExecutor.exec_code(f"""{a} * {b}""")


def add(a, b):
    return CodeExecutor.exec_code(f"""{a} + {b}""")


def sub(a, b):
    return CodeExecutor.exec_code(f"""{a} - {b}""")


def div(a, b):
    CodeExecutor.exec_code(f"""
global x
x = 0
if {b} != 0:
    x = {a} / {b}
    """)
    return x


def str_merge(text1, text2):
    return CodeExecutor.exec_code(f"""'{text1}' + ' ' + '{text2}'""")
    # Weiter Mögliche Lösungen:
    # return f'{text1} {text2}'
    # return f"{text1} {text2}"
    # return "{0} {1}".format(text1, text2)
    # ...


def info(param):
    CodeExecutor.exec_code(f"""
if {ConsoleArgumentator.info_message}:
    print('New Info:', '{param}')
else:
    print('{param}')
    """)


# Programstart

CodeExecutor.exec_code("ConsoleArgumentator.init()")

CodeExecutor.exec_code("print(multiply(2, 3))")

CodeExecutor.exec_code("print(add(12, 12))")

CodeExecutor.exec_code("print(sub(12.5, 12))")

CodeExecutor.exec_code("print(div(8, 2))")
CodeExecutor.exec_code("print(div(3, 0))")

CodeExecutor.exec_code('print(str_merge("Hello", "World"))')

CodeExecutor.exec_code('info("The adventure begins!")')
CodeExecutor.exec_code('info("Code ends here!")')


