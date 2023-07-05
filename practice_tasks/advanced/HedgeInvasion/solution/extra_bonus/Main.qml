import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    id: window
    width: Screen.width
    height: Screen.height
    visible: true
    title: qsTr("Hello World")

    property var arrayOfHedgeHogs: []

    Component.onCompleted: {
        player.bullet.reset()
    }

    onHeightChanged: {
        player.bullet.reset()
    }

    Label {
        id: hpLabel
        text: "HP: " + player.hp

        anchors.fill: parent

        color: "red"

        font.bold: true
        font.pixelSize: 32
    }

    MouseArea {
        hoverEnabled: true
        propagateComposedEvents: true

        property int lastVal: 0

        anchors.fill: parent
        onMouseXChanged: {
            if (mouseY > lastVal && player.rotation < 15)
                player.rotation += 1
            else if (mouseY < lastVal && player.rotation > -15)
                player.rotation -= 1
            lastVal = mouseY
        }

        onClicked: {
            player.shoot()
        }
    }

    Player {
        id: player
    }

    Rectangle {
        id: line

        x: 0
        y: player.y + player.height - 100

        height: 500
        width: window.width
        color: "black"
    }
}
