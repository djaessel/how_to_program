import QtQuick
import QtQuick.Controls

BasePage {
    id: _userSettingsPage

    forceDefaultData: true

    ComboBox {
        id: selectUserMode

        anchors.left: parent.left
        anchors.top: parent.top

        anchors.margins: 32

        width: parent.width * 0.25
        height: 120

        displayText: "Select User Mode"

        font.pointSize: 32

        model: userModeTexts

        onCurrentTextChanged: {
            displayText = selectUserMode.currentText
        }
    }

    ComboBox {
        id: selectInfoLevel

        anchors.left: parent.left
        anchors.top: selectUserMode.bottom

        anchors.margins: 32

        width: parent.width * 0.25
        height: 120

        displayText: "Select Info Level"

        font.pointSize: 32

        model: infoLevelNames

        onCurrentTextChanged: {
            displayText = selectInfoLevel.currentText
        }
    }
}
