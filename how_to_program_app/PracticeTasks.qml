import QtQuick

ProgressPage {
    id: _practiceTasks

    property var myModel: []

    onMyModelChanged: {
        tasksList.model = myModel

        allCount = myModel.length
        doneCount = 0 // later actual count based on active and stored
    }

    Component.onCompleted: {
        var newModel = []

        var umnae = userModeName.toLowerCase()
        var count = taskLoader.load_available_tasks(umnae)
        for (var i = 0; i < count; i++) {
            var taskName = taskLoader.get_task(i)
            var taskPath = taskLoader.get_task_path([taskName, umnae])
            var taskInfo = taskLoader.read_task_info([taskPath, infoLevelNames, infoLevel])

            // remove first while empty
            while (taskInfo[0].length == 0) {
                taskInfo.splice(0, 1)
            }

            newModel.push({
                "taskName": taskName,
                "taskPath": taskPath,
                "taskInfo": taskInfo
            })
        }

        _practiceTasks.myModel = newModel
    }

    ListModel {
        id: testModel

        ListElement {
            title: "Task1"
            description: "Lorem impsum"
        }
        ListElement {
            title: "HOOOOOOO"
            description: "HAAAAAAAAAAAAAEYYYYYYYYYY"
        }
        ListElement {
            title: "Lorem impsum 124324346549646 485jz48h9j984j hj496"
            description: "Master 143245645 434534 \n344345\nTTTTEST"
        }
    }

    ListView {
        id: tasksList

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.top: progressTopSplit.bottom

        model: testModel

        delegate: PracticeTaskListItem {

            width: tasksList.width
            height: tasksList.height * 0.25

            titleText: _practiceTasks.myModel[index].taskName.replace("_", " ")
            path: _practiceTasks.myModel[index].taskPath
            descriptionText: _practiceTasks.myModel[index].taskInfo.join("\n")
        }
    }
}
