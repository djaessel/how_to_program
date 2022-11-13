import QtQuick
import QtQuick.Controls

Rectangle {
    id: _videoTutorialThumbnailItem

    property double resizer: 1.0

    property string curYoutubeVideoId: "wKqLaNqxgas"
    property string defaultVideoUrl: "https://www.youtube.com/watch?v=" + curYoutubeVideoId + "?t=" + videoStartTime
    property string thumbnailUrl: "https://img.youtube.com/vi/" + curYoutubeVideoId + "/maxresdefault.jpg"

    property string videoTitle: "Creating user interfaces with Qt for Python {On-demand webinar}"

    property int videoStartTime: 0
    property int videoDurationAllSeconds: 3460 - videoStartTime
    property int videoDurationSeconds: videoDurationAllSeconds % 60
    property int videoDurationMinutes: parseInt(videoDurationAllSeconds / 60)
    property int videoDurationHours: parseInt(videoDurationMinutes / 60)

    color: "#ded"

    MouseArea {
        anchors.fill: parent
        onClicked: {
            systemCaller.openUrl(defaultVideoUrl)
        }
    }

    Label {
        id: videoTitleLabel

        anchors.left: parent.left
        anchors.top: parent.top
        anchors.right: parent.right

        anchors.leftMargin: resizer * 32
        anchors.topMargin: resizer * 8

        height: resizer * 48

        font.pointSize: resizer * 24

        verticalAlignment: Text.AlignVCenter

        text: videoTitle
    }

    Label {
        id: videoTimeLabel

        anchors.left: parent.left
        anchors.top: videoTitleLabel.bottom
        anchors.right: parent.right

        anchors.leftMargin: resizer * 32

        height: resizer * 32

        font.pointSize: resizer * 18

        verticalAlignment: Text.AlignVCenter

        text: "Duration: " + ((videoDurationHours > 0) ? videoDurationHours + ":" : "") + videoDurationMinutes + ":" + videoDurationSeconds
    }

    Image {
        id: videoThumbnail

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.top: videoTimeLabel.bottom

        anchors.margins: resizer * 32
        anchors.topMargin: resizer * 8

        source: thumbnailUrl
    }
}
