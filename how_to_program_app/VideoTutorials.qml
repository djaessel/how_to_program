import QtQuick
import QtQuick.Controls
//import SystemCaller

BasePage {
    id: _videoTutorials

    forceDefaultData: true

    //SystemCaller {
    //    id: systemCaller
    //}

    VideoTutorialThumbnail {
        id: vidTut1

        anchors.left: parent.left
        anchors.top: parent.top

        //anchors.margins: 32

        resizer: 0.75

        width: parent.width * 0.5
        height: parent.height * 0.5
    }

    VideoTutorialThumbnail {
        id: vidTut2

        anchors.left: vidTut1.right
        anchors.top: parent.top

        //anchors.margins: 32

        resizer: 0.75

        width: parent.width * 0.5
        height: parent.height * 0.5
    }
}
