import QtQuick
import QtQuick.Controls

Page {
    id: _basePage

    anchors.fill: parent

    visible: false

    property bool forceDefaultData: false

    Component.onCompleted: {
        checkAndSetDefaultData()
    }

    Text {
        id: defaultTextMessage
        anchors.fill: parent
        anchors.margins: 64

	z: 100

        property bool isDefaultMessage: true

        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignTop
        text: "Hello, I am still in development! :)"
        font.pointSize: 64
    }

    function checkAndSetDefaultData()
    {
        if (_basePage.children.length > 0) {
            if (_basePage.children[0].children.length > 1 && !forceDefaultData) {
                defaultTextMessage.visible = false
            } else {
                var isDefaultPage = _basePage.children[0].children[0].isDefaultMessage
                if (isDefaultPage) {
                    defaultTextMessage.visible = true
                }
            }
        }
    }
}
