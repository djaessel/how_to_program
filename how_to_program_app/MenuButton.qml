import QtQuick 2.15

Rectangle {
    id: _menuItem

    property string defaultColor: "white"
    property string downColor: "#898"
    property string hoverColor: "#aba"
    property string extraborderColor: "#aba"
    property string hoverDeactivatedColor: "darkgray"

    property alias textColor: _menuItemText.color
    property alias text: _menuItemText.text

    property alias mouseItem: _menuItemMouseArea
    property alias textItem: _menuItemText

    property int borderWidthRight: 1
    property int borderWidthLeft: 1
    property int borderWidthBottom: 1
    property int borderWidthTop: 1

    color: defaultColor

    Rectangle {
        anchors.fill: parent

        anchors.rightMargin: -borderWidthRight
        anchors.leftMargin: -borderWidthLeft
        anchors.topMargin: -borderWidthTop
        anchors.bottomMargin: -borderWidthBottom

        z: -1

        color: extraborderColor
    }

    MouseArea {
        id: _menuItemMouseArea

        anchors.fill: parent

        hoverEnabled: true

        onEntered: {
            if (_menuItem.enabled) {
                _menuItem.color = hoverColor
            } else {
                _menuItem.color = hoverDeactivatedColor
            }
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

    Text {
        id: _menuItemText

        anchors.fill: parent

        color: "#343"

        font.pointSize: 24
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }
}
