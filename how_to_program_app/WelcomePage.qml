import QtQuick
import QtQuick.Controls

Page {
    id: _welcomePage

    anchors.fill: parent

    Label {
        id: welcomeMessage

        anchors.left: parent.left
        anchors.top: parent.top
        font.letterSpacing: 2
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        padding: 32
        font.family: "Tahoma"
        anchors.right: parent.right

        text: "Welcome Programmer!"
        font.pointSize: 32
    }

    Label {
        id: userModeInfo

        anchors {
            top: welcomeMessage.bottom
            left: parent.left
            right: parent.right
        }

        text: "You are currently " + userModeTexts[userMode]
        font.letterSpacing: 4
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        padding: 16
        leftPadding: 32
        topPadding: 16
        font.family: "Tahoma"
        font.pointSize: 24
    }
}
