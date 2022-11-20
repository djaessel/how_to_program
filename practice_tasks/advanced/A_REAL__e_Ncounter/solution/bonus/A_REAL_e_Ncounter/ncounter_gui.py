# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


button_data = [
    {
        "myText": "Click me Real!",
        "pointsToEnable": 0,
        "pointsPerClick": 1,
    },
    {
        "myText": "Click me not?",
        "pointsToEnable": 50,
        "pointsPerClick": 10,
    },
    {
        "myText": "Click me again!",
        "pointsToEnable": 250,
        "pointsPerClick": 50,
    },
]

button_auto_clicker_data = [
    {
        "myText": "Autoclicker 1",
        "pointsToEnableFactor": 5, # if 0 then 1 * 5 = 5
        "duration": 100, # milliseconds
    },
    {
        "myText": "Autoclicker 2",
        "pointsToEnableFactor": 5, # 50 * 5 = 250
        "duration": 1000, # milliseconds
    },
    {
        "myText": "Autoclicker 3",
        "pointsToEnableFactor": 5, # 250 * 5 = 1250
        "duration": 2000, # milliseconds
    },
]


if __name__ == "__main__":
    # This is auto-generated by QtCreator
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "main.qml"


    context = engine.rootContext()
    context.setContextProperty("button_data_py", button_data)
    context.setContextProperty("button_auto_clicker_data_py", button_auto_clicker_data)


    # This is auto-generated by QtCreator
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())