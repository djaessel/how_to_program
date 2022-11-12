import QtQuick
import QtQuick.Controls
//import SystemCaller

BasePage {
    id: _videoTutorials

    property string curYoutubeVideoId: "wKqLaNqxgas"
    property string defaultVideoUrl: "https://www.youtube.com/watch?v=" + curYoutubeVideoId

    //SystemCaller {
    //    id: systemCaller
    //}


    Image {
        id: videoThumbnail

        anchors.fill: parent
        anchors.margins: 32

        source: "https://img.youtube.com/vi/" + curYoutubeVideoId + "/maxresdefault.jpg"

        MouseArea {
            anchors.fill: parent
            onClicked: {
                systemCaller.openUrl(defaultVideoUrl)
            }
        }
    }
}
