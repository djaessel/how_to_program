import QtQuick
import QtQuick.Controls

Button {
    id: _curButton

    property alias showText: _contentItem.text
    property int pointsToEnable: 0
    property int pointsPerClick: 0

    property bool activated: false

    enabled: (pointsToEnable <= clickerBox.curPoints || curButton.activated)

    onEnabledChanged: {
        if (enabled) {
            _curButton.activated = true
        }
    }

    function addPoints() {
        clickerBox.curPoints += pointsPerClick
    }

    onClicked: addPoints()

    anchors {
        left: parent.left
        right: parent.right
    }

    height: 128

    contentItem: Text {
        id: _contentItem
        text: "Placeholder Text"
        font.pointSize: 28
        color: _curButton.enabled ? (_curButton.down ? "#aabbaa" : "white") : "#gray"
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        elide: Text.ElideRight
    }

    background: Rectangle {
        border.color: _curButton.down ? "#88cc88" : "##223322"
        border.width: 8
        color: _curButton.down ? "#244" : "#577"
        radius: parent.width * 0.25
    }
}
