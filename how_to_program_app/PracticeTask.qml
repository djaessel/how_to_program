import QtQuick
import QtQuick.Controls

SpecialPage {
    id: _practiceTaskPage

    windowTitle: titleText

    property var missi: parent

    function checkIsDone() {
        if (standardButtons.isDone
         && bonusButtons.isDone
         && extraBonusButtons.isDone) {
            taskDone = true
        }
    }

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

            TaskButtonRow {
                id: standardButtons

                anchors.left: parent.left
                anchors.right: parent.right

                y: _pageConent.contentY

                height: missi.height * 0.15

                visible: true
                programmingEnabled: true

                infoLevelUsed: 0
                infoLevelText: "Standard"

                onIsDoneChanged: {
                    if (standardButtons.isDone && appWindow.infoLevel > 0) {
                        bonusButtons.visible = true
                    }
                    _practiceTaskPage.checkIsDone()
                }
            }

            TaskButtonRow {
                id: bonusButtons

                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: standardButtons.bottom

                height: missi.height * 0.15

                infoLevelUsed: 1
                infoLevelText: "Bonus"

                onVisibleChanged: {
                    if (bonusButtons.visible) {
                        bonusButtons.programmingEnabled = standardButtons.isDone
                    }
                }

                onIsDoneChanged: {
                    if (bonusButtons.isDone && appWindow.infoLevel > 1) {
                        extraBonusButtons.visible = true
                    }
                    _practiceTaskPage.checkIsDone()
                }
            }

            TaskButtonRow {
                id: extraBonusButtons

                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: bonusButtons.bottom

                height: missi.height * 0.15

                infoLevelUsed: 2
                infoLevelText: "Extra Bonus"

                onVisibleChanged: {
                    if (extraBonusButtons.visible) {
                        extraBonusButtons.programmingEnabled = bonusButtons.isDone
                    }
                }

                onIsDoneChanged: {
                    _practiceTaskPage.checkIsDone()
                }
            }

            Label {
                id: finishedMessage

                visible: taskDone || taskStarted

                anchors.top: {
                    if (extraBonusButtons.visible && bonusButtons.isDone) return extraBonusButtons.bottom
                    if (bonusButtons.visible && standardButtons.isDone) return bonusButtons.bottom
                    if (standardButtons.visible && standardButtons.programmingEnabled) return standardButtons.bottom
                    return parent.top
                }
                anchors.left: buttonRect.left
                anchors.right: buttonRect.right

                anchors.margins: 16
                anchors.leftMargin: buttonRect.width * 0.25

                height: missi.height * 0.15

                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter

                fontSizeMode: Text.Fit

                font.pointSize: 32
                font.bold: true

                text: (taskDone) ? "\u2713  TASK COMPLETE" : "\uf0ad  TASK IN PROGRESS"
                color: "#9a9"
            }
        }
    }
}
