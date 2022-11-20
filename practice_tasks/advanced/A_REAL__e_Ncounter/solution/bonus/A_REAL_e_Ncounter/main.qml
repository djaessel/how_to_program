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

            model: button_data_py
            spacing: spacingAndMargin

            delegate: AutoClickerButton {
                id: curAutoClickerButton

                showText: button_auto_clicker_data_py[index]["myText"]
                pointsToEnable: button_data_py[index]["pointsToEnable"]
                pointsToEnableFactor: button_auto_clicker_data_py[index]["pointsToEnableFactor"]
                pointsPerClick: button_data_py[index]["pointsPerClick"]
                autoClickDuration: button_auto_clicker_data_py[index]["duration"]
            }
        }

    }

}
