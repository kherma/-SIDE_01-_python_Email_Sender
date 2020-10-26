import smtplib

gmail_user = "your_email@gmail.com"
gmail_pwd = "Your_Password1!"
Emails = ['receiver_1@sample.com', 'receiver_2@sample.com', 'receiver_3@sample.com']
SUBJECT = "Message_Subject"
TEXT = "Message text"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
for TO in Emails:
    BODY = '\r\n'.join(['To: %s' % TO,
            'From: %s' % gmail_user,
            'Subject: %s' % SUBJECT,
            '', TEXT])

    server.sendmail(gmail_user, [TO], BODY)
    print ('email sent')