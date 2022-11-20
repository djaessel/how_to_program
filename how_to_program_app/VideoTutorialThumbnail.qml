import QtQuick
import QtQuick.Controls

Rectangle {
    id: _videoTutorialThumbnailItem

    property double resizer: 0.75

    property bool alreadyOpened: false
    property bool markedAsDone: false

    property string curYoutubeVideoId: "" // test video id
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
    property int videoDurationMinutes: parseInt(videoDurationAllActualSeconds % 3600 / 60)
    property int videoDurationHours: parseInt(videoDurationAllActualSeconds / 3600)

    property bool mouseInside: false
    //property bool mouseDown: false

    color: (mouseInside) ? "#9a9" : "#ded"
    border.color: (mouseInside) ? "#aba" : "gray"
    border.width: 1


    function init(videoData)
    {
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

            var videoId = videoData.videoId
            if (videoUrlData.length > 1){
                var time = videoUrlData[1].split("&")[0].split("=")[1]
                videoStartTime = time
            }

            if (url.indexOf("youtu") >= 0 && url.indexOf("playlist") < 0) {
                curYoutubeVideoId = videoId

                var curSaveDataString = settingsManager.videoSaveData(videoId)
                var curSavedData = JSON.parse(curSaveDataString)
                if (curSaveDataString.length > 2) {
                    alreadyOpened = curSavedData.opened
                    markedAsDone = curSavedData.finished
                }
            }

            var allVideoTimeSeconds = 0
            var times = videoData.duration.split(':')
            allVideoTimeSeconds += parseInt(times[times.length - 1])
            if (times.length > 1) {
                allVideoTimeSeconds += (parseInt(times[times.length - 2]) * 60)
                if (times.length > 2) {
                    allVideoTimeSeconds += (parseInt(times[times.length - 3]) * 3600)
                }
            }

            // TODO: optimize duration loading time with playlist (maybe?)
            videoDurationAllSeconds = allVideoTimeSeconds
        }

        //var dependencies = videoData.dependencies

        videoInfo = videoData.infoText.join("<br>").replace(",<br>", ", ").replace("NO_TEXT_FOUND", "No explanation yet.") + "<br><br><br><br><br>"
    }

    function updateVideoSaveData() {
        if (curYoutubeVideoId != "") {
            settingsManager.handleVideoSaveData(JSON.stringify({
                "videoId": curYoutubeVideoId,
                "opened": alreadyOpened,
                "finished": markedAsDone
            }))
        }
    }

    onMarkedAsDoneChanged: updateVideoSaveData()
    onAlreadyOpenedChanged: updateVideoSaveData()


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

        text: "Duration: " + (
                  ((videoDurationHours > 0) ?
                      ((JSON.stringify(videoDurationHours).length == 1) ? "0" : "") + videoDurationHours + ":" : "") +
                  ((JSON.stringify(videoDurationMinutes).length == 1) ? "0" : "") + videoDurationMinutes + ":" +
                  ((JSON.stringify(videoDurationSeconds).length == 1) ? "0" : "") + videoDurationSeconds
        )
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

        property bool loaded: false

        onStatusChanged: {
           if (status == Image.Error) {
              source = alternativeThumbnailUrl
              // maybe later more will be added
           } else if (status == Image.Loading && !videoThumbnail.loaded) {
              restarte.restart()
           } else if (status == Image.Ready) {
              restarte.stop()
           }/* else {
              // some are stuck in Image.Loading ???
           }*/
        }

        // fix for image loading on start
        Timer {
            id: restarte

            interval: 1500
            repeat: false

            onTriggered: {
                var orgSource = videoThumbnail.source
                videoThumbnail.source = ""
                videoThumbnail.source = orgSource
                videoThumbnail.loaded = true
            }
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
