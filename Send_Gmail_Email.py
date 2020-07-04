import smtplib
import config


def send_email(subject, msg):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message='Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS,message)
        server.quit()
        print("Email sent successfully")
    except:
        print("email fail to send.")

subject='GMAIL email Automation success'        
msg='Finally I\'m able to automate gmail email generation using this script'
send_email(subject,msg)
