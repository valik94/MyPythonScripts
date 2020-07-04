#Sending automated emails

import smtplib
conn = smtplib.SMTP('smtp.outlook.com', 587) #smtp.emailhostingdomain.ca/com, 587 =port number
#refer to https://automatetheboringstuff.com/ table16.1 for SMTP email hosting domains
conn.ehlo() #start connection with function, if code 250,b'... 250= means connection successful and b'=bytes object
conn.starttls() #call starttls encryption function for when sending password, 220=successful
conn.login('email','password') #235=successful
conn.sendmail('from email','to email','Subject: abcdefg... \n\n Dear Val,\nso long and thanks for your friendship.\n\n-Val.')
#read documentation for proper email formatting as needed
#if {} is returned then emails were sent correctly.

conn.quit() #disconnect from smtp server.
