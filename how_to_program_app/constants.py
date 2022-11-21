# This Python file uses the following encoding: utf-8

import os

from functools import partial
open_latin = partial(open, encoding='UTF-8')

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

# if __name__ == "__main__":
#     pass
