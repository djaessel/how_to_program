# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QmlElement

import os
import sys
import subprocess
import importlib


QML_IMPORT_NAME = "VideoLoader"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0 # Optional

@QmlElement
class VideoLoader(QObject):
    def __init__(self, parent=None):
        super(VideoLoader, self).__init__(parent)
        self.checkInstallYoutubeDL()

    @Slot(str, result=list)
    def loadAllBaseOnUserMode(self, dir):
        videoData = []
        path = "../video_tutorials/" + dir + "/"
        videoFiles = []
        files = os.listdir(path)
        for file in files:
            file_path = path + file
            if os.path.isfile(file_path):
                videoFiles.append(file_path)

        for vidFile in videoFiles:
            data = self.loadVideoData(vidFile)
            if data != -1:
                videoData.append(data)
        videoData.sort(key=self.orderVideo)
        return videoData


    def checkInstallYoutubeDL(self):
#        spec = importlib.util.find_spec("youtube_dl")
#        found = spec is not None
#        print("Check Youtube-DL:", found, spec)
#        if not found:
#            args = [sys.executable, "-m", "pip", "install", "youtube-dl"]
#            p = subprocess.run(args, check=True, capture_output=True)
#            return len(p.stdout.decode()) > 0
#        return True
        return False


    def orderVideo(self, element):
        return element["orderCode"]


    def extractDuration(self, url):
        # youtube-dl --flat-playlist --get-duration # --get-id
        # youtube-dl --get-duration
        args = ["youtube-dl", "--get-duration", url]
        p = subprocess.run(args, check=True, capture_output=True)
        return p.stdout.decode().strip("\n").strip(" ")

    def loadVideoData(self, file_path):
        url = ""
        dependencies = []
        infoTextLines = []

        #filePathData = file_path.split("___")
        #orderCode = filePathData[0].replace("_", ".")
        #videoTitle = filePathData[1]

        videoTitle = file_path.replace("\\", "/").split("/")[-1]
        ll = videoTitle.split("_")

        orderCode = ""
        nameStartIndex = 0
        for l in ll:
            if l.isdigit():
                orderCode += l + "."
                nameStartIndex += len(l) + 1
            else:
                break
        orderCode.rstrip(".")
        videoTitle = videoTitle[nameStartIndex:].split(".")[0]
        videoTitle = videoTitle.replace("_", " ")
        duration = "00:00"

        with open(file_path) as vf:
            dataLen = 1
            emptyStartLine = True
            foundVideoLink = False
            while dataLen > 0:
                line = vf.readline()
                dataLen = len(line)
                if dataLen > 0:
                    line_l = line.lower()
                    if line_l.startswith("video:") or line_l.startswith("link:"):
                        if line_l.startswith("video:"):
                            foundVideoLink = True
                            url = ":".join(line.split(":")[1:]).rstrip('\n').strip()
                            duration = self.extractDuration(url)
                    else:
                        line = line.rstrip("\n").rstrip()
                        if emptyStartLine and len(line.strip()) > 0:
                            emptyStartLine = False
                        if not emptyStartLine:
                            infoTextLines.append(line)

        vidData = {
            "orderCode": orderCode,
            "title": videoTitle,
            "url": url,
            "duration": duration,
            "dependencies": dependencies,
            "infoText": infoTextLines,
        }

        if not foundVideoLink:
            vidData = -1

        return vidData


