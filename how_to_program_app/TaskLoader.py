# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QmlElement

import os
import shutil
import os_specific as os_spec
from constants import WORKING_DIR

QML_IMPORT_NAME = "TaskLoader"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0 # Optional

@QmlElement
class TaskLoader(QObject):
    base_dir = WORKING_DIR + "\\..\\practice_tasks"

    task_file = "task.txt"
    solution_dir = "solution"
    task_files_dir = "task_files"
    working_dir = WORKING_DIR + "\\..\\working_area"

    tasks = []
    current_task_index = -1

    def __init__(self, parent=None):
        super(TaskLoader, self).__init__(parent)

    @Slot(str, result=int)
    def load_available_tasks(self, user_mode_name):
        TaskLoader.tasks = []
        mode_base_dir = TaskLoader.base_dir + "\\" + user_mode_name
        if os.path.exists(mode_base_dir) and os.path.isdir(mode_base_dir):
            task_dir = os.listdir(mode_base_dir)
            for i in range(len(task_dir)):
                if os.path.isdir(mode_base_dir + "\\" + task_dir[i]):
                    TaskLoader.tasks.append(task_dir[i])
        return len(TaskLoader.tasks)

    @Slot(bool, result=str)
    def get_cur_task(self, fixed=False):
        cur_index = self.current_task_index
        if cur_index >= 0 and cur_index < len(TaskLoader.tasks):
            cur_task = TaskLoader.tasks[cur_index]
            if fixed:
                cur_task = cur_task.replace("_", " ")
            return cur_task

    @Slot(int, result=str)
    def get_task(self, cur_index):
        if cur_index >= 0 and cur_index < len(TaskLoader.tasks):
            cur_task = TaskLoader.tasks[cur_index]
            # cur_task = cur_task.replace("_", " ")
            return cur_task
        return ""

    @Slot(list, result=str)
    def get_task_path(self, params):
        task_name = params[0]
        user_mode_name = params[1]
        return TaskLoader.base_dir + "\\" + user_mode_name + "\\" + task_name

    @Slot(list, result=list)
    def read_task_info(self, params):
        path = params[0].rstrip("\\")
        path = path + "\\" + TaskLoader.task_file
        info_level_keys = params[1]
        info_level = params[2]

        lines = []
        with open(path, "r") as f:
            data_len = 1
            access_granted = True
            while data_len > 0:
                line = f.readline()
                data_len = len(line)
                if data_len > 0:
                    info_level_check = line.strip().rstrip(":").replace(" ", "_").lower()
                    if info_level_check in info_level_keys:
                        if info_level < info_level_keys.index(info_level_check):
                            access_granted = False
                    if access_granted:
                        lines.append(line.rstrip("\n"))
        return lines

    @Slot(int, result=bool)
    def select_path(self, index):
        if index >= 0 and index < len(TaskLoader.tasks):
            self.current_task_index = index
            return True
        return False

    @Slot(list, result=int)
    def prepare_working_dir(self, params):
        allowed = True
        result = 0x0

        user_mode_name = params[0]
        override_workdir = eval(str(params[1]).capitalize())

        cur_task = self.get_cur_task()
        params = [
            cur_task,
            user_mode_name,
        ]
        tf_dir = self.get_task_path(params) + "\\" + TaskLoader.task_files_dir
        task_files = os.listdir(tf_dir)

        if not os.path.exists(TaskLoader.working_dir):
            os.mkdir(TaskLoader.working_dir)

        task_working_dir = TaskLoader.working_dir + "\\" + cur_task
        if not os.path.exists(task_working_dir):
            os.mkdir(task_working_dir)
        else:
            allowed = override_workdir
            result = 0x1 # Warning: Task already started!

        if allowed:
            for task_file in task_files:
                shutil.copy(tf_dir + "\\" + task_file, task_working_dir)

        # maybe make optional (settings?)
        os_spec.open_file_browser(task_working_dir)

        return result


    @Slot(list, result=bool)
    def show_solution(self, params):
        user_mode_name = params[0]
        info_level_name = params[1]

        cur_task = self.get_cur_task()
        paramsx = [
            cur_task,
            user_mode_name,
        ]
        sol_dir = self.get_task_path(paramsx) + "\\" + TaskLoader.solution_dir + "\\"
        sol_dir_fin = sol_dir + info_level_name.capitalize().replace(" ", "_")

        sol_dir_fin = os.path.abspath(sol_dir_fin)
        if not os.path.exists(sol_dir_fin):
            sol_dir_fin = sol_dir + info_level_name.lower()

        sol_dir_fin = os.path.abspath(sol_dir_fin)
        if os.path.exists(sol_dir_fin):
            # print(f"Opening file explorer for {info_level_name} solution...")
            os_spec.open_file_browser(sol_dir_fin)
            return True
        return False




