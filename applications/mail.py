# encoding:utf-8
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_address = 'karuros.come@gmail.com'
my_password = 'iino0063'
to_address = 'iinoryo@team-lab.com'

charset = 'ISO-2022-JP'
subject = 'Pythonテストメール（件名）'
text = 'メール本文'

msg = MIMEText(text, 'plain', charset)
msg['Subject'] = Header(subject, charset)
msg['From'] = from_address
msg['To'] = to_address
msg['Date'] = formatdate(localtime=True)

smtp = smtplib.SMTP(smtp_host, smtp_port)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(from_address, my_password)
smtp.send_message(msg)
smtp.close()
