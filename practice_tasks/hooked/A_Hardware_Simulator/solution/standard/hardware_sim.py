#!/usr/bin/python3

import os
import sys
from simulator import Simulator


def main():
    simulate_file = "./asm_codes/asm_codes_1.asm"
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1] and os.path.isfile(sys.argv[1])):
            simulate_file = sys.argv[1]
        else:
            print("Invalid file path:", sys.argv[1])

    sim = Simulator()
    sim.simulate_asm_file(simulate_file)


main()


