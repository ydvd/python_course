import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow {
    id: mainWindow
    height: 160
    width: 300
    title: "My window"

    Item {
        id: page
        visible: true
        width: parent.width

        Rectangle {
            id: myRect
            height: {
                console.log("Im a comment?")
                return 160
            }
            width: parent.width

            color: "#ff0000"

            Text {
                id: mainText
                text: "I am some normal text"
                height: 50
                width: parent.width
                font.pixelSize: 12
                color: "#0ff"
                horizontalAlignment: Text.AlignHCenter
            }

            Button {
                id: mainbutton
                text: "Push Me"
                anchors.top: mainText.bottom
                onClicked: {
                    if(myRect.color == "#000000") {
                        myRect.color = "#fff"
                        mainText.color = "#000"
                    }
                    else {
                        myRect.color = "#000"
                        mainText.color = "#fff"
                    }

                    console.log(myRect.color)
                }
            }

        }
    }
}