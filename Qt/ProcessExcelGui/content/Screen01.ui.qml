

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.3
import QtQuick.Controls 6.3
import ProcessExcelGui
import QtQuick.Layouts 6.3

Rectangle {
    id: rectangle
    width: 500
    height: 200
    color: "#1b1a1a"
    border.color: "#ffffff"
    layer.enabled: false

    layer.textureMirroring: ShaderEffectSource.NoMirroring

    Label {
        id: label1
        x: 8
        y: 44
        width: 186
        height: 31
        text: qsTr("Select daily report file..")
    }

    Label {
        id: label2
        x: 8
        y: 85
        width: 186
        height: 31
        text: qsTr("Select weekly report file..")
        textFormat: Text.StyledText
        clip: false
    }

    Button {
        id: button1
        x: 8
        y: 162
        width: 173
        height: 30
        text: qsTr("Generate Daily Report")
        wheelEnabled: false
        font.weight: Font.Normal
        font.capitalization: Font.Capitalize
    }

    Button {
        id: button2
        x: 187
        y: 162
        width: 173
        height: 30
        text: qsTr("Generate Weekly Report")
        font.capitalization: Font.Capitalize
        layer.smooth: false
        layer.mipmap: false
        layer.wrapMode: ShaderEffectSource.RepeatHorizontally
        antialiasing: false
        activeFocusOnTab: true
        focus: false
        font.hintingPreference: Font.PreferDefaultHinting
        wheelEnabled: false
        autoRepeat: false
        autoExclusive: false
        scale: 1
        clip: false
        font.kerning: false
        font.preferShaping: true
        focusPolicy: Qt.StrongFocus
        checkable: false
        highlighted: false
        flat: false
        checked: false
    }

    Button {
        id: button3
        x: 252
        y: 38
        width: 173
        height: 30
        text: qsTr("Browse")
        layer.smooth: false
        wheelEnabled: false
        clip: false
        activeFocusOnTab: true
        layer.mipmap: false
        autoExclusive: false
        flat: false
        autoRepeat: false
        scale: 1
        highlighted: false
        antialiasing: false
        checkable: false
        font.capitalization: Font.Capitalize
        checked: false
        font.hintingPreference: Font.PreferDefaultHinting
        font.kerning: false
        font.preferShaping: true
        focusPolicy: Qt.StrongFocus
        layer.wrapMode: ShaderEffectSource.RepeatHorizontally
        focus: false
    }

    Button {
        id: button4
        x: 252
        y: 79
        width: 173
        height: 30
        text: qsTr("Browse")
        layer.smooth: false
        wheelEnabled: false
        clip: false
        activeFocusOnTab: true
        layer.mipmap: false
        flat: false
        autoExclusive: false
        autoRepeat: false
        scale: 1
        highlighted: false
        antialiasing: false
        checkable: false
        checked: false
        font.capitalization: Font.Capitalize
        font.kerning: false
        font.hintingPreference: Font.PreferDefaultHinting
        font.preferShaping: true
        focusPolicy: Qt.StrongFocus
        layer.wrapMode: ShaderEffectSource.RepeatHorizontally
        focus: false
    }
    states: [
        State {
            name: "clicked"
            when: button1.checked
        }
    ]
}
