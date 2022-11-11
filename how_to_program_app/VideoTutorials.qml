import QtQuick
import QtQuick.Controls

Page {
    id: _videoTutorials

    anchors.fill: parent

    property string curYoutubeVideoId: "wKqLaNqxgas"
    property string defaultVideoUrl: "https://www.youtube.com/watch?v=vidID"

    Image {
        id: videoThumbnail

        anchors.fill: parent

        source: "https://img.youtube.com/vi/" + curYoutubeVideoId + "/maxresdefault.jpg"

        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("Open browser with: " + defaultVideoUrl.replace("vidID", curYoutubeVideoId))
            }
        }
    }
}
