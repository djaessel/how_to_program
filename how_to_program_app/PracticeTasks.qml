import QtQuick

ProgressPage {
    id: _practiceTasks

    property var myModel: []

    onMyModelChanged: {
        tasksList.model = myModel

        allCount = myModel.length

        updateProgressData()
    }

    function init() {
        var newModel = []

        var umName = userModeName.toLowerCase()
        var count = taskLoader.load_available_tasks(umName)
        for (var i = 0; i < count; i++) {
            var taskName = taskLoader.get_task(i)
            var params1 = [taskName, umName]
            var taskPath = taskLoader.get_task_path(params1)
            var params2 = [taskPath, infoLevelNames, infoLevel]
            var taskInfo = taskLoader.read_task_info(params2)

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

            // fix because just calling once does not fully work ???
            var taskDisplayText = taskName
            while (taskDisplayText.indexOf("_") >= 0) {
                taskDisplayText = taskDisplayText.replace("_", " ")
            }

            newModel.push({
                "taskName": taskName,
                "taskDisplayText": taskDisplayText,
                "taskPath": taskPath,
                "taskInfo": taskInfo
            })
        }

        _practiceTasks.myModel = newModel
    }

    function updateProgressData() {
        var count = 0

        // FIXME: optimize later
        for (var i = 0; i < tasksList.children[0].children.length; i++) {
            if (tasksList.children[0].children[i].taskDone) {
                count += 1
            }
        }

        _practiceTasks.doneCount = count
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
            id: curTaskItem

            width: tasksList.width
            height: tasksList.height * 0.25

            Component.onCompleted: {
                var curTaskName = _practiceTasks.myModel[index].taskName
                var curSaveDataString = settingsManager.taskSaveData(curTaskName)
                var curSavedData = JSON.parse(curSaveDataString)
                if (curSaveDataString.length > 2) {
                    curTaskItem.taskStarted = curSavedData.started
                    curTaskItem.taskDone = curSavedData.finished
                    curTaskItem.infoLevelProgress[0] = parseInt(curSavedData.standard)
                    curTaskItem.infoLevelProgress[1] = parseInt(curSavedData.bonus)
                    curTaskItem.infoLevelProgress[2] = parseInt(curSavedData.extra_bonus)
                }
            }

            titleText: _practiceTasks.myModel[index].taskDisplayText
            path: _practiceTasks.myModel[index].taskPath
            descriptionText: _practiceTasks.myModel[index].taskInfo.join("<br>") + "<br><br><br><br><br>"
        }
    }
}
