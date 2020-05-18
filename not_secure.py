import smtplib, ssl

port = 465
account = "whatever@gmail.com"
password = "the actual password"

context = ssl.create_default_context()

sender_email = account
receiver_email = "wayne.ngan@gmail.com"
message = """\
Subject: This is the subject

This is the body"""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server :
    server.login(account, password)
    server.sendmail(sender_email, receiver_email, message)

