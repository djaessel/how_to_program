import sys
import platform


def python_main_version():
    python_version = platform.python_version()
    main_version = python_version.split('.')[0]
    return int(main_version)


def is_python_3():
    version = python_main_version()
    return version == 3


def is_python_2():
    version = python_main_version()
    return version == 2

