#!/usr/bin/python3

import os
import sys

# adding course_program to the system path
sys.path.insert(0, './course_program')

import version_check as ver


if ver.is_python_3():
   import programming_course as pro_c
   pro_c.main()
else:
    os.system("python --version")
    print("You are not using Python3.")
    print("In case you installed Python3, make sure it is in the PATH variable.")
    print("Maybe try 'python3' instead of simply python")


