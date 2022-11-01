#Enter script code
fname=dialog.input_dialog("Enter first name")
lname=dialog.input_dialog("Enter last name")
email_addr=dialog.input_dialog("Enter users personal email")


keyboard.send_keys(fname.data)
keyboard.send_key("<tab>")
keyboard.send_keys(lname.data)
keyboard.send_key("<tab>")
keyboard.send_keys(fname.data+"."+lname.data+"@fullstackacademy.com")
keyboard.send_key("<tab>",2)
keyboard.send_keys(email_addr.data)