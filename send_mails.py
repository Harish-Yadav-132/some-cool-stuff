import yagmail

receiver_email = input("Receiever Mail: ")
subject = input("Subject: ")
body = input("""Body: """)
attachments = ["filepath"]
yag = yagmail.SMTP("Sender_mail", "Password")
yag.send(
    to=receiver_email,
    subject=subject,
    contents=body,
    attachments=attachments
)
