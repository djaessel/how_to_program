import QtQuick
import QtQuick.Window
import QtQuick.Controls 2.15

Window {
    width: 1024
    height: 800
    visible: true
    title: qsTr("e Ncounter")

    x: Screen.width / 2 - width / 2
    y: Screen.height / 2 - height / 2

    Rectangle {
        id: clickerBox
        color: "#234"

        property int curPoints: 0

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
            id: myListView

            property int spacingAndMargin: 12

            anchors.top: pointsLabel.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom

            anchors.topMargin: 32
            anchors.leftMargin: spacingAndMargin
            anchors.rightMargin: spacingAndMargin
            anchors.bottomMargin: spacingAndMargin

            model: button_data_py
            spacing: spacingAndMargin

            delegate: Button {
                id: curButton

                property bool activated: false

                enabled: (button_data_py[index]["pointsToEnable"] <= clickerBox.curPoints || curButton.activated)

                onEnabledChanged: {
                    if (enabled) {
                        curButton.activated = true
                    }
                }

                anchors {
                    left: parent.left
                    right: parent.right
                }

                height: 128

                onClicked: {
                    clickerBox.curPoints += button_data_py[index]["pointsPerClick"]
                }

                contentItem: Text {
                    text: button_data_py[index]["myText"]
                    font.pointSize: 28
                    color: curButton.enabled ? (curButton.down ? "#aabbaa" : "white") : "#gray"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }

                background: Rectangle {
                    border.color: curButton.down ? "#88cc88" : "##223322"
                    border.width: 8
                    color: curButton.down ? "#244" : "#577"
                    radius: parent.width * 0.25
                }
            }
        }

    }

}
