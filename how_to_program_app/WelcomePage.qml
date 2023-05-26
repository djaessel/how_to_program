import QtQuick 2.15
import QtQuick.Controls 2.15

BasePage {
    id: _welcomePage

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

        text: "<u><b>Welcome Programmer!</b></u>"
        font.pointSize: 32
    }

    Label {
        id: userModeInfo

        anchors {
            top: welcomeMessage.bottom
            left: parent.left
            right: parent.right
        }

        text: "<i>You are currently <b>" + userModeName + "</b></i>"
        font.letterSpacing: 4
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        padding: 16
        leftPadding: 32
        topPadding: -16
        font.family: "Tahoma"
        font.pointSize: 24
    }

    Label {
        id: infoLevelInfo

        anchors {
            top: userModeInfo.bottom
            left: parent.left
            right: parent.right
        }

        text: "<i>Your current information level is <b>" + infoLevelName + "</b></i>"
        font.letterSpacing: 4
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        padding: 16
        leftPadding: 32
        topPadding: -16
        font.family: "Tahoma"
        font.pointSize: 24
    }
}
