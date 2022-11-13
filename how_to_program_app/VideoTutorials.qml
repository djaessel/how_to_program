import QtQuick
import QtQuick.Controls
//import SystemCaller

BasePage {
    id: _videoTutorials

    //forceDefaultData: true

    //SystemCaller {
    //    id: systemCaller
    //}

    MouseArea {
        anchors.fill: parent
        onWheel: {
            for (var i = 0; i < videosContainer.children.length; i++) {
                videosContainer.children[i].y += (wheel.angleDelta.y > 0) ? 32 : -32
            }
        }
    }

    function createVideoElements(videoData) {
        for (var i = 0; i < videoData.length; i++) {
            var component = Qt.createComponent("VideoTutorialThumbnail.qml");
            var sprite = component.createObject(videosContainer, {});

            if (sprite == null) {
                // Error Handling
                console.log("Error creating object");
            } else {
                sprite.init(videoData[i], i, videosContainer)
            }
        }
    }

    Component.onCompleted: {
        var videoData = videoLoader.loadAllBaseOnUserMode(userModeName.toLowerCase())
        createVideoElements(videoData)
    }

    Rectangle {
        id: progressContainer

        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right

        height: 128

        property int watchedVideos: 2
        property int allVideoCount: 10

        Text {
            id: progressInfoLabel

            anchors.left: parent.left
            anchors.top: parent.top

            anchors.margins: 32

            height: 32

            font.pointSize: 24

            text: "<i><b>" + qsTr("Current Progress") +
                  " ( " + progressContainer.watchedVideos + " / " + progressContainer.allVideoCount + " )</b></i>" +
                  " <i>" + parseInt(progressBar.value * 100) + " %</i>"
        }

        ProgressBar {
            id: progressBar

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom

            anchors.margins: 32

            height: 24

            value: (progressContainer.watchedVideos / progressContainer.allVideoCount)
        }
    }

    LineSplitter {
        id: splitLine1

        anchors.top: progressContainer.bottom
    }

    Rectangle {
        id: videosContainer

        anchors.top: splitLine1.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom

//        VideoTutorialThumbnail {
//            id: vidTut1
//        }

//        VideoTutorialThumbnail {
//            id: vidTut2
//        }

    }
}
