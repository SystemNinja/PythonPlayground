identity = dialog.input_dialog("Title","Type username or alias without domain")
keyboard.send_keys(f'Start-ManagedFolderAssistant -Identity "{identity.data}"')