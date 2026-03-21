import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import threading

EMAIL_USERNAME ="pinkimahato9814@gmail.com" 
EMAIL_PASSWORD = "anht rdll jhkc datf"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL =False

msg = "this is test message"
s= smtplib.SMTP(EMAIL_HOST, EMAIL_PORT, timeout = 120)
if EMAIL_USE_TLS:
    s.starttls()
s.login(EMAIL_USERNAME, EMAIL_PASSWORD)
message = MIMEMultipart()
message['Subject'] = "Test Email"
message.attach(MIMEText(msg, 'plain'))
content = message.as_string()
s.sendmail(EMAIL_USERNAME, "sagar.sedai.np@gmail.com", content)
s.quit()
  # add mail,



import pandas as pd
df = pd.read_csv("./emails.csv")

for index, item in df.iterrows():
    email = item['email']
    name = item['name']
    subject = item['Subject']


threading.Thread(target=send_email, args=(email, name, subject)).start()
