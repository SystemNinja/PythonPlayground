idiot = dialog.input_dialog("Title", "Name of idiot")
msg =f"""
Hello {idiot.data},

Problem has been taken care of, if there is anything else that you need, let me know.

Regards,

Milos
"""

keyboard.send_keys(msg)