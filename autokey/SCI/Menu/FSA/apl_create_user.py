import fsasetup as fsa

# Set first name
keyboard.send_keys(fsa.process_form("Name").split(" ")[0])
keyboard.send_key("<tab>",2)
# Sett last name
keyboard.send_keys(fsa.process_form("Name").split(" ")[1])
keyboard.send_key("<tab>",6)
keyboard.send_key("<down>",35)
keyboard.send_key("<tab>",5)
# Set fsa email
fsa_email = fsa.process_form("GOOGLE Email address")
keyboard.send_keys(fsa_email)
keyboard.send_key("<tab>")
