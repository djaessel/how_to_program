import QtQuick

ProgressPage {
    id: _practiceTasks

    Text {
        id: test1

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.top: progressTopSplit.bottom

        font.pointSize: 64

        text: "Hey How"
    }
}
