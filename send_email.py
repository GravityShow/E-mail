import smtplib
from email.message import EmailMessage

login_email = "Email adress"
login_generated_pwd = "App pwd generated in Google Account Settings"

##############################

# Instance of email object
email = EmailMessage()

# Email header
email["to"] = "Receiving E-mail adress"
email["subject"] = "Subject of E-mail"

# Email body
email.set_content("Content of E-mail")

##############################

# Using SMTP to send email to gmail.com adress
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(login_email, login_generated_pwd)
    smtp.send_message(email)
    print("E-mail send")