import QtQuick
import QtQuick.Controls
//import SystemCaller

ProgressPage {
    id: _videoTutorials

    //forceDefaultData: true

    //SystemCaller {
    //    id: systemCaller
    //}

    doneCount: 0
    allCount: 0

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

        _videoTutorials.allCount = videoData.length
    }

    Component.onCompleted: {
        var videoData = videoLoader.loadAllBaseOnUserMode(userModeName.toLowerCase())
        createVideoElements(videoData)
    }

    Rectangle {
        id: videosContainer

        anchors.top: progressTopSplit.bottom
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
