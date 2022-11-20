import QtQuick
import QtQuick.Controls

ClickerButton {
    id: _autoClickerButton

    property int pointsToEnableFactor: 1
    property int autoClickDuration: 100
    property bool bought: false

    enabled: (((pointsToEnable <= 0) ? 1 : pointsToEnable)
              * pointsToEnableFactor <= clickerBox.curPoints
              || curAutoClickerButton.activated)

    onClicked: {
        _autoClickerButton.bought = true
    }

    Timer {
        id: _intervalTimer

        interval: autoClickDuration // be sure that this is in milliseconds
        running: _autoClickerButton.bought
        repeat: true

        onTriggered: addPoints()
    }
}
