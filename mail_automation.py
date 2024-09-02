
import smtplib
from email.message import EmailMessage
import imghdr

EMAIL_ADDRES = "farajavitalie@gmail.com"
EMAIL_PASSWORD = "dnwj stvg xsyu skuh"

msg = EmailMessage()
msg['Subject'] = 'Hey! please check doge pic'
msg['From'] = EMAIL_ADDRES
msg['To'] = "farajavitalie1@outlook.com"
msg.set_content('Image is attached')

dog_images = ['doge.png','dog1.png','dog2.png','dog3.png']
for file in dog_images:
    with open(file,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)    

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    
    smtp.login(EMAIL_ADDRES,EMAIL_PASSWORD)
    
    smtp.send_message(msg)