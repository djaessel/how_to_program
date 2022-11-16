import QtQuick
import QtQuick.Controls

Rectangle {
    id: _videoTutorialThumbnailItem

    property double resizer: 0.75

    function init(videoData, listIndex, container, contHeight) {
        if (listIndex < 2) {
            anchors.top = container.top
        } else if (container) {
            // TODO: get children and then add anchors based on current bottom
            var prevIndex = listIndex - 1
            if ((listIndex % 2) != 0) {
                prevIndex = prevIndex - 1
            }

            var hackHeight = Screen.height * 0.25 // this is not good!!! later use actual height of container
            var newY = container.children[prevIndex].y + hackHeight
            _videoTutorialThumbnailItem.y = newY
        }

        if ((listIndex % 2) == 0) {
            _videoTutorialThumbnailItem.anchors.right = container.right
        } else {
            _videoTutorialThumbnailItem.anchors.left = container.left
        }

        var orderCode = videoData.orderCode

        videoTitle = videoData.title

        var url = videoData.url

        // maybe do this part in python later on
        if (url.indexOf('/') >= 0) {
            var videoUrlData = ""
            if (url.indexOf("watch?v=") >= 0) {
                videoUrlData = url.split("/")[3].split("=")[1].split("?")
            } else if (url.indexOf("youtu.be") >= 0) {
                videoUrlData = url.split("/")[3].split("?")
            } else {
                videoUrlData = [url]
            }

            var videoId = videoUrlData[0]
            if (videoUrlData.length > 1){
                var time = videoUrlData[1].split("&")[0].split("=")[1]
                videoStartTime = time
            }

            if (url.indexOf("youtu") >= 0 && url.indexOf("playlist") < 0) {
                curYoutubeVideoId = videoId
            }

            var allVideoTimeSeconds = 0
            // TODO: get this from actual video!
            videoDurationAllSeconds = allVideoTimeSeconds
        }

        //var dependencies = videoData.dependencies

        videoInfo = videoData.infoText.join("\n").replace(",\n", ", ")
    }

    property string curYoutubeVideoId: "wKqLaNqxgas" // test video id
    property string defaultVideoUrl: "https://www.youtube.com/watch?v=" + curYoutubeVideoId + "?t=" + videoStartTime
    property string thumbnailUrl: "https://img.youtube.com/vi/" + curYoutubeVideoId + "/maxresdefault.jpg"
    property string alternativeThumbnailUrl: "https://i1.ytimg.com/vi/" + curYoutubeVideoId + "/hqdefault.jpg"

    property string videoTitle: "Test Video Title"
    property string videoInfo: "Video Info"

    property int videoStartTime: 0 // maybe get this from the link
    // TODO: get time from actual video
    property int videoDurationAllSeconds: 3460 // test duration
    property int videoDurationAllActualSeconds: videoDurationAllSeconds - videoStartTime
    property int videoDurationSeconds: videoDurationAllActualSeconds % 60
    property int videoDurationMinutes: parseInt(videoDurationAllActualSeconds / 60)
    property int videoDurationHours: parseInt(videoDurationMinutes / 60)

    property bool mouseInside: false
    //property bool mouseDown: false

    color: (mouseInside) ? "#9a9" : "#ded"
    border.color: (mouseInside) ? "#aba" : "gray"
    border.width: 1

    width: parent.width * 0.5
    height: parent.height * 0.3

    VideoTutorial {
        id: vidTut
        anchors.fill: parent
        visible: false
    }

    MouseArea {
        anchors.fill: parent
        hoverEnabled: true

        onClicked: {
            stackView.push(vidTut)
            //systemCaller.openUrl(defaultVideoUrl)
        }

        onEntered: {
            mouseInside = true
        }

        onExited: {
            mouseInside = false
        }
    }

    Label {
        id: videoTitleLabel

        anchors.left: parent.left
        anchors.top: parent.top
        anchors.right: parent.right

        anchors.leftMargin: resizer * 32
        anchors.topMargin: resizer * 8

        height: resizer * 48

        font.pointSize: resizer * 24

        verticalAlignment: Text.AlignVCenter

        text: "<b>" + videoTitle + "</b>"
    }

    Label {
        id: videoTimeLabel

        anchors.left: parent.left
        anchors.top: videoTitleLabel.bottom
        anchors.right: parent.right

        anchors.leftMargin: resizer * 32

        height: resizer * 32

        font.pointSize: resizer * 18

        verticalAlignment: Text.AlignVCenter

        text: "Duration: " + ((videoDurationHours > 0) ? videoDurationHours + ":" : "") + videoDurationMinutes + ":" + videoDurationSeconds
    }

    Image {
        id: videoThumbnail

        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.top: videoTimeLabel.bottom

        anchors.margins: resizer * 32
        anchors.topMargin: resizer * 8

        width: parent.width * 0.33

        smooth: true
        fillMode: Image.PreserveAspectCrop

        source: thumbnailUrl

        cache: true
        asynchronous: true

        onStatusChanged: {
           if (status == Image.Error) {
              source = alternativeThumbnailUrl
              // maybe later more will be added
           }
           // some are stuck in Image.Loading ???
        }
    }

    Label {
        id: videoInfoText

        anchors.left: videoThumbnail.right
        anchors.top: videoThumbnail.top
        anchors.right: parent.right
        anchors.bottom: videoThumbnail.bottom

        anchors.margins: 16
        anchors.topMargin: 0

        wrapMode: Text.WordWrap
        elide: Text.ElideRight

        font.pointSize: 16

        text: videoInfo
    }
}
