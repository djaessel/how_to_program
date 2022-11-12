# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QUrl, QObject, Slot
from PySide6.QtGui import QDesktopServices
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "SystemCaller"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0 # Optional

@QmlElement
class SystemCaller(QObject):
    def __init__(self, parent=None):
        super(SystemCaller, self).__init__(parent)

    @Slot(str)
    def openUrl(self, url):
        QDesktopServices.openUrl(QUrl(url))
#        self.urlOpened(url);

#    @Slot(str)
#    def urlOpened(self, url):
#        pass
