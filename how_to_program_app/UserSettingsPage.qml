import QtQuick
import QtQuick.Controls

BasePage {
    id: _userSettingsPage

    //forceDefaultData: true

    Label {
        id: userModeLabel

        anchors.left: parent.left
        anchors.top: parent.top

        anchors.margins: 32

        width: parent.width * 0.25

        font.pointSize: 24

        text: "<i>Select User Mode:</i>"
    }

    ComboBox {
        id: selectUserMode

        Component.onCompleted: {
            var curS = ""
            var myModel = []
            for (var i = 0; i < userModeTexts.length; i++) {
                curS = userModeTexts[i].charAt(0).toUpperCase() + userModeTexts[i].substring(1).replace("_", " ")
                myModel.push(curS)
            }
            selectUserMode.model = myModel
        }

        anchors.left: parent.left
        anchors.top: userModeLabel.bottom

        anchors.margins: 32
        anchors.topMargin: 16

        width: parent.width * 0.25
        height: 120

        font.pointSize: 32

        onCurrentTextChanged: {
            userMode = selectUserMode.currentIndex
        }

        contentItem: Text {
            width: parent.width
            height: parent.height

            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter

            font.pointSize: 24
            font.bold: true

            text: userModeName
        }

        background: Rectangle {
            width: parent.width
            height: parent.height

            color:  {
                if (parent.down) {
                    return "#787"
                }

                return parent.hovered ? "#abc" : "#aba"
            }
        }
    }

    Label {
        id: infoLevelLabel

        anchors.left: parent.left
        anchors.top: selectUserMode.bottom

        anchors.margins: 32
        anchors.topMargin: 64

        width: parent.width * 0.25

        font.pointSize: 24

        text: "<i>Select Info Level:</i>"
    }

    ComboBox {
        id: selectInfoLevel

        Component.onCompleted: {
            var curS = ""
            var myModel = []
            for (var i = 0; i < infoLevelNames.length; i++) {
                curS = infoLevelNames[i].charAt(0).toUpperCase() + infoLevelNames[i].substring(1).replace("_", " ")
                myModel.push(curS)
            }
            selectInfoLevel.model = myModel
        }

        anchors.left: parent.left
        anchors.top: infoLevelLabel.bottom

        anchors.margins: 32
        anchors.topMargin: 16

        width: parent.width * 0.25
        height: 120

        font.pointSize: 32

        onCurrentTextChanged: {
            infoLevel = selectInfoLevel.currentIndex
        }

        contentItem: Text {
            width: parent.width
            height: parent.height

            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter

            font.pointSize: 24
            font.bold: true

            text: infoLevelName
        }

        background: Rectangle {
            width: parent.width
            height: parent.height

            color:  {
                if (parent.down) {
                    return "#787"
                }

                return parent.hovered ? "#abc" : "#aba"
            }
        }
    }
}
