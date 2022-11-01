import fsasetup as fsa

keyboard.send_keys(fsa.process_form("Cost Center"))
keyboard.send_key("<tab>")
keyboard.send_keys("Fullstack Academy")
keyboard.send_key("<tab>", 4)
keyboard.send_keys(fsa.process_form("Manager Level (IC/Mngr/Sr.Mngr/Dir/Etc)"))
keyboard.send_key("<tab>")
if(fsa.process_form("PT/FT") == "Full time"):
    keyboard.send_keys("Salary")
    keyboard.send_key("<tab>")
else:
    keyboard.send_keys("Hourly")
    keyboard.send_key("<tab>")
keyboard.send_keys(fsa.process_form("Exemption Status"))
keyboard.send_key("<tab>")
keyboard.send_keys(fsa.process_form("Employee Type"))
keyboard.send_key("<tab>",2)
keyboard.send_keys(fsa.process_form("PT/FT"))