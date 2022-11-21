# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QmlElement

import os
# import sys
import subprocess
# import importlib
from constants import WORKING_DIR


QML_IMPORT_NAME = "VideoLoader"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0 # Optional

@QmlElement
class VideoLoader(QObject):
    vid_tut_dir = WORKING_DIR + "\\..\\video_tutorials\\"
    cache_dir = WORKING_DIR + "\\.cache\\"
    cache_playlists_file = cache_dir + ".cached_playlists"

    def __init__(self, parent=None):
        if not os.path.exists(VideoLoader.cache_dir):
            os.mkdir(VideoLoader.cache_dir)
        super(VideoLoader, self).__init__(parent)
        self.checkInstallYoutubeDL()

    @Slot(str, result=list)
    def loadAllBasedOnUserMode(self, dir):
        videoData = []
        path = VideoLoader.vid_tut_dir + dir + "\\"
        videoFiles = []
        if os.path.exists(path) and os.path.isdir(path):
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


    @Slot(str, result=list)
    def loadPlaylistBasedOnUserMode(self, dir):
        path = VideoLoader.vid_tut_dir + dir + "\\0_1_Playlist.txt"
        return self.loadPlaylist(path)


    def loadPlaylist(self, file_path):
        if not os.path.exists(file_path):
            return []

        playlistUrl = ""
        with open(file_path) as vf:
            dataLen = 1
            foundVideoLink = False
            while dataLen > 0 and not foundVideoLink:
                line = vf.readline()
                dataLen = len(line)
                if dataLen > 0:
                    line_l = line.lower()
                    if line_l.startswith("video:") or line_l.startswith("link:"):
                        if line_l.startswith("video:"):
                            foundVideoLink = True
                            playlistUrl = ":".join(line.split(":")[1:]).rstrip('\n').strip()

        cachedPlaylistData = self.getCachedPlaylistList()
        if not playlistUrl in cachedPlaylistData:
            playlist_data = self.extractVideoDataPlaylist(playlistUrl).split("\n")
            self.storePlaylistData(playlistUrl, playlist_data)

        playlist_data = self.loadExtractedPlaylistData(playlistUrl)

        videoData = []
        for i in range(0, len(playlist_data), 3):
            data = self.loadVideoDataById(i, playlist_data[i], playlist_data[i+1], playlist_data[i+2].rstrip("\\r"))
            if data != -1:
                videoData.append(data)

        return videoData


    def getCachedPlaylistList(self):
        existing_playlists = []
        if os.path.exists(VideoLoader.cache_playlists_file):
            with open(VideoLoader.cache_playlists_file) as f:
                for line in f:
                    existing_playlists.append(line.rstrip("\n"))
        return existing_playlists

    def storePlaylistData(self, playlist_url, playlist_data):
        existing_playlists = self.getCachedPlaylistList()
        file_index = len(existing_playlists)
        existing_playlists.append(playlist_url)

        with open(f"{VideoLoader.cache_dir}.cached_pl_{file_index}", "w") as f:
            for data in playlist_data:
                f.write(data + "\n")

        with open(VideoLoader.cache_playlists_file, "w") as f:
            for p in existing_playlists:
                f.write(p + "\n")


    def loadExtractedPlaylistData(self, playlist_url):
        playlist_data = []
        existing_playlists = self.getCachedPlaylistList()
        if playlist_url in existing_playlists:
            file_index = existing_playlists.index(playlist_url)
            with open(f"{VideoLoader.cache_dir}.cached_pl_{file_index}", "r") as f:
                for line in f:
                    playlist_data.append(line.rstrip("\n"))
        return playlist_data



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


    def extractVideoDataPlaylist(self, url):
        # youtube-dl --flat-playlist --get-duration # --get-id
        # youtube-dl --get-duration
        args = ["youtube-dl", "--get-duration", "--get-id", "--get-title", url]
        p = subprocess.run(args, check=True, capture_output=True)
        return p.stdout.decode().strip("\n").strip(" ")


    def extractDuration(self, url):
        # youtube-dl --flat-playlist --get-duration # --get-id
        # youtube-dl --get-duration
        args = ["youtube-dl", "--get-duration", url]
        p = subprocess.run(args, check=True, capture_output=True)
        return p.stdout.decode().strip("\n").strip(" ")

    def loadVideoDataById(self, index, videoTitle, videoId, videoDuration):
        url = "https://youtu.be/" + videoId
        dependencies = ""
        infoTextLines = ["NO_TEXT_FOUND"]
        foundVideoLink = True
        orderCode = int(index / 3) + 1

        vidData = {
            "orderCode": orderCode,
            "title": videoTitle,
            "url": url,
            "videoId": videoId,
            "duration": videoDuration,
            "dependencies": dependencies,
            "infoText": infoTextLines,
        }

        if not foundVideoLink:
            vidData = -1

        return vidData

    def extractVideoId(self, url):
        videoId = ""
        videoUrlData = []
        if url.find("watch?v=") >= 0:
            videoUrlData = url.split("/")[3].split("=")[1].split("?")
        elif url.find("youtu.be") >= 0:
            videoUrlData = url.split("/")[3].split("?")
        else:
            videoUrlData = [url]

        if videoUrlData[0].find("http") < 0:
            videoId = videoUrlData[0]

        return videoId


    def loadVideoData(self, file_path):
        url = ""
        dependencies = []
        infoTextLines = []

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
        videoId = ""

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
                            videoId = self.extractVideoId(url)
                            # duration = self.extractDuration(url)
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
            "videoId": videoId,
            "duration": duration,
            "dependencies": dependencies,
            "infoText": infoTextLines,
        }

        if not foundVideoLink:
            vidData = -1

        return vidData


