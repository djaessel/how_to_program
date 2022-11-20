import QtQuick
import QtQuick.Controls

ClickerButton {
    id: _autoClickerButton

    property int pointsToEnableFactor: 1
    property int autoClickDuration: 100
    property bool bought: false

    property int clickerCosts: ((pointsToEnable <= 0) ? 1 : pointsToEnable) * pointsToEnableFactor

    box.color: (bought) ? "#123" : (_autoClickerButton.down ? "#244" : "#577")
    textBox.color: (enabled || bought) ? "white" : "black"

    enabled: (clickerCosts <= clickerBox.curPoints
              || curAutoClickerButton.activated)
              && !bought

    onClicked: {
        if (!_autoClickerButton.bought) {
            clickerBox.curPoints -= clickerCosts
            _autoClickerButton.bought = true
        }
    }

    Timer {
        id: _intervalTimer

        interval: autoClickDuration // be sure that this is in milliseconds
        running: _autoClickerButton.bought
        repeat: true

        onTriggered: addPoints()
    }
}
