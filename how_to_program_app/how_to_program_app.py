# This Python file uses the following encoding: utf-8
# Auto-generated code by QtCreator
import os
import sys
from pathlib import Path

# Auto-generated code by QtCreator
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# from PySide6 import QtQml
from PySide6 import QtCore

from SystemCaller import SystemCaller
from VideoLoader import VideoLoader
from TaskLoader import TaskLoader
from SettingsManager import SettingsManager


# Default message handler to be called to bypass all other warnings.
QT_DEFAULT_MESSAGE_HANDLER = QtCore.qInstallMessageHandler(None)
# a custom message handler to intercept warnings
def customMessageHandler(type, context, msg):
    pass


def main():
    # Set default encoding
    # only works for stdin, stdout and stdere
    # os.environ["PYTHONIOENCODING"] = "utf-8"
    os.environ["PYTHONIOENCODING"] = "latin-1"

    # Auto-generated code by QtCreator
    app = QGuiApplication(sys.argv)

    QtCore.qInstallMessageHandler(customMessageHandler)

    # The following should make SystemCaller available as QmlElement
    # But when instanciated the program crashes for some reason :/
    # QtQml.qmlRegisterType(SystemCaller, "SystemCaller", 1, 0, "SystemCaller")

    # Auto-generated code by QtCreator
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "main.qml"

    # This is the alternative, which works for now
    # But later we might want to add Custom Python QmlElements
    # So we have to make sure that it will work by then!
    context = engine.rootContext()

    systemCaller = SystemCaller()
    context.setContextProperty("systemCaller", systemCaller)

    videoLoader = VideoLoader()
    context.setContextProperty("videoLoader", videoLoader)

    taskLoader = TaskLoader()
    context.setContextProperty("taskLoader", taskLoader)

    settingsManager = SettingsManager()
    context.setContextProperty("settingsManager", settingsManager)

    taskSaveData = []
    context.setContextProperty("taskSaveData", taskSaveData)

    videoSaveData = []
    context.setContextProperty("videoSaveData", videoSaveData)

    # Auto-generated code by QtCreator
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


