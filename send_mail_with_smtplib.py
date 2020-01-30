import smtplib
import imghdr
from email.message import EmailMessage


msg = EmailMessage()
msg['Subject'] = 'Check out Desert Image'
msg['From'] = Sender_email
msg['To'] = 'receiver_mail'
msg.set_content('msg body')

with open('file address', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_email, Sender_password)

    smtp.send_message(msg)
