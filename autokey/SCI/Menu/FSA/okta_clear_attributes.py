import itertools

def iteration_multi(key1, key2, count):
    for _ in itertools.repeat(None, count):    
        keyboard.send_key("<"+key1+">")
        keyboard.send_key("<"+key2+">")

keyboard.send_key("<tab>", 7)
# delete title
keyboard.send_key("<delete>")
keyboard.send_key("<tab>", 4)
# replace secondary email
keyboard.send_keys("setton@fullstackacademy.com")
iteration_multi("tab", "delete", 22)
keyboard.send_keys("Google")
iteration_multi("tab", "delete", 3)