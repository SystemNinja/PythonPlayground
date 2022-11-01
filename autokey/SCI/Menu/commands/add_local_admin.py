idiot = dialog.input_dialog("Title", "Enter idiot name")
keyboard.send_keys(f"net localgroup Administrators \"{idiot.data}\" /add")