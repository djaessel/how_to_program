import QtQuick

Rectangle {
    id: _menuItem

    property string defaultColor: "white"
    property string downColor: "#898"
    property string hoverColor: "#aba"
    property string rightBorderColor: "#aba"

    property alias textColor: _menuItemText.color
    property alias text: _menuItemText.text

    property alias mouseItem: _menuItemMouseArea
    property alias textItem: _menuItemText

    property int borderWidthRight: 1
    property int borderWidthLeft: 1

    color: defaultColor

    Rectangle {
        anchors.fill: parent
        anchors.rightMargin: -borderWidthRight
        anchors.leftMargin: -borderWidthLeft

        z: -1

        color: rightBorderColor
    }

    Text {
        id: _menuItemText

        anchors.fill: parent

        color: "#343"

        font.pointSize: 24
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter

        MouseArea {
            id: _menuItemMouseArea

            anchors.fill: parent

            hoverEnabled: true

            onEntered: {
                _menuItem.color = hoverColor
            }

            onExited: {
                _menuItem.color = defaultColor
            }

            onPressedChanged: {
                if (pressed) {
                    _menuItem.color = downColor
                } else {
                    _menuItem.color = hoverColor
                }
            }
        }
    }
}
