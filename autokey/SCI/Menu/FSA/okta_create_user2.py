import fsasetup as fsa

# Set first name
keyboard.send_keys(fsa.process_form("Name").split(" ")[0])
keyboard.send_key("<tab>")
# Sett last name
keyboard.send_keys(fsa.process_form("Name").split(" ")[1])
keyboard.send_key("<tab>")
# Set fsa email
# fsa_email = str(data.get("Name")).split(" ")[0] + "." + str(data.get("Name")).split(" ")[1] + "@fullstackacademy.com"
fsa_email = fsa.process_form("GOOGLE Email address")
keyboard.send_keys(fsa_email)
keyboard.send_key("<tab>",2)
# Set personal email
keyboard.send_keys(fsa.process_form("PERSONAL Email address"))
keyboard.send_key("<tab>",3)
keyboard.send_keys("Fullstack123!")