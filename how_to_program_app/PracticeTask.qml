import QtQuick

SpecialPage {
    id: _practiceTaskPage

    windowTitle: titleText

    property var missi: parent

    Flickable {
        id: _pageConent

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.top: pageTitleSplit.bottom

        contentHeight: Math.max(taskDesc.height, missi.height - windowTitleHeight)

        Rectangle {
            id: contentRect

            anchors.left: parent.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom

            width: parent.width * 0.5

            Text {
                id: taskDesc

                anchors.top: parent.top
                anchors.left: parent.left
                anchors.right: parent.right

                anchors.margins: 32
                anchors.rightMargin: 16

                font.pointSize: 15

                text: descriptionText
            }
        }

        Rectangle {
            id: buttonRect

            anchors.left: contentRect.right
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom

            Row {
                id: standardButtons

                anchors.left: parent.left
                anchors.right: parent.right
                //anchors.top: parent.top

                y: _pageConent.contentY

                height: missi.height * 0.15

                MenuButton {
                    id: standardStartButton

                    anchors.left: parent.left
                    anchors.top: parent.top

                    anchors.margins: 32

                    enabled: true

                    height: parent.height
                    width: parent.width * 0.45

                    textItem.font.pointSize: 18

                    textItem.text: "Programming Standard"
                }

                MenuButton {
                    id: standardSolutionButton

                    anchors.left: standardStartButton.right
                    anchors.right: parent.right
                    anchors.top: parent.top

                    anchors.margins: 32

                    enabled: false

                    height: parent.height

                    textItem.font.pointSize: 18

                    textItem.text: "Standard Solution"
                }
            }

            Row {
                id: bonusButtons

                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: standardButtons.bottom

                height: missi.height * 0.15

                MenuButton {
                    id: bonusStartButton

                    anchors.left: parent.left
                    anchors.top: parent.top

                    anchors.margins: 32

                    enabled: false

                    height: parent.height
                    width: parent.width * 0.45

                    textItem.font.pointSize: 18

                    textItem.text: "Programming Bonus"
                }

                MenuButton {
                    id: bonusSolutionButton

                    anchors.left: bonusStartButton.right
                    anchors.right: parent.right
                    anchors.top: parent.top

                    anchors.margins: 32

                    enabled: false

                    height: parent.height

                    textItem.font.pointSize: 18

                    textItem.text: "Bonus Solution"
                }
            }

            Row {
                id: extraBonusButtons

                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: bonusButtons.bottom

                height: missi.height * 0.15

                MenuButton {
                    id: extraBonusStartButton

                    anchors.left: parent.left
                    anchors.top: parent.top

                    anchors.margins: 32

                    enabled: false

                    height: parent.height
                    width: parent.width * 0.45

                    textItem.font.pointSize: 18

                    textItem.text: "Programming Extra Bonus"
                }

                MenuButton {
                    id: extraBonusSolutionButton

                    anchors.left: extraBonusStartButton.right
                    anchors.right: parent.right
                    anchors.top: parent.top

                    anchors.margins: 32

                    enabled: false

                    height: parent.height

                    textItem.font.pointSize: 18

                    textItem.text: "Extra Bonus Solution"
                }
            }
        }
    }
}
