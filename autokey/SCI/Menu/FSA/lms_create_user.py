import fsasetup as fsa

# Set first name
keyboard.send_keys(fsa.process_form("Name").split(" ")[0])
keyboard.send_key("<tab>")
# Sett last name
keyboard.send_keys(fsa.process_form("Name").split(" ")[1])
keyboard.send_key("<tab>")
# Set fsa email
fsa_email = fsa.process_form("GOOGLE Email address")
keyboard.send_keys(fsa_email)
keyboard.send_key("<tab>")
# Set lms password
keyboard.send_keys("###Sunkist0101")
keyboard.send_key("<tab>")
keyboard.send_keys("###Sunkist0101")