from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders





mail_content = '''Hello,
This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
send_from = 'ramesh.developer1589@gmail.com'
sender_pass = 'rameshdev01'
send_to = 'ramesh.rathod01@gmail.com'
#Setup the MIME
#The subject line
#The body and the attachments for the mail

msg = MIMEMultipart()
msg['From'] = send_from
msg['To'] = send_to
msg['Subject'] = 'A test mail sent by Python. It has an attachment.'
msg.attach(MIMEText(mail_content, 'text'))

part = MIMEBase('application', "octet-stream")
part.set_payload(open(file_path, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename=file_path')
msg.attach(part)
print('Mail Sent')

