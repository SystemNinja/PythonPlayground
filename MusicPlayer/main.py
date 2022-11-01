'''
https://pysimplegui.readthedocs.io/en/latest/#about-the-pysimplegui-documentation-system
https://pysimplegui.readthedocs.io/en/latest/call%20reference/
https://pysimplegui.readthedocs.io/en/latest/cookbook/
https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-save-and-load-program-settings
https://pysimplegui.readthedocs.io/en/latest/cookbook/#button-graphics-media-player

AudioPlayer
https://github.com/mjbrusso/AudioPlayer/blob/master/example/playerGUI.py
https://pypi.org/project/audioplayer/#description

PyDub
https://github.com/jiaaro/pydub#installation

'''
import PySimpleGUI as sg
from audioplayer import AudioPlayer

sg.theme("DarkBlue")


layout = [
    [sg.Text("Pick a song to play.")],
    [sg.Input(key="-SONGNAME-"), sg.FileBrowse()],
    [sg.Button("Previous"), sg.Button("Play"), sg.Button("Pause"), sg.Button("Stop"), sg.Button("Next")]
]

# no_titlebar=True - Removes top part of the window with title, windows default
# grab_anywhere=True - Move window by clicking anywhere and dragging
window = sg.Window("Music Player", layout, no_titlebar=False, grab_anywhere=True)

paused = False
event, values = window.read()
song_name = values["-SONGNAME-"]
player = AudioPlayer(song_name)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        player.stop()
        player.close()
        break
    if event == "Play":
        if paused == False:
            player.play()
            print(paused,"play")
        else:
            player.resume()
            print(paused,"resume")
    if event == "Pause":
        player.pause()
        paused = True
        print(paused,"pause")
    if event == "Stop":
        player.stop()
        paused = False
        player.close()


window.close()
