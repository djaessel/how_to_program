import QtQuick
import QtQuick.Window
import QtQuick.Controls

Rectangle {
    id: enemy1

    property int identifier: 0
    property alias hit: healthBar.hit
    property int hp: 4

    x: parent.width

    onXChanged: {
        if (x <= 0) {
            if (player.hp >= 2) {
                player.hp -= 2
            } else {
                player.hp = 0
            }
        }
    }

    width: 250
    height: 180

    function stop() {
        animMove.stop()
        destroy()
    }

    function performHit() {
        healthBar.width -= healthBar.hit
        enemy1.hp -= 1
    }

    Rectangle {
        id: healthBar

        anchors.left: parent.left
        anchors.top: parent.top

        width: parent.width
        height: 20

        property int hit: 1

        color: "red"
    }

    Label {
        id: hpLabel
        text: "HP: " + enemy1.hp

        anchors.fill: parent
    }

    Image {
        id: smiley

        anchors.top: healthBar.bottom
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right

        source: "https://images7.alphacoders.com/353/353511.jpg"

        fillMode: Image.PreserveAspectCrop

        Component.onCompleted: {
            healthBar.hit = healthBar.width / hp
        }
    }

    // Animate the y property. Setting loops to Animation.Infinite makes the
    // animation repeat indefinitely, otherwise it would only run once.
    SequentialAnimation on x {
        id: animMove

        // Then move back to minHeight in 1 second, using the OutBounce easing function
        NumberAnimation {
            from: parent.width + enemy1.identifier * enemy1.width
            to: 0
            //easing.type: Easing.OutBounce
            duration: 20000 + enemy1.identifier * 1000
        }

        // Then pause for 500ms
        //PauseAnimation { duration: 50 }
    }
}
