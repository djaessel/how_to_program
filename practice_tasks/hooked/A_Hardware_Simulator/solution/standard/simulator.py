#!/usr/bin/python3

import os
import sys


class Simulator:
    basic_registers = {
        "AX",
        "BX",
        "CX",
        "DX",
    }

    def __init__(self):
        self.registers = {
            "AX":   0x0000,
            "BX":   0x0000,
            "CX":   0x0000,
            "DX":   0x0000,
            "TEST": 0xFFFF,
            "F1":   0x0000,
            "F2":   0x0000,
            "SP":   0x0000,
            "OP":   0x0000,
        }
        self.memory = []
        self.labels = {
            "__START__": 0x0000
        }
        self.label_search = True

    def reset_all_registers(self):
        for key in self.registers:
            self.registers[key] = 0x0000
            # if key.startswith("F"):
            #    self.registers[key] = 0xFFFF
        self.registers["TEST"] = 0xFFFF

    def get_reg_val(self, reg_name):
        # print("get_reg_val", reg_name)
        return self.registers[reg_name]

    def set_reg_val(self, reg_name, val):
        # print("set_reg_val", reg_name, val)
        self.registers[reg_name] = val

    def extract_val(self, arg):
        # print("extract_val", arg)
        valx = arg.lstrip("0x")
        try:
            valx = int(valx, 16)
        except:
            valx = self.get_reg_val(valx)
        return valx

    def add_label(self, label_name):
        address = self.get_reg_val("OP") + 1 # next line is the operation
        self.labels[label_name] = address

    def get_label_address(self, label_name):
        return self.labels[label_name]

    def print_all_registers(self):
        print()
        print("REGISTER", "|", "HEX-VAL", "|", "INT-VAL", "|", "CHAR-VAL")
        for reg_name in self.registers:
            val1 = self.get_reg_val(reg_name)
            if ord('a') <= val1 <= ord('z') or ord('A') <= val1 <= ord('Z') or ord('0') <= val1 <= ord('9'):
                val1char = chr(val1)
            else:
                val1char = "???"
            print(reg_name, "\t", "|", "", end='')
            print("0x" + hex(val1).lstrip("0x").zfill(4).upper(),  " |", "", end='')
            print('{val: <7} |'.format(val=val1), "", end='')
            print(val1char)
        print()

    def memory_push(self, val):
        mem_address = self.get_reg_val("SP")
        self.memory.insert(mem_address, val)
        self.set_reg_val("SP", mem_address + 1)

    def memory_pop(self):
        mem_address = self.get_reg_val("SP")
        if 0 < mem_address <= len(self.memory):
            mem_address -= 1
            valx = self.memory[mem_address]
            if mem_address > 0:
                self.set_reg_val("SP", mem_address - 1)
        else:
            valx = 0x0000 # default when memory is empty
        return valx

    def simulate_mov(self, args):
        reg_name = args[0].strip()
        val2 = self.extract_val(args[1].strip())
        self.set_reg_val(reg_name, val2)

    def simulate_add(self, args):
        reg_name = args[0].strip()
        val1 = self.extract_val(reg_name)
        val2 = self.extract_val(args[1].strip())
        val1 = val1 + val2
        self.set_reg_val(reg_name, val1)
        
    def simulate_sub(self, args):
        reg_name = args[0].strip()
        val1 = self.extract_val(reg_name)
        val2 = self.extract_val(args[1].strip())
        val1 = val1 - val2
        self.set_reg_val(reg_name, val1)

    def simulate_mul(self, args):
        reg_name = args[0].strip()
        val1 = self.extract_val(reg_name)
        val2 = self.extract_val(args[1].strip())
        val1 = val1 * val2
        self.set_reg_val(reg_name, val1)

    def simulate_push(self, args):
        reg_name = args[0].strip()
        val1 = self.extract_val(reg_name)
        self.memory_push(val1)

    def simulate_pop(self, args):
        reg_name = args[0].strip()
        val1 = self.memory_pop()
        self.set_reg_val(reg_name, val1)

    def simulate_pusha(self):
        for reg_name in Simulator.basic_registers:
            self.simulate_push([reg_name])

    def simulate_popa(self):
        for reg_name in Simulator.basic_registers:
            self.simulate_pop([reg_name])

    def simulate_test(self, args):
        print("TODO: SIMULATE TEST WITH:", args)

    def simulate_jump(self, args):
        jump_address = self.get_label_address(args[0])
        return jump_address

    def simulate_res(self):
        print("TODO: HANDLE RES CODE!")

    def simulate_asm_code(self, asm_code, address):
        codes = asm_code.split()
        for i in range(len(codes)):
            codes[i] = codes[i].strip(',').strip()

        # always holds the current execution address
        # self.simulate_mov(["OP", hex(address)])
        self.set_reg_val("OP", address)

        print("Executing:", codes)

        if codes[0].endswith(":"):
            self.add_label(codes[0].rstrip(":"))
            # address -= 1 # since labels are not counted as code

        if self.label_search:
            return address + 1

        if codes[0] == "MOV":
            self.simulate_mov(codes[1:])
        elif codes[0] == "ADD":
            self.simulate_add(codes[1:])
        elif codes[0] == "SUB":
            self.simulate.sub(codes[1:])
        elif codes[0] == "MUL":
            self.simulate_mul(codes[1:])
        elif codes[0] == "PUSH":
            self.simulate_push(codes[1:])
        elif codes[0] == "POP":
            self.simulate_pop(codes[1:])
        elif codes[0] == "PUSHA":
            self.simulate_pusha()
        elif codes[0] == "POPA":
            self.simulate_popa()
        elif codes[0] == "JMP":
            address = self.simulate_jump(codes[1:])
            address -= 1 # otherwise it will be override from return code
        elif codes[0] == "TEST":
            self.simulate_test(codes[1:])
        elif codes[0] == "RES":
            self.simulate_res()

        return address + 1

    def simulate_asm_file(self, file_path):
        asm_codes = self.read_asm_file(file_path)

        for i in range(len(asm_codes) - 1, -1, -1):
            if asm_codes[i].startswith("#"):
                del asm_codes[i]

        # First run is for label search
        address = 0
        while address < len(asm_codes):
            code = asm_codes[address]
            address = self.simulate_asm_code(code, address)

        # Second run is actual simulation
        self.label_search = False
        address = 0
        while address < len(asm_codes):
            code = asm_codes[address]
            address = self.simulate_asm_code(code, address)
            # print(code, address)
        self.print_all_registers()

    def read_asm_file(self, file_path):
        asm_codes = []
        if os.path.exists(file_path):
            with open(file_path, "r") as asm_reader:
                data_len = 1
                while data_len > 0:
                    line = asm_reader.readline()
                    data_len = len(line)
                    if data_len > 0:
                        code = line.strip("\n").strip()
                        if len(code) > 0:
                            asm_codes.append(code)
        
        return asm_codes



