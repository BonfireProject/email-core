import os
import smtplib

EMAIL_USERADDRESS = 'pwned@bonfiresoftware.org' # This is my email, I beg you not to spam me with emails with a for loop, I am just giving you ideas haha!
EMAIL_MSG = f"Subject: {EMAIL_SUBJECT}\n\n{body}" #This looks weird but trust it me it will make everything work.
EMAIL_SUBJECT = 'Made by Asher Buechel' #Put your subject for the matter of whatever you do with this.
EMAIL_BODY = 'Hello World!' #For you people, the body is the thing you see when you click on the email.
EMAIL_ADDRESS = os.enivron.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#This commented part is for testing so you don't have to send emails to yourself. (DO NOT REMOVE THE QUOTES IF YOU AREN'T TESTING!)
#You also do need to setup it up so here are the commands.
#Linux: python3 -m smtpd -c DebuggingServer -n localhost:578
#578 is the default for this project.
#Windows: python -m smtpd -c DebuggingServer -n localhost:578
#This may be wrong on windows, I don't use Windows myself.
#MaxOSx: Same as Linux.
'''
with smtplib.SMTP(f'localhost', 587) as smtp:
    #smtp.ehlo()
    #smtp.starttls #This encrypts the email
    #smtp.ehlo()

    #smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 

    #Those aren't nessecary for it to run, you are running it locally, you don't need to worry about this unless you are sending it through the interwebs.

    smtp.sendmail(EMAIL_ADDRESS, EMAIL_USERADDRESS, EMAIL_MSG) #This also looks weird but you can figure this out yourself
'''

#This is for our email server that I use. It may be different for you. This is an example for people using their own domains for this.
'''
with smtplib.SMTP('smtp.porkbun.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls #This encrypts the email
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 


    smtp.sendmail(EMAIL_ADDRESS, EMAIL_USERADDRESS, EMAIL_MSG) #This also looks weird but you can figure this out yourself
'''

#You do need to enable unsecure app access for gmail if you don't have 2auth, you will need to make a app passport for 2authed accounts.
'''
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    with smtplib.SMTP('smtp.porkbun.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls #This encrypts the email
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 


    smtp.sendmail(EMAIL_ADDRESS, EMAIL_USERADDRESS, EMAIL_MSG) #This also looks weird but you can figure this out yourself
'''
