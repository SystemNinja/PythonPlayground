#Enter script code
#Enter script code
idiot = dialog.input_dialog("Title", "Name")
issue = dialog.input_dialog("Title", "Issue")
msg=f"""
Hi {idiot.data} Milos here from Setton Consulting. I am contacting you regarding the ticket about {issue.data}. Can I remote in to take a look?
"""

keyboard.send_keys(msg)