"""
Browse files via tkinter
https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/

"""
from tkinter import *
from tkinter import filedialog
from audioplayer import AudioPlayer



def play_music():
    global paused
    print(paused)
    paused = False
    if paused:
        player.resume()
        print(paused)
    elif not paused:
        player.play()
        paused = True
        print(paused)

def pause_music():
    player.pause()
    paused = True
    print(paused)

def stop_music():
    player.stop()

def resume_music():
    player.resume()

song_name = r"D:\music\A Jedis Fury Extended.mp3"
player = AudioPlayer(song_name)


window = Tk()
window.title("Media Player")

#Window size
w=300
h=110

ws=window.winfo_screenwidth() # get screen width
hs=window.winfo_screenheight() # get screen height

#Calculate x and y coordinates for the Tk window, this shit is used when you want to make window appear in middle of screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

l1 = Label(window, text = "Song Name:")
l1.grid(row=0, column=0)

l2 = Label(window, text="Placeholder for file name")
l2.grid(row=1, column=0)

btn1 = Button(window, text="Browse")
btn1.grid(row=1, column=1)

btn2 = Button(window, text="Play", command=play_music)
btn2.grid(row=2, column=0)

btn3 = Button(window, text="Pause", command=pause_music)
btn3.grid(row=2, column=1)

btn4 = Button(window, text="Stop", command=stop_music)
btn4.grid(row=2, column=2)

btn5 = Button(window, text="Resume", command=resume_music)
btn5.grid(row=2, column=3)

window.mainloop()