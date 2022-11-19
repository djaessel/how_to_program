import QtQuick

ProgressPage {
    id: _practiceTasks

    property var myModel: []

    onMyModelChanged: {
        tasksList.model = myModel

        allCount = myModel.length
        doneCount = 0 // later actual count based on active and stored
    }

    function init() {
        var newModel = []

        var umnae = userModeName.toLowerCase()
        var count = taskLoader.load_available_tasks(umnae)
        for (var i = 0; i < count; i++) {
            var taskName = taskLoader.get_task(i)
            var taskPath = taskLoader.get_task_path([taskName, umnae])
            var taskInfo = taskLoader.read_task_info([taskPath, infoLevelNames, infoLevel])

            // remove first while empty
            while (taskInfo[0].length === 0) {
                taskInfo.splice(0, 1)
            }

            var listActive = false
            var lastEndedWithBack = false
            for (var j = 0; j < taskInfo.length; j++) {
                var orgLin = taskInfo[j]

                if (taskInfo[j].startsWith(">")) {
                    taskInfo[j] = "<i>" + taskInfo[j].replace(">", "") + "</i>"
                }

                var listObjIndex = taskInfo[j].indexOf("- ")
                if (listObjIndex >= 0 || lastEndedWithBack) {
                    if (!lastEndedWithBack) {
                        var x = ""
                        if (!listActive) {
                            taskInfo[j - 1] = "<b>" + taskInfo[j - 1] + "</b>"
                            x += "<ul style='list-style-position: outside'>"
                        }

                        lastEndedWithBack = orgLin.trim(" ", "\n").endsWith("\\")

                        taskInfo[j] = x + "<li>" + taskInfo[j].replace("- ", " ").split("\\")[0]

                        if (!lastEndedWithBack) {
                            taskInfo[j] += "</li>"
                        }
                    } else {
                        taskInfo[j] = taskInfo[j] + "</li>"
                        lastEndedWithBack = orgLin.trim(" ", "\n").endsWith("\\")
                    }

                    listActive = true
                } else {
                    if (listActive) {
                        taskInfo[j] = "</ul><br>" + taskInfo[j]
                    }

                    lastEndedWithBack = false
                    listActive = false
                }

                taskInfo[j] = taskInfo[j].replace("-->", "\u2192").replace("<--", "\u2190")
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
            title: "Task2"
            description: "Lorem impsum\nMultiline"
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
            descriptionText: _practiceTasks.myModel[index].taskInfo.join("<br>") + "<br><br><br><br><br>"
        }
    }
}
