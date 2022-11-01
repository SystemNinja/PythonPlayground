from audioplayer import AudioPlayer

song = r"D:\music\A Jedi´s Fury Extended.mp3"

player = AudioPlayer(song)

while True:
    action = input("Play/Pause/Stop/Exit/Resume")
    if action == "p":
        player.pause()
    elif action == "pl":
        player.play(block=False)
    elif action == "s":
        player.stop()
    elif action == "r":
        player.resume()
    else:
        player.close()
        break
