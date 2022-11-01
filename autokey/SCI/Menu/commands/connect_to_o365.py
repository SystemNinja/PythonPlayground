tenant = dialog.input_dialog("Title","Type tenant username")

# keyboard.send_keys("Import-Module ExchangeOnlineManagement <enter>")
keyboard.send_keys(f"Connect-ExchangeOnline -UserPrincipalName {tenant.data} -ShowProgress $true <enter>")