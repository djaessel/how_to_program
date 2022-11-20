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

    Dialog {
        id: popupMessage
        modal: true
        standardButtons: Dialog.Ok
    }

    function showSolution() {
        var params = [
            userModeName.toLowerCase(),
            infoLevelText.toLowerCase().replace(" ", "_")
        ]

        var success = taskLoader.show_solution(params)
        if (!success) {
            popupMessage.title = qsTr("Error: Solution is not available!")
            popupMessage.visible = true
        } else {
            _buttons.finishedEnabled = true
        }
    }

    function startProgramming() {
        var params1 = [
            userModeName.toLowerCase(),
            false // do not override for now
        ]

        var result = taskLoader.prepare_working_dir(params1)
        if ((result & 0x1) == 0x1) {
            popupMessage.title = qsTr("Warning: Task already started!")
            popupMessage.visible = true
        }

        _buttons.solutionEnabled = true
    }

    function finish() {
        _buttons.isDone = true
    }

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

        mouseItem.onClicked: _buttons.startProgramming()
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

        mouseItem.onClicked: _buttons.showSolution()
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

        mouseItem.onClicked: _buttons.finish()
    }
}
