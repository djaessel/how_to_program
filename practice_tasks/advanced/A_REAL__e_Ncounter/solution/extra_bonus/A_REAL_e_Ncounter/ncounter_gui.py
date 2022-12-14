# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from SaveGame import SaveGame

import json


def loadJSONData():
    all_data = dict()
    with open('settings.json') as cbf:
        all_data = json.load(cbf)

    return all_data


if __name__ == "__main__":
    # This is auto-generated by QtCreator
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "main.qml"


    all_data = loadJSONData()
    button_data = all_data["button_data"]
    button_auto_clicker_data = all_data["button_auto_clicker_data"]
    achievements = all_data["achievements"]

    context = engine.rootContext()
    context.setContextProperty("button_data_py", button_data)
    context.setContextProperty("button_auto_clicker_data_py", button_auto_clicker_data)
    context.setContextProperty("achievements_py", achievements)

    saveGame = SaveGame()
    saveGame.load(ac_button_count=len(button_auto_clicker_data))
    context.setContextProperty("saveGame", saveGame)

    # This is auto-generated by QtCreator
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
