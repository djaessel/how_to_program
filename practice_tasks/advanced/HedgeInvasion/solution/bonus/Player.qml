import QtQuick
import QtQuick.Controls

Rectangle {
    id: player

    property int isFirst: 1
    property alias rotation: gunny.rotation
    property alias bullet: bullet

    property int starterY: 0

    property int hp: 7

    height: 250
    width: 250

    x: 0
    y: parent.height / 2 - height / 2

    function shoot() {
        if (isFirst == 1) {
            for (var i = 0; i < 4; i++) {
                var component = Qt.createComponent("Enemy1.qml")
                var sprite = component.createObject(parent, {"identifier": i})
                sprite.y = line.y - sprite.height
                arrayOfHedgeHogs.push(sprite)
            }
            isFirst = 0
        } else {
            bulletShotStart.from = starterY
            bulletShotStart.to = starterY + 120 * (gunny.rotation / 15)
            bulletShotAngle.start()
            bulletShot.start()
        }
    }

    Rectangle {
        id: bullet

        width: 100
        height: 100

        radius: 90

        color: "black"

        x: 50
        y: parent.y + parent.height * 0.5

        onXChanged: {
            for (var i = 0; i < arrayOfHedgeHogs.length; i++) {
                if (arrayOfHedgeHogs[i])
                    movement(arrayOfHedgeHogs[i])
            }
        }

        function movement(enemy1) {
            if (bullet.x >= enemy1.x //&&
                    //bullet.y <= (enemy1.y + enemy1.height) &&
                    //bullet.y >= enemy1.y
                    ) {
                bulletShot.stop()
                bullet.reset()
                if (enemy1.hp > 0) {
                    enemy1.performHit()
                }

                if (enemy1.hp <= 0) {
                    enemy1.stop()
                }
            }
        }

        function reset() {
            bullet.x = 50
            bullet.y = parent.height / 4
            starterY = bullet.y
        }

        SequentialAnimation on y {
            id: bulletShotAngle
            //loops: Animation.Infinite
            running: false

            // Move from minHeight to maxHeight in 300ms, using the OutExpo easing function
            NumberAnimation {
                id: bulletShotStart
                from: bullet.y
                to: 0
                //easing.type: Easing.OutExpo
                duration: 1000
            }

            // Then pause for 500ms
            //PauseAnimation { duration: 500 }
        }

        SequentialAnimation on x {
            id: bulletShot
            //loops: Animation.Infinite
            running: false


            // Move from minHeight to maxHeight in 300ms, using the OutExpo easing function
            NumberAnimation {
                from: 50
                to: window.width
                //easing.type: Easing.OutExpo
                duration: 1000
            }

            // Then pause for 500ms
            //PauseAnimation { duration: 500 }
        }
    }

    Image {
        id: gunny

        anchors.fill: parent

        source: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fih0.redbubble.net%2Fimage.250600051.4903%2Fflat%2C1000x1000%2C075%2Cf.u1.jpg&f=1&nofb=1&ipt=00aa35cca261502b25fb82e1be113dee1a2e040efaaf49678d0c1b95db7ec78c&ipo=images"
    }
}
