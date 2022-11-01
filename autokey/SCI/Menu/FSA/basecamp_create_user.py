import fsasetup as fsa

# Set name
keyboard.send_keys(fsa.process_form("Name"))
keyboard.send_key("<tab>")
# Set fsa email
fsa_email = fsa.process_form("GOOGLE Email address")
keyboard.send_keys(fsa_email)
keyboard.send_key("<tab>", 2)
keyboard.send_key("<down>", 5)
keyboard.send_key("<enter>")