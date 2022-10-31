import os
import sys
import shutil

from console_args import ConsoleArgs
import os_specific as os_spec


class TaskManager:
    base_dir = "./practice_tasks"

    task_file = "task.txt"
    solution_dir = "solution"
    task_files_dir = "task_files"
    working_dir = "./working_area"

    tasks = []
    current_task_index = -1

    @staticmethod
    def print_available_tasks():
        user_mode_name = ConsoleArgs.get_user_mode_name()
        print(f"Available tasks for {user_mode_name}:")
        
        TaskManager.tasks = []
        mode_base_dir = TaskManager.base_dir + "/" + ConsoleArgs.get_user_mode_name()
        task_dir = os.listdir(mode_base_dir)
        for i in range(len(task_dir)):
            if os.path.isdir(mode_base_dir + "/" + task_dir[i]):
                print("", len(TaskManager.tasks), ":", task_dir[i].replace("_", " "))
                TaskManager.tasks.append(task_dir[i])
        print()
        return len(TaskManager.tasks)

    @staticmethod
    def select_task():
        default_index = 0
        cur_index = -1
        count = 0
        while cur_index < 0 or cur_index >= len(TaskManager.tasks):
            count = TaskManager.print_available_tasks()

            if count <= 0:
                break

            cur_index = -1
            current_task = input("Select task [0]: ")
            if current_task.isdigit():
                cur_index = int(current_task)
            elif len(current_task) == 0:
                cur_index = default_index
            else:
                print("Invalid input! Try again.")

        if count > 0:
            TaskManager.current_task_index = cur_index
            print(f'"{TaskManager.get_cur_task(True)}"', "selected!")
            print()
            return True
        return False

    @staticmethod
    def get_cur_task(fixed=False):
        cur_index = TaskManager.current_task_index
        if cur_index >= 0 and cur_index < len(TaskManager.tasks):
            cur_task = TaskManager.tasks[cur_index]
            if fixed:
                cur_task = cur_task.replace("_", " ")
            return cur_task

    @staticmethod
    def get_task_path(task_name):
        user_mode_name = ConsoleArgs.get_user_mode_name()
        return TaskManager.base_dir + "/" + user_mode_name + "/" + task_name

    @staticmethod
    def read_task_info(path):
        lines = []
        with open(path, "r") as f:
            data_len = 1
            access_granted = True
            while data_len > 0:
                line = f.readline()
                data_len = len(line)
                if data_len > 0:
                    info_level_check = line.strip().rstrip(":").replace(" ", "_").lower()
                    if info_level_check in ConsoleArgs.info_level.keys():
                        info_level = ConsoleArgs.get_info_level()
                        if info_level < ConsoleArgs.info_level[info_level_check]:
                            access_granted = False
                    if access_granted:
                        lines.append(line.rstrip("\n"))
        return lines

    @staticmethod
    def show_task_info():
        cur_task = TaskManager.get_cur_task()
        info_path = TaskManager.get_task_path(cur_task) + "/" + TaskManager.task_file
        if os.path.exists(info_path):
            task_info = TaskManager.read_task_info(info_path)
            print("Task description:")
            for ti in task_info:
                print(ti)
            print()

    @staticmethod
    def prepare_working_dir():
        allowed = True

        cur_task = TaskManager.get_cur_task()
        tf_dir = TaskManager.get_task_path(cur_task) + "/" + TaskManager.task_files_dir
        task_files = os.listdir(tf_dir)

        if not os.path.exists(TaskManager.working_dir):
            os.mkdir(working_dir)

        task_working_dir = TaskManager.working_dir + "/" + cur_task
        if not os.path.exists(task_working_dir):
            os.mkdir(task_working_dir)
        else:
            allowed = False
            print("Warning: Task already started!")
            overwrite = input("Do you want to overwrite? [y/N]: ")
            if overwrite.lower() in ["y", "j"]:
                allowed = True

        if allowed:
            print("Copying task files...", end='')
            for task_file in task_files:
                shutil.copy(tf_dir + "/" + task_file, task_working_dir)
            print("Done")
            print()
            
            print("Opening terminal for coding...", end='')
            os_spec.open_coding_terminal(f'cd "{task_working_dir}" && {os_spec.dir_list_command()}')
            print("Done")
            print()

            # print("Opening file explorer for coding...", end='')
            # os_spec.open_file_browser(task_working_dir)
            # print("Done")
            # print()

            print("Now you can start coding! :)")
            print()

    @staticmethod
    def show_solutions():
        ready = False
        while not ready:
            ready = input("Ready for solutions? [Y/n/q]: ")
            if ready.lower() in ["y", "j"] or len(ready) == 0:
                info_level = ConsoleArgs.get_info_level()
                for key in ConsoleArgs.info_level:
                    if info_level >= ConsoleArgs.info_level[key]:
                        cur_task = TaskManager.get_cur_task()
                        sol_dir = TaskManager.get_task_path(cur_task) + "/" + TaskManager.solution_dir + "/"
                        sol_dir += key.capitalize()
                        if os.path.exists(sol_dir):
                            print(f"Opening terminal for {key} solution...", end='')
                            os_spec.open_coding_terminal(f'cd "{sol_dir}" && {os_spec.dir_list_command()}')
                            print("Done")
                            # 
                            # print(f"Opening file explorer for {key} solution...", end='')
                            # os_spec.open_file_browser(sol_dir)
                            # print("Done")
                            # print()

                ready = True
            elif ready.lower() == "q":
                # quit here
                ready = True
            else:
                ready = False
            print()

    @staticmethod
    def task_wheel():
        print()
        print("THIS IS WORK IN PROGRESS!")
        print("Plese report bugs and errors! Thanks! :)")
        print()
        
        if TaskManager.select_task():
            TaskManager.show_task_info()
            TaskManager.prepare_working_dir()
            TaskManager.show_solutions()
        else:
            print("No tasks available in this mode")
        
        another = input("Run another task? [y/N] ")
        return another.lower() in ["y", "j"]



