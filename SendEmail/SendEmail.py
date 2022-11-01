"""
This program demonstrates how to send an email using python

smtp library ref:
https://realpython.com/python-send-email/

Yagmail lib ref:
https://pypi.org/project/yagmail/
https://github.com/kootenpv/yagmail

OAuth2 ref:
https://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html
OAuth2 uses file oauth2_creds.json to store token which allows sending email from gmail account
without enabling less secure apps

Outlook mail settings:
Server name: smtp.office365.com
Port: 587
Encryption method: STARTTLS

Google mail settings:
smtp.gmail.com
Requires SSL: Yes
Requires TLS: Yes (if available)
Requires Authentication: Yes
Port for SSL: 465
Port for TLS/STARTTLS: 587


"""

import smtplib, ssl
import yagmail

google_email_server = "smtp.gmail.com"
outlook_email_server = "smtp.office365.com"
port_smtp = 465
port_tls = 587
outlook_email = "milosp101@outlook.com"
google_email = "reaperovsorrow101@gmail.com"
receiver = "milosp1606@gmail.com"
# Create a secure SSL context
context = ssl.create_default_context()

#plain text message to be sent as an email
message = """
This is just a test email.
Another email as well.
Sent from python.
"""

#HTML formatted message to be sent as an email
html = """\
<html>
  <body>
    <p>Subject,<br>
       Email from python<br>
       <a href="http://www.realpython.com">Real Python</a> 
       Testing passing html msg via python
    </p>
  </body>
</html>
"""

# send email using SSL encryption method
def send_email_smtp(context):
    password = input("Type password:")
    with smtplib.SMTP_SSL(google_email_server, port_smtp, context=context) as server:
        server.login(google_email, password)
        server.sendmail(outlook_email, receiver, message)

# send email using TLS/STARTTLS encryption method
def send_email_tls(ssl_context):
    password = input("Type password:")
    with smtplib.SMTP(outlook_email_server, port_tls) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=ssl_context)
        server.ehlo()  # Can be omitted
        server.login(outlook_email,password)
        server.sendmail(outlook_email, receiver, message)


def send_email_yagmail_oauth():
    yag = yagmail.SMTP("milosp1606@gmail.com", oauth2_file="oauth2_creds.json")
    yag.send(subject="Email via python", contents=html, to=google_email)


# send_email_smtp(context)
send_email_tls(context)
# send_email_yagmail_oauth()
