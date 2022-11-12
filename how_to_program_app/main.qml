import QtQuick
import QtQuick.Controls

Window {
    id: appWindow

    flags: Qt.Window | Qt.FramelessWindowHint

    width: Screen.width
    height: Screen.height
    visible: true
    title: qsTr("How to program")

    color: "#cdc"

    property bool menuSmall: true

    property int userMode: 0
    property var userModeTexts: [
        "Beginner", // 4 tasks
        "Advanced", // 4 tasks
        "Hooked",   // 1 tasks
        "Insane",   // 0 tasks
        "Hacker",   // 0 tasks
    ]

    property int infoLevel: 0
    property var infoLevelNames: [
        "Standard",     // default
        "Bonus",        // for interested ones
        "Extra Bonus",  // if you really mean it
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
    }

    Text {
        id: appName

        anchors.left: parent.left
        anchors.top: parent.top
        anchors.right: titleBar.left
        anchors.bottom: titleBar.bottom

        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter

        font.pointSize: 24

        color: "#797"

        text: (appWindow.menuSmall) ? "|-|" : "<b>" + appWindow.title.toUpperCase() + "</b>"
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

            //text: (appWindow.menuSmall) ? ">" : "<"
            text: (appWindow.menuSmall) ? "\u276F" : "\u276E"
            width: titleBar.height

            textItem.font.pointSize: 18

            mouseItem.onClicked: {
                appWindow.menuSmall = !appWindow.menuSmall
            }
        }

        Text {
            id: curPageTitle

            anchors.top: parent.top
            anchors.left: menuSwitcher.right
            anchors.right: settingsButton.left
            anchors.bottom: parent.bottom

            anchors.leftMargin: 32
            anchors.rightMargin: 32

            font.pointSize: 24

            verticalAlignment: Text.AlignVCenter

            text: "..."
        }

        MenuButton {
            id: settingsButton

            anchors.top: parent.top
            anchors.right: exitButton.left
            anchors.bottom: parent.bottom

            text: "\uf0c9"
            width: titleBar.height

            mouseItem.onClicked: {
                stackView.push(settingsPage)
                curPageTitle.text = "Settings".toUpperCase()
            }
        }

        MenuButton {
            id: exitButton

            anchors.top: parent.top
            anchors.right: parent.right
            anchors.bottom: parent.bottom

            //text: "\uf057"
            text: "\uf2d3"
            width: titleBar.height

            mouseItem.onClicked: {
                appWindow.close()
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

        function setNewPage(pageId, index) {
            if (stackView.currentItem !== pageId) {
                if (stackView.currentItem !== welcomePage.id) {
                    stackView.pop()
                }
                stackView.push(pageId)
            } // else change to warning modal?
        }

        function initNewPageByIndex(index) {
            // TODO: check this until it works properly!!!
            // TODO: optimize code logic
            switch (index) {
            case 0:
                setNewPage(welcomePage, index)
                break
            case 1:
                setNewPage(videoTutorials, index)
                break
            case 2:
                setNewPage(practiceTasks, index)
                break
            case 3:
                setNewPage(userSettingsPage, index)
                break
            default:
                console.log("Unknown case in menu: " + index)
            }

            curPageTitle.text = listModel.get(index).textx.toUpperCase()
        }

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

                mouseItem.onClicked: sideMenu.initNewPageByIndex(index)
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

        //initialItem: welcomePage
        Component.onCompleted: {
            sideMenu.initNewPageByIndex(0)
        }

        Transition {
            id: testTransition
            SequentialAnimation {
                XAnimator {
                    from: 0
                    to: 25
                    duration: 5
                }
                XAnimator {
                    from: 25
                    to: 0
                    duration: 5
                }
            }
        }

        pushEnter: testTransition
        pushExit: testTransition

        popEnter: testTransition
        popExit: testTransition

        WelcomePage {
            id: welcomePage
        }

        VideoTutorials {
            id: videoTutorials
        }

        PracticeTasks {
            id: practiceTasks
        }

        UserSettingsPage {
            id: userSettingsPage
        }

        SettingsPage {
            id: settingsPage
        }
    }
}
