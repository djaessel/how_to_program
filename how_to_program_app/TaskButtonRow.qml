import QtQuick
import QtQuick.Controls


Row {
    id: _buttons

    anchors.left: parent.left
    anchors.right: parent.right

    anchors.topMargin: 32

    property int infoLevelUsed: -1
    property string infoLevelText: "Test"

    property bool programmingEnabled: false
    property bool solutionEnabled: false
    property bool finishedEnabled: false
    property bool isDone: false

    visible: false
    enabled: programmingEnabled

    Dialog {
        id: popupMessage
        modal: true
        standardButtons: Dialog.Ok
    }

    Component.onCompleted: {
        // on start if no data given always 1
        if (programmingEnabled && infoLevelProgress[infoLevelUsed] <= 0) {
            infoLevelProgress[infoLevelUsed] = 1
        }

        _buttons.programmingEnabled = (infoLevelProgress[infoLevelUsed] >= 1) || programmingEnabled
        _buttons.solutionEnabled = (infoLevelProgress[infoLevelUsed] >= 2)
        _buttons.finishedEnabled = (infoLevelProgress[infoLevelUsed] >= 3)
        _buttons.isDone = (infoLevelProgress[infoLevelUsed] >= 4)
    }

    onProgrammingEnabledChanged: {
        // on start if no data given always 1
        if (programmingEnabled && infoLevelProgress[infoLevelUsed] <= 0) {
            infoLevelProgress[infoLevelUsed] = 1
        }
        updateTaskSaveData()
    }
    onSolutionEnabledChanged: updateTaskSaveData()
    onFinishedEnabledChanged: updateTaskSaveData()
    onIsDoneChanged: updateTaskSaveData()


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
            infoLevelProgress[infoLevelUsed] = 3
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
//            popupMessage.visible = true
        }

        infoLevelProgress[infoLevelUsed] = 2
        taskStarted = true
        _buttons.solutionEnabled = true
    }

    function finish() {
        infoLevelProgress[infoLevelUsed] = 4

        _buttons.isDone = true
    }

    Label {
        id: standardLabel

        anchors.left: parent.left
        anchors.top: parent.top
        anchors.margins: 32

        visible: programmingEnabled

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

        visible: programmingEnabled

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

        visible: solutionEnabled

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

        visible: finishedEnabled && !isDone

        height: parent.height

        textItem.font.pointSize: 18

        textItem.text: "Finished"

        mouseItem.onClicked: _buttons.finish()
    }

    Label {
        id: infoFinishedMessage

        anchors.left: standardSolutionButton.right
        anchors.right: parent.right
        anchors.top: parent.top

        anchors.margins: 32

        height: parent.height

        visible: isDone

        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter

        font.pointSize: 64
        font.bold: true

        text: "\u2713"
        color: "#9a9"
    }
}
