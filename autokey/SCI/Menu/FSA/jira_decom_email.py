email_addr = dialog.input_dialog("Jira Decom Template", "Type email")

# email_addr returns tuple like:
# DialogData(return_code=0, data='test')
# email_addr.data will just print contents of the data
email_msg = f"""Hey Stephen,

Milos here, I have Fullstack Academy user {email_addr.data}who is no longer with the company.
Can you terminate their Jira account?

Regards
"""

keyboard.send_keys("Fullstack Academy - Jira User Decommission<tab>")
keyboard.send_keys(email_msg)