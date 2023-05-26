import QtQuick 2.15
import QtQuick.Controls 2.15
//import SystemCaller

ProgressPage {
    id: _videoTutorials

    //SystemCaller {
    //    id: systemCaller
    //}

    property var modelx: []

    onModelxChanged: {
        updateProgressData()
    }

    function createVideoElements(videoData) {
        var model = []
        for (var i = 0; i < videoData.length; i+=2) {
            if (i < videoData.length - 1) {
                model.push([videoData[i], videoData[i + 1]])
            } else {
                model.push([videoData[i]])
            }
        }

        _videoTutorials.modelx = model
        videosContainer.model = _videoTutorials.modelx

        _videoTutorials.allCount = videoData.length

        updateProgressData()
    }

    function init() {
        var videoDataOLD = videoLoader.loadAllBasedOnUserMode(userModeName.toLowerCase())
        var videoData = videoLoader.loadPlaylistBasedOnUserMode(userModeName.toLowerCase())

        for (var i = 0; i < videoDataOLD.length; i++) {
            var found = false
            for (var j = 0; j < videoData.length; j++) {
                if (videoData[j]["videoId"] === videoDataOLD[i]["videoId"]) {
                    videoData[j]["infoText"] = videoDataOLD[i]["infoText"]
                    found = true
                    j = videoData.length // break
                }
            }

            if (!found) {
                console.log(JSON.stringify(videoDataOLD[i]))
                //videoData.push(videoDataOLD[i])
            }
        }

        createVideoElements(videoData)
    }

    function updateProgressData() {
        var count = 0

        // FIXME: optimize code
        var ally = JSON.parse(settingsManager.allVideoSaveData())
        for (var i=0; i < ally.length; i++) {
            var found = false
            for (var j=0; j < videosContainer.model.length; j++) {
                for (var k=0; k < videosContainer.model[j].length; k++) {
                    if (videosContainer.model[j][k].videoId === ally[i].videoId) {
                        found = true
                    }
                }
            }

            if (ally[i].finished && found) {
                count += 1
            }
        }

        _videoTutorials.doneCount = count
    }


    ListView {
        id: videosContainer

        anchors.top: progressTopSplit.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom

        clip: false

        model: []

        delegate: Rectangle {
            id: rowy

            width: videosContainer.width
            height: videosContainer.height * 0.3

            VideoTutorialThumbnail {
                id: col1

                anchors.left: rowy.left
                anchors.top: rowy.top
                anchors.bottom: rowy.bottom

                width: rowy.width * 0.5

                Component.onCompleted: {
                    col1.init(_videoTutorials.modelx[index][0])
                }
            }

            VideoTutorialThumbnail {
                id: col2

                anchors.right: rowy.right
                anchors.top: rowy.top
                anchors.bottom: rowy.bottom

                width: rowy.width * 0.5

                Component.onCompleted: {
                    if (_videoTutorials.modelx[index].length > 1) {
                        col2.init(_videoTutorials.modelx[index][1])
                    } else {
                        col2.visible = false
                    }
                }
            }
        }

    }
}
