import QtQuick
import QtQuick.Controls


Row {
    id: _buttons

    anchors.left: parent.left
    anchors.right: parent.right

    anchors.topMargin: 32

    property string infoLevelText: "Test"

    property bool programmingEnabled: false
    property bool solutionEnabled: false
    property bool finishedEnabled: false
    property bool isDone: false

    Label {
        id: standardLabel

        anchors.left: parent.left
        anchors.top: parent.top
        anchors.margins: 32

        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter

        height: parent.height
        width: parent.width * 0.2
        font.pointSize: 18

        text: _buttons.infoLevelText
    }

    MenuButton {
        id: standardStartButton

        anchors.left: standardLabel.right
        anchors.top: parent.top

        anchors.margins: 32

        enabled: programmingEnabled

        height: parent.height
        width: parent.width * 0.2

        textItem.font.pointSize: 18

        textItem.text: "Programming"

        mouseItem.onClicked: {
            _buttons.solutionEnabled = true
        }
    }

    MenuButton {
        id: standardSolutionButton

        anchors.left: standardStartButton.right
        anchors.top: parent.top

        anchors.margins: 32

        enabled: solutionEnabled

        height: parent.height
        width: parent.width * 0.2

        textItem.font.pointSize: 18

        textItem.text: "Solution"

        mouseItem.onClicked: {
            _buttons.finishedEnabled = true
        }
    }

    MenuButton {
        id: standardDoneButton

        anchors.left: standardSolutionButton.right
        anchors.right: parent.right
        anchors.top: parent.top

        anchors.margins: 32

        enabled: finishedEnabled

        height: parent.height

        textItem.font.pointSize: 18

        textItem.text: "Finished"

        mouseItem.onClicked: {
            _buttons.isDone = true
        }
    }
}
