import QtQuick
import QtQuick.Controls

ScrollView {
    id: _specialPage

    property string windowTitle: ""
    property int resizer: 1

    width: 400
    height: 300

    clip: true

    Rectangle {
        id: titleContainer

        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right

        height: 80

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

            text: "<b>" + windowTitle + "</b>"
        }
    }

    LineSplitter {
        id: splitLine1

        anchors.top: titleContainer.bottom
    }

}
