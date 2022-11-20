# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QmlElement

import os
from constants import WORKING_DIR


QML_IMPORT_NAME = "SettingsManager"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0 # Optional

@QmlElement
class SettingsManager(QObject):
    save_file = WORKING_DIR + "/.settings"

    def __init__(self, parent=None):
        super(SettingsManager, self).__init__(parent)
        self._stored_user_mode = 0
        self._stored_info_level = 0

    @Slot(result=int)
    def get_user_mode(self):
        return self._stored_user_mode

    @Slot(result=int)
    def get_info_level(self):
        return self._stored_info_level

    @Slot(result=list)
    def read_saved_data(self):
        settings_data = []
        if os.path.exists(SettingsManager.save_file):
            with open(SettingsManager.save_file, "rb") as f:
                bdata = f.read()
                modes = int.from_bytes(bdata, "big")
                settings_data.append(modes)
        else:
            settings_data.append(0x00)

        self._stored_user_mode = (settings_data[0] >> 4) & 0x0F
        self._stored_info_level = settings_data[0] & 0x0F

        return settings_data

    @Slot(list)
    def save_data(self, data):
        with open(SettingsManager.save_file, "wb") as f:
            run_mode = data[0] & 0xFF
            self._stored_user_mode = (run_mode >> 4) & 0x0F
            self._stored_info_level = run_mode & 0x0F
            run_mode_bdata = run_mode.to_bytes(1, "big")
            f.write(run_mode_bdata)


