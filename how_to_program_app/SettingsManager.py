# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, Slot, Property
from PySide6.QtQml import QmlElement

import os
from constants import WORKING_DIR


QML_IMPORT_NAME = "SettingsManager"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0 # Optional

@QmlElement
class SettingsManager(QObject):
    save_file = WORKING_DIR + "/.settings_gui"

    def __init__(self, parent=None):
        super(SettingsManager, self).__init__(parent)
        self._stored_user_mode = 0
        self._stored_info_level = 0
        self._stored_watched_videos = []
        self._stored_done_videos = []
        self._stored_watched_tasks = []
        self._stored_done_tasks = []

    @Slot(result=int)
    def get_user_mode(self):
        return self._stored_user_mode

    @Slot(result=int)
    def get_info_level(self):
        return self._stored_info_level

    @Property(list)
    def stored_watched_videos(self):
        return self._stored_watched_videos

    @Property(list)
    def stored_done_videos(self):
        return self._stored_done_videos

    @Property(list)
    def stored_watched_tasks(self):
        return self._stored_watched_tasks

    @Property(list)
    def stored_done_tasks(self):
        return self._stored_done_tasks

    @Slot(result=list)
    def read_saved_data(self):
        settings_data = []
        video_info = []
        task_info = []

        if os.path.exists(SettingsManager.save_file):
            with open(SettingsManager.save_file, "r") as f:
                bdata = f.readline().rstrip("\n")
                modes = int(bdata)
                settings_data.append(modes)

                line = f.readline().rstrip("\n")
                if line == "videos:":
                    line = f.readline().rstrip("\n")
                    while not line == "end":
                        video_info.append(line.split(";"))
                        line = f.readline().rstrip("\n")

                line = f.readline().rstrip("\n")
                if line == "tasks:":
                    line = f.readline().rstrip("\n")
                    while not line == "end":
                        task_info.append(line.split(";"))
                        line = f.readline().rstrip("\n")
        else:
            settings_data.append(0x00)

        self._stored_user_mode = (settings_data[0] >> 4) & 0x0F
        self._stored_info_level = settings_data[0] & 0x0F

        return settings_data

    @Slot(list)
    def save_data(self, data):
        with open(SettingsManager.save_file, "w") as f:
            run_mode = data[0] & 0xFF
            self._stored_user_mode = (run_mode >> 4) & 0x0F
            self._stored_info_level = run_mode & 0x0F
            f.write(str(run_mode) + "\n")

            f.write("video:\n")
            # TODO: write video data
            f.write("end")

            f.write("tasks:\n")
            # TODO: write tasks here
            f.write("end")


