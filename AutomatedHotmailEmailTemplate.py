#Sending automated HOTMAIL emails

import smtplib
import time

conn = smtplib.SMTP('smtp-mail.outlook.com', 587) #smtp.emailhostingdomain.ca/com, 587 =port number
#refer to https://automatetheboringstuff.com/ table16.1 for SMTP email hosting domains
time.sleep(3)
conn.ehlo() #start connection with function, if code 250,b'... 250= means connection successful and b'=bytes object
time.sleep(3)
conn.starttls() #call starttls encryption function for when sending password, 220=successful
time.sleep(5)
#username=str(input('please enter your full email:'))
#password =str(input('please enter your password:'))
conn.login('starshiy@ive.ca','Valik1994') #235=successful
time.sleep(5)
conn.sendmail('starshiy@live.ca','starshiy@live.ca', 'Subject: Self-Email \n\nDear Val, thanks for sending youself an email. \n\n-Val')
#read documentation for proper email formatting as needed
#if {} is returned then emails were sent correctly.
time.sleep(10)
conn.quit() #disconnect from smtp server.
