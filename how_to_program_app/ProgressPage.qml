import QtQuick
import QtQuick.Controls

BasePage {
    id: _progressPage

    property int doneCount: 0
    property int allCount: 0

    property alias progressTopSplit: progressTopSplit


    Rectangle {
        id: progressContainer

        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right

        height: 128

        Text {
            id: progressInfoLabel

            anchors.left: parent.left
            anchors.top: parent.top

            anchors.margins: 32

            height: 32

            font.pointSize: 24

            text: "<i><b>" + qsTr("Current Progress") +
                  " ( " + _progressPage.doneCount + " / " + _progressPage.allCount + " )</b></i>" +
                  " <i>" + parseInt(progressBar.value * 100) + " %</i>"
        }

        ProgressBar {
            id: progressBar

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom

            anchors.margins: 32

            height: 24

            value: (_progressPage.doneCount / _progressPage.allCount)
        }
    }

    LineSplitter {
        id: progressTopSplit

        anchors.top: progressContainer.bottom
    }
}
