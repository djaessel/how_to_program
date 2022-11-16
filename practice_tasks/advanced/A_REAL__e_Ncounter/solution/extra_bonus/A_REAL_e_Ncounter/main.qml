import QtQuick
import QtQuick.Window
import QtQuick.Controls 2.15


ApplicationWindow {
    width: 1024
    height: 800
    visible: true
    title: qsTr("e Ncounter")

    x: Screen.width / 2 - width / 2
    y: Screen.height / 2 - height / 2

    Component.onCompleted: {
        achievementBox.setLastAchievement(saveGame.points)
        clickerBox.curPoints = saveGame.points
    }

    onClosing: {
        saveGame.points = clickerBox.curPoints
        saveGame.save()
    }

    Rectangle {
        id: achievementBox

        property int lastVal: -1

        anchors.right: parent.right
        anchors.top: parent.top

        z: 100

        height: 100
        width: parent.width * 0.25

        visible: false

        function setLastAchievement(val) {
            achievementBox.lastVal = val
        }

        function activateAchievement(index) {
            achievementText.text = achievements_py[index].message
            achievementBox.setLastAchievement(achievements_py[index].value)
            achievementIntervalTimer.restart()
            achievementBox.visible = true
        }

        color: "#abb"

        Text {
            id: unlockedText

            anchors.top: parent.top
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: achievementText.top

            anchors.leftMargin: 12
            anchors.rightMargin: 8
            anchors.topMargin: 8

            verticalAlignment: Text.AlignVCenter

            font.pointSize: 165
            fontSizeMode: Text.Fit

            color: "yellow"

            text: "UNLOCKED"
        }

        Text {
            id: achievementText

            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.right: parent.right

            height: parent.height * 0.55

            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter

            anchors.leftMargin: 8
            anchors.rightMargin: 8

            font.pointSize: 165
            fontSizeMode: Text.Fit

            color: "yellow"
        }

        Timer {
            id: achievementIntervalTimer

            interval: 5000

            onTriggered: {
                achievementBox.visible = false
            }
        }
    }

    Rectangle {
        id: clickerBox
        color: "#234"

        property int curPoints: 0

        onCurPointsChanged: {
            // TODO: optimize checks
            for (var i=0; i < achievements_py.length; i++) {
                if (achievements_py[i].value > achievementBox.lastVal && achievements_py[i].value <= curPoints) {
                    if (i < achievements_py.length - 1) {
                        if (achievements_py[i + 1].value > curPoints) {
                            achievementBox.activateAchievement(i)
                        }
                    } else {
                        achievementBox.activateAchievement(i)
                    }
                }
            }
        }

        anchors {
            left: parent.left
            bottom: parent.bottom
            top: parent.top
        }

        width: parent.width //* 0.5

        Label {
            id: pointsLabel

            text: "You have " + clickerBox.curPoints + " " + ((clickerBox.curPoints == 1) ? "point" : "points")
            font.pointSize: 16
            color: "white"

            //horizontalAlignment: Text.AlignLeft
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            elide: Text.ElideRight

            anchors.top: parent.top
            anchors.left: parent.left
            anchors.right: parent.right

            anchors.topMargin: 32
            anchors.leftMargin: 32
        }

        ListView {
            id: clickerButtonsList

            property int spacingAndMargin: 12

            anchors.top: pointsLabel.bottom
            anchors.left: parent.left
            anchors.bottom: parent.bottom

            width: parent.width * 0.5 - spacingAndMargin * 2

            anchors.topMargin: 32
            anchors.leftMargin: spacingAndMargin
            anchors.rightMargin: spacingAndMargin
            anchors.bottomMargin: spacingAndMargin

            model: button_data_py
            spacing: spacingAndMargin

            delegate: ClickerButton {
                id: curButton

                showText: button_data_py[index]["myText"]
                pointsToEnable: button_data_py[index]["pointsToEnable"]
                pointsPerClick: button_data_py[index]["pointsPerClick"]
            }
        }

        ListView {
            id: autoClickerButtonsList

            property int spacingAndMargin: 12

            anchors.top: pointsLabel.bottom
            anchors.right: parent.right
            anchors.bottom: parent.bottom

            width: parent.width * 0.5 - spacingAndMargin * 2

            anchors.topMargin: 32
            anchors.leftMargin: spacingAndMargin
            anchors.rightMargin: spacingAndMargin
            anchors.bottomMargin: spacingAndMargin

            model: button_auto_clicker_data_py
            spacing: spacingAndMargin

            delegate: AutoClickerButton {
                id: curAutoClickerButton

                onBoughtChanged: {
                    if (saveGame) {
                        saveGame.setItemData(index + ":" + curAutoClickerButton.bought)
                    }
                }

                bought: {
                    if (saveGame) return saveGame.getItemData(index)
                    return false
                }
                showText: button_auto_clicker_data_py[index]["myText"]
                pointsToEnable: button_data_py[index]["pointsToEnable"]
                pointsToEnableFactor: button_auto_clicker_data_py[index]["pointsToEnableFactor"]
                pointsPerClick: button_data_py[index]["pointsPerClick"]
                autoClickDuration: button_auto_clicker_data_py[index]["duration"]
            }
        }

    }

}
