import QtQuick
import QtQuick.Controls

Rectangle {
    id: _practice_task_list_item

    property alias titleText: taskTitle.text
    property alias descriptionText: taskShortDescription.text
    property string path: ""

    property bool taskStarted: false
    property bool taskDone: false

    property var infoLevelProgress: {
        var l = []
        for (var i = 0; i < infoLevelNames.length; i++) {
            l.push(0)
        }
        return l
    }

    signal clicked

    onClicked: {
        taskLoader.select_path(index)
    }

    anchors.margins: 16

    color: "#aba"
    border.width: 1
    border.color: "gray"


    onTaskStartedChanged: updateTaskSaveData()
    onTaskDoneChanged: updateTaskSaveData()


    function updateTaskSaveData() {
        var curName = taskLoader.get_cur_task(false)
        if (curName !== "") {
            settingsManager.handleTaskSaveData(JSON.stringify({
                "task_name": curName,
                "started": taskStarted,
                "finished": taskDone,
                "standard": infoLevelProgress[0], // 0 no, 1 started, 2 solution, 3 finished
                "bonus": infoLevelProgress[1], // 0 no, 1 started, 2 solution, 3 finished
                "extra_bonus": infoLevelProgress[2] // 0 no, 1 started, 2 solution, 3 finished
            }))
        }
    }


    PracticeTask {
        id: taskView
        anchors.fill: parent
        visible: false
    }

    MouseArea {
        anchors.fill: parent

        hoverEnabled: true
//        pressAndHoldInterval: 5

//        onPressAndHold: {
//            _practice_task_list_item.color = "#676"
//        }

//        onReleased: {
//            _practice_task_list_item.color = "#aba"
//        }

        onEntered: {
            _practice_task_list_item.color = "#898"
        }

        onExited: {
            _practice_task_list_item.color = "#aba"
        }

        onClicked: {
            stackView.push(taskView)
            _practice_task_list_item.clicked()
        }
    }

    Text {
        id: taskTitle

        anchors.top: parent.top
        anchors.left: parent.left
        anchors.bottom: parent.bottom

        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter

        font.pointSize: 24

        width: parent.width * 0.35

        wrapMode: Text.WordWrap
    }

    Text {
        id: taskShortDescription

        anchors.top: parent.top
        anchors.left: taskTitle.right
        anchors.bottom: parent.bottom
        anchors.right: parent.right

        anchors.margins: 8

        font.pointSize: 20

        elide: Text.ElideRight
    }
}
