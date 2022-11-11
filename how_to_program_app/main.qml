import QtQuick
import QtQuick.Controls

Window {
    id: appWindow

    width: Screen.width
    height: Screen.height
    visible: true
    title: qsTr("How to program")

    color: "#cdc"

    property bool menuSmall: true
    property int userMode: 0

    property var userModeTexts: [
        "Beginner",
        "Advanced",
        "Hooked",
        "Insane",
        "Hacker",
    ]

    ListModel {
        id: listModel

        ListElement {
            textx: "Dashboard | Home"
            //icon: "\u2302"
            icon: "\ue49f"
        }
        ListElement {
            textx: "Video Tutorials"
            icon: "\uf03d"
        }
        ListElement {
            textx: "Practice Tasks"
            icon: "\uf120"
        }
        ListElement {
            textx: "User Account Settings"
            icon: "\uf183"
        }
//        ListElement {
//            textx: "Settings"
//            icon: "\uf0c9"
//        }
    }

    Rectangle {
        id: titleBar

        anchors.left: sideMenu.right
        anchors.top: parent.top
        anchors.right: parent.right

        height: 64

        MenuButton {
            id: menuSwitcher

            anchors.top: parent.top
            anchors.left: parent.left
            anchors.bottom: parent.bottom

            text: (appWindow.menuSmall) ? ">" : "<"
            width: titleBar.height

            mouseItem.onClicked: {
                appWindow.menuSmall = !appWindow.menuSmall
            }
        }

        MenuButton {
            id: settingsButton

            anchors.top: parent.top
            anchors.right: parent.right
            anchors.bottom: parent.bottom

            text: "\uf0c9"
            width: titleBar.height

            mouseItem.onClicked: {
                //stackView.push(settings)
            }
        }
    }

    Rectangle {
        id: sideMenu

        anchors.top: titleBar.bottom
        anchors.bottom: parent.bottom
        anchors.left: parent.left

        color: appWindow.color

        // optimize later maybe
        width: (appWindow.menuSmall) ? 64 : Screen.width * 0.2

        ListView {
            id: sideMenuView

            anchors.fill: parent

            model: listModel
            delegate: MenuButton {
                id: _curDelegate
                property int id: index

                //height: appWindow.height / listModel.count// - sideMenuView.spacing * listModel.count
                width: sideMenuView.width
                height: 64

                defaultColor: appWindow.color

                textItem.font.pointSize: (appWindow.menuSmall) ? 32 : 24
                text: '<b>' + ((appWindow.menuSmall) ? icon : textx) + "</b>"

                mouseItem.onClicked: {
                    // TODO: check this until it works properly!!!
                    stackView.pop()
                    switch (index) {
                    case 1:
                        if (stackView.currentItem != videoTutorials)
                            stackView.push(videoTutorials)
                        break
                    case 0:
                    default:
                        if (stackView.currentItem != welcomePage)
                            stackView.push(welcomePage) // change to warning modal?
                    }
                }
            }

            focus: true
            interactive: false // deactivates swiping and scrolling
            highlight: Rectangle {
                color: "#aba"
            }
        }
    }

    StackView {
        id: stackView

        anchors.right: parent.right
        anchors.top: titleBar.bottom
        anchors.bottom: parent.bottom
        anchors.left: sideMenu.right

        initialItem: welcomePage

        WelcomePage {
            id: welcomePage
        }

        VideoTutorials {
            id: videoTutorials
            visible: false
        }

        // TODO: add more pages
    }
}
