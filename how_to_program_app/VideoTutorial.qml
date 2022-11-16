import QtQuick
import QtQuick.Controls

ScrollView {
    id: _vidTutorial

    width: 400
    height: 300

    clip: true

    Rectangle {
        id: progressContainer

        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right

        height: 80

        property int watchedVideos: 2
        property int allVideoCount: 10

        MenuButton {
            id: backToTuts

            anchors.top: parent.top
            anchors.left: parent.left
            anchors.bottom: parent.bottom

            text: "\u276E"
            width: titleBar.height

            textItem.font.pointSize: 18

            mouseItem.onClicked: {
                stackView.pop()
            }
        }

        Label {
            id: videoTitleLabel

            anchors.left: backToTuts.right
            anchors.top: parent.top
            anchors.right: parent.right

            anchors.leftMargin: resizer * 32
            anchors.topMargin: resizer * 8

            height: resizer * 56

            font.pointSize: resizer * 32

            verticalAlignment: Text.AlignVCenter

            text: "<b>" + videoTitle + "</b>"
        }

        Label {
            id: videoTimeLabel

            anchors.left: videoTitleLabel.left
            anchors.top: videoTitleLabel.bottom
            anchors.right: parent.right

            //anchors.leftMargin: resizer * 32

            height: resizer * 32

            font.pointSize: resizer * 18

            verticalAlignment: Text.AlignVCenter

            text: "Duration: " + ((videoDurationHours > 0) ? videoDurationHours + ":" : "") + videoDurationMinutes + ":" + videoDurationSeconds
        }
    }

    LineSplitter {
        id: splitLine1

        anchors.top: progressContainer.bottom
    }

    Image {
        id: videoThumbnail

        anchors.left: parent.left
        anchors.top: splitLine1.bottom

        anchors.margins: resizer * 32

        width: parent.width * 0.33

        smooth: true
        fillMode: Image.PreserveAspectFit

        source: thumbnailUrl

        cache: true
        asynchronous: true

        onStatusChanged: {
           if (status == Image.Error) {
              source = alternativeThumbnailUrl
              // maybe later more will be added
           }
           // some are stuck in Image.Loading ???
        }

        MouseArea {
            anchors.fill: parent
            hoverEnabled: true

            onEntered: {
                videoThumbnail.opacity = 0.6789
            }

            onExited: {
                videoThumbnail.opacity = 1
            }

            onClicked: {
                systemCaller.openUrl(defaultVideoUrl)
            }
        }

        Label {
            z: 10
            anchors.fill: parent

            text: "\u25B6"

            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter

            font.pointSize: 64
            color: "#444"
        }
    }

    Label {
        id: videoInfoText

        anchors.left: videoThumbnail.right
        anchors.top: videoThumbnail.top
        anchors.right: parent.right
        anchors.bottom: parent.bottom

        anchors.margins: resizer * 32
        anchors.topMargin: 0

        wrapMode: Text.WordWrap
        elide: Text.ElideRight

        font.pointSize: 16

        text: videoInfo
    }
}
