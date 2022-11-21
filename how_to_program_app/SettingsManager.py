# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QmlElement

import os
import json
from constants import WORKING_DIR


QML_IMPORT_NAME = "SettingsManager"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0 # Optional

@QmlElement
class SettingsManager(QObject):
    save_file = os.path.join(WORKING_DIR, ".settings_gui")

    def __init__(self, parent=None):
        super(SettingsManager, self).__init__(parent)
        self._stored_user_mode = 0
        self._stored_info_level = 0
        self._stored_video_data = []
        self._stored_task_data = []

    @Slot(result=int)
    def get_user_mode(self):
        return self._stored_user_mode

    @Slot(result=int)
    def get_info_level(self):
        return self._stored_info_level

    @Slot(str, result=str)
    def videoSaveData(self, videoId):
        for i, d in enumerate(self._stored_video_data):
            if d["videoId"] == videoId:
                return json.dumps(d)
        return "{}"

    @Slot(result=str)
    def allVideoSaveData(self):
        return json.dumps(self._stored_video_data)

    @Slot(result=str)
    def allTaskSaveData(self):
        return json.dumps(self._stored_task_data)

    @Slot(str, result=str)
    def taskSaveData(self, task_name):
        for i, d in enumerate(self._stored_task_data):
            if d["task_name"] == task_name:
                return json.dumps(d)
        default_d = {
            "task_name": task_name,
            "started": False,
            "finished": False,
            "standard": 0, # 0 no, 1 started, 2 solution, 3 finished
            "bonus": 0, # 0 no, 1 started, 2 solution, 3 finished
            "extra_bonus": 0 # 0 no, 1 started, 2 solution, 3 finished
        }
        return json.dumps(default_d)

    def updateTaskSaveData(self, index, data):
        if 0 <= index < len(self._stored_task_data):
            self._stored_task_data[index] = data
            return True
        return False

    @Slot(str)
    def handleTaskSaveData(self, data):
        a_data = json.loads(data)
        for i, td in enumerate(self._stored_task_data):
            if td["task_name"] == a_data["task_name"]:
                self.updateTaskSaveData(i, a_data)
                return # skip push part
        self._stored_task_data.append(a_data)

    def updateVideoSaveData(self, index, data):
        if 0 <= index < len(self._stored_video_data):
            self._stored_video_data[index] = data
            return True
        return False

    @Slot(str)
    def handleVideoSaveData(self, data):
        a_data = json.loads(data)
        for i, vd in enumerate(self._stored_video_data):
            if vd["videoId"] == a_data["videoId"]:
                self.updateVideoSaveData(i, a_data)
                return # skip push part
        self._stored_video_data.append(a_data)

    def readBlockSettings(self, f, linex, blockId):
        block = []
        if linex.startswith(f'"{blockId}":'):
            data_s = ":".join(linex.split(":")[1:])
            line = f.readline().rstrip("\n")
            while not line.startswith('"'):
                data_s += line
                line = f.readline().rstrip("\n")
            block = json.loads(data_s)
        return block, line

    @Slot(result=list)
    def read_saved_data(self):
        settings_data = []
        video_info = []
        task_info = []

        if os.path.exists(SettingsManager.save_file):
            with open(SettingsManager.save_file, "r", encoding="utf-8") as f:
                lastLine = f.readline().rstrip("\n")
                modes = int(lastLine.split(":")[1].strip())
                if modes >= 0xFF:
                    modes = 0x00
                settings_data.append(modes)

                lastLine = f.readline().rstrip("\n")
                video_info, last_line = self.readBlockSettings(f, lastLine, "videos")
                task_info, lastLine = self.readBlockSettings(f, last_line, "tasks")

        else:
            settings_data.append(0x00)

        self._stored_user_mode = (settings_data[0] >> 4) & 0x0F
        self._stored_info_level = settings_data[0] & 0x0F
        self._stored_video_data = video_info
        self._stored_task_data = task_info

        return settings_data

    @Slot(list)
    def save_data(self, data):
        with open(SettingsManager.save_file, "w", encoding="utf-8") as f:
            run_mode = data[0] & 0xFF
            self._stored_user_mode = (run_mode >> 4) & 0x0F
            self._stored_info_level = run_mode & 0x0F
            f.write('"run_mode": ' + str(run_mode))
            f.write('\n')

            f.write('"videos":')
            video_data = self._stored_video_data
            f.write(",\n".join(json.dumps(video_data).split(",")))
            f.write('\n')

            f.write('"tasks":')
            task_data = self._stored_task_data
            f.write(",\n".join(json.dumps(task_data).split(",")))
            f.write('\n')

            f.write('"end": true') # just for better loading
            # f.write('\n')
