import os
import sys
import shutil


class ConsoleArgs:
    save_file = ".settings"

    default_run_mode = 0x00
    current_run_mode = default_run_mode

    mode_argument = False
    info_argument = False

    modes = {
        "beginner":     0x10,
        "advanced":     0x20,
        "hooked":       0x30,
        }

    info_level = {
        "standard":     0x00,
        "bonus":        0x01,
        "extra_bonus":  0x02,
        }


    @staticmethod
    def read_saved_data():
        if os.path.exists(ConsoleArgs.save_file):
            with open(ConsoleArgs.save_file, "rb") as f:
                bdata = f.read()
                mai = int.from_bytes(bdata, "big")
                ConsoleArgs.set_run_mode_val(mai)

    @staticmethod
    def save_data():
        with open(ConsoleArgs.save_file, "wb") as f:
            run_mode = ConsoleArgs.get_run_mode() & 0xFF
            run_mode_bdata = run_mode.to_bytes(1, "big")
            f.write(run_mode_bdata)

    @staticmethod
    def init_data(reset=False):
        if reset:
            ConsoleArgs.mode_argument = False
            ConsoleArgs.info_argument = False

        if ConsoleArgs.current_run_mode == ConsoleArgs.default_run_mode:
            ConsoleArgs.read_saved_data()
            run_mode = ConsoleArgs.get_run_mode()
            default_mode = (run_mode & 0xF0) >> 4
            default_info = (run_mode & 0x0F)
            mode_int = 0
            info_level_int = -1

            if not ConsoleArgs.mode_argument:
                max_mode = 123456789
                while max_mode < mode_int or mode_int < 1:
                    mode_int = 0

                    print()
                    print("Select a mode:")
                    for key in ConsoleArgs.modes:
                        print("-", key, "=", ConsoleArgs.modes[key] >> 4)
                        max_mode = ConsoleArgs.modes[key] >> 4

                    mode_s = input(f"Mode [{default_mode}]: ")
                    if len(mode_s) == 0:
                        mode_int = default_mode
                    elif mode_s.isdigit():
                        mode_int = int(mode_s)
                    else:
                        print("Invalid input! Try again.")

            if not ConsoleArgs.info_argument:
                max_info_level = 123456789
                while max_info_level < info_level_int or info_level_int < 0:
                    info_level_int = -1

                    print()
                    print("Select info level:")
                    for key in ConsoleArgs.info_level:
                        print("-", key, "=", ConsoleArgs.info_level[key])
                        max_info_level = ConsoleArgs.info_level[key]

                    info_level_s = input(f"Info Level [{default_info}]: ")
                    if len(info_level_s) == 0:
                        info_level_int = default_info
                    elif info_level_s.isdigit():
                        info_level_int = int(info_level_s)
                    else:
                        print("Invalid input! Try again.")

            if mode_int > 0 and info_level_int >= 0:
                run_mode = (mode_int << 4) | info_level_int
                ConsoleArgs.set_run_mode_val(run_mode)

        ConsoleArgs.save_data()


    @staticmethod
    def handle_arguments(argc, argv):
        if argc > 0:
            for arg in argv:
                if arg.startswith("--mode=") or arg.startswith("-m="):
                    mode = arg.split("=")[1]
                    ConsoleArgs.set_run_mode(mode)
                    ConsoleArgs.mode_argument = True
                elif arg.startswith("--info-level=") or arg.startswith("-i="):
                    info_l = arg.split("=")[1]
                    ConsoleArgs.set_run_mode(info_level=info_l)
                    ConsoleArgs.info_argument = True

    @staticmethod
    def set_run_mode_val(val):
        if type(val) == type(0):
            ConsoleArgs.current_run_mode = val
            return True
        return False

    @staticmethod
    def set_run_mode(mode="", info_level="standard"):
        if len(mode) == 0 and info_level in ConsoleArgs.info_level.keys():
            ConsoleArgs.current_run_mode |= ConsoleArgs.info_level[info_level]
        elif mode in ConsoleArgs.modes.keys() and info_level in ConsoleArgs.info_level.keys():
            ConsoleArgs.current_run_mode = ConsoleArgs.modes[mode] | ConsoleArgs.info_level[info_level]

    @staticmethod
    def get_run_mode():
        return ConsoleArgs.current_run_mode

    @staticmethod
    def get_info_level():
        return ConsoleArgs.current_run_mode & 0x0F

    @staticmethod
    def get_info_level_name():
        name = "NOT_FOUND"
        user_mode = ConsoleArgs.get_info_level()
        for key, val in ConsoleArgs.info_level.items():
            if val == user_mode:
                name = key
        return name

    @staticmethod
    def get_user_mode():
        return (ConsoleArgs.current_run_mode & 0xF0) >> 4

    @staticmethod
    def get_user_mode_name():
        name = "NOT_FOUND"
        user_mode = ConsoleArgs.get_user_mode() << 4
        for key, val in ConsoleArgs.modes.items():
            if val == user_mode:
                name = key
        return name

