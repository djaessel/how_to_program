#!/usr/bin/python3

import os
import sys

# adding course_program to the system path
sys.path.insert(0, os.path.join('.', 'how_to_program_app'))
sys.path.insert(0, os.path.join('..', 'how_to_program_app'))
sys.path.insert(0, os.path.join('.', 'course_program'))
sys.path.insert(0, os.path.join('..', 'course_program'))

import version_check as ver


if ver.is_python_3():
   err = os.system("pip3 install PySide6")
   if err != 0:
       err = os.system("pip install PySide6")

   import how_to_program_app as app
   app.main()
else:
    os.system("python --version")
    print("You are not using Python3.")
    print("In case you installed Python3, make sure it is in the PATH variable.")
    print("Maybe try 'python3' instead of simply python")


