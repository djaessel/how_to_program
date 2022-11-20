# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, Slot, Property
from PySide6.QtQml import QmlElement
import os

QML_IMPORT_NAME = "SaveGame"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0 # Optional

@QmlElement
class SaveGame(QObject):
    save_game_file_location = "save1.save"

    def __init__(self, parent=None):
        super(SaveGame, self).__init__(parent)
        self._points = 0
        self._buttons = list()

    @Property(int)
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        if value >= 0:
            self._points = value
        else:
            self._points = 0

    @Property(list)
    def buttons(self):
        return self._buttons

    @Slot(int, result=bool)
    def getItemData(self, index):
        return self._buttons[index]

    @Slot(str)
    def setItemData(self, data):
        d = data.split(":")
        idx = int(d[0])
        val = d[1].capitalize()
        valBool = eval(val)
        if idx >= len(self._buttons):
            self._buttons.append(valBool)
        else:
            self._buttons[idx] = valBool

    @Slot()
    def load(self, ac_button_count=0):
        if os.path.exists(SaveGame.save_game_file_location):
            if os.path.isfile(SaveGame.save_game_file_location):
                with open(SaveGame.save_game_file_location) as saveFile:
                    line = saveFile.readline().rstrip("\n")
                    self.loadPoints(line)

                    line = saveFile.readline().rstrip("\n")
                    self.loadAutoClickerButtons(line)
        else:
            self._buttons = list()
            for i in range(ac_button_count):
                self.setItemData(str(i) + ":False")

    @Slot()
    def save(self):
        with open(SaveGame.save_game_file_location, "w") as saveFile:
            saveFile.write("Points: " + str(self._points) + "\n")
            saveFile.write("Buttons[")
            for i, b in enumerate(self._buttons):
                val = "False"
                if b:
                    val = "True"
                saveFile.write(str(i) + ":" + val)
                if i < len(self._buttons) - 1:
                    saveFile.write(",")
            saveFile.write("]\n")


    def loadAutoClickerButtons(self, line):
        self._buttons = []
        line_data = line.split("[")[1].rstrip("]").split(",")
        for button_data in line_data:
            data = button_data.split(":")[1].strip()
            self._buttons.append(eval(data))


    def loadPoints(self, line):
        line_data = line.split(":")
        p_text = line_data[1].strip()
        p = int(p_text)
        self._points = p

