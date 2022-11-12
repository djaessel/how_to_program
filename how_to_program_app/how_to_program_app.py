# This Python file uses the following encoding: utf-8
# Auto-generated code by QtCreator
import sys
from pathlib import Path

# Auto-generated code by QtCreator
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# from PySide6 import QtQml
from PySide6 import QtCore
from SystemCaller import SystemCaller

# Default message handler to be called to bypass all other warnings.
QT_DEFAULT_MESSAGE_HANDLER = QtCore.qInstallMessageHandler(None)
# a custom message handler to intercept warnings
def customMessageHandler(type, context, msg):
    pass


if __name__ == "__main__":
    # Auto-generated code by QtCreator
    app = QGuiApplication(sys.argv)

    QtCore.qInstallMessageHandler(customMessageHandler)

    # The following should make SystemCaller available as QmlElement
    # But when instanciated the program crashes for some reason :/
    # QtQml.qmlRegisterType(SystemCaller, "SystemCaller", 1, 0, "SystemCaller")

    # Auto-generated code by QtCreator
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "main.qml"
    context = engine.rootContext()

    # This is the alternative, which works for now
    # But later we might want to add Custom Python QmlElements
    # So we have to make sure that it will work by then!
    systemCaller = SystemCaller()
    context.setContextProperty("systemCaller", systemCaller)

    # Auto-generated code by QtCreator
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

