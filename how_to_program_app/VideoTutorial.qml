import QtQuick
import QtQuick.Controls

SpecialPage {
    id: _vidTutorial

    windowTitle: videoTitle

    property var missi: parent

    Flickable {
        id: _pageConent

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.top: pageTitleSplit.bottom

        contentHeight: Math.max(videoInfoText.height, missi.height - windowTitleHeight)

        Rectangle {
            id: videoRect

            anchors.left: parent.left
            anchors.top: parent.top

            //y: _pageConent.contentY

            width: missi.width * 0.33
            height: videoThumbnail.height + videoTimeLabel.height

            anchors.margins: resizer * 32

            color: "#010"

            MouseArea {
                anchors.fill: parent
                hoverEnabled: true

                onEntered: {
                    videoRect.opacity = 0.6789
                }

                onExited: {
                    videoRect.opacity = 1
                }

                onClicked: {
                    systemCaller.openUrl(defaultVideoUrl)
                    alreadyOpened = true
                }
            }

            property int extraBorderWidth: 4

            Rectangle {
                anchors.fill: videoRect

                anchors.rightMargin: -videoRect.extraBorderWidth
                anchors.leftMargin: -videoRect.extraBorderWidth
                anchors.topMargin: -videoRect.extraBorderWidth
                anchors.bottomMargin: -videoRect.extraBorderWidth

                z: -1

                color: "black"
            }

            Image {
                id: videoThumbnail

                anchors.left: parent.left
                //anchors.top: parent.top
                anchors.right: parent.right
                anchors.bottom: videoTimeLabel.top

                smooth: true
                fillMode: Image.PreserveAspectFit

                source: thumbnailUrl

                cache: true
                asynchronous: true

                property bool loaded: false

                onStatusChanged: {
                    if (status == Image.Error) {
                       source = alternativeThumbnailUrl
                       // maybe later more will be added
                    } else if (status == Image.Loading && !videoThumbnail.loaded) {
                       restarte.restart()
                    } else if (status == Image.Ready) {
                       restarte.stop()
                    }/* else {
                       // some are stuck in Image.Loading ???
                    }*/
                }

                // fix for image loading on start
                Timer {
                    id: restarte

                    interval: 500
                    repeat: false

                    onTriggered: {
                        var orgSource = videoThumbnail.source
                        videoThumbnail.source = ""
                        videoThumbnail.source = orgSource
                        videoThumbnail.loaded = true
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
                id: videoTimeLabel

                anchors.left: parent.left
                anchors.bottom: parent.bottom
                anchors.right: parent.right

                height: resizer * 32

                font.pointSize: resizer * 18

                color: "#ddd"

                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter

                text: "<i>Duration: " + (
                          ((videoDurationHours > 0) ?
                              ((JSON.stringify(videoDurationHours).length == 1) ? "0" : "") + videoDurationHours + ":" : "") +
                          ((JSON.stringify(videoDurationMinutes).length == 1) ? "0" : "") + videoDurationMinutes + ":" +
                          ((JSON.stringify(videoDurationSeconds).length == 1) ? "0" : "") + videoDurationSeconds +
                      "</i>"
                )
            }
        }

        Label {
            id: finishedMessage

            visible: markedAsDone || alreadyOpened

            anchors.top: videoRect.bottom
            anchors.left: videoRect.left
            anchors.right: videoRect.right

            anchors.margins: 16
            anchors.topMargin: 0

            height: missi.height * 0.15

            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignLeft

            font.pointSize: 32
            font.bold: true

            text: (markedAsDone) ? "\u2713  COMPLETED" : "\uf04c  ALREADY OPENED"
            color: "#9a9"
        }

        MenuButton {
            id: markAsDoneButton

            anchors.top: {
                anchors.topMargin = 0
                if (finishedMessage.visible) return finishedMessage.bottom
                if (videoRect.visible) {
                    anchors.topMargin = 16
                    return videoRect.bottom
                }
                return parent.top
            }
            anchors.left: videoRect.left
            anchors.right: videoRect.right

            height: missi.height * 0.15

            visible: !markedAsDone

            text: qsTr("Mark as done")

            mouseItem.onClicked: {
                alreadyOpened = true
                markedAsDone = true
            }
        }

        Label {
            id: videoInfoText

            anchors.left: videoRect.right
            anchors.right: parent.right

            // FIXME: find a better way, maybe with correct anchors
            Component.onCompleted: {
                videoInfoText.y = _pageConent.contentY + resizer * 32
            }

            anchors.margins: resizer * 32

            wrapMode: Text.WordWrap
            elide: Text.ElideRight

            font.pointSize: 16

            text: videoInfo
        }
    }
}
