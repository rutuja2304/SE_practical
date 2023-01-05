import random
import smtplib
import re

sender_email='rutuja.u.sawant@gmail.com'
sender_email_password="qjpt vgcw qhlr kwaz"
reciever_email='dontknowabc2001@gmail.com'#input("enter your email address.")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def validate_email(reciever_email):
    if (re.fullmatch(regex,reciever_email)):
        #generate_otp()
        return True
    else:
        return  False


def generate_otp():
    otp = ''.join([str(random.randint(0, 9)) for i in range(4)])
    #send_mail(otp)
    return otp

def send_mail(otp):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password = sender_email_password)
        msg = 'Hello, Your OTP is '+ str(otp)
        server.sendmail(sender_email, reciever_email, msg)
        server.quit()
        #verify_otp(otp)
        return True
    except:
        return False

def verify_otp(otp):
    verifying_otp=str(input("Enter OTP recieved on email "))
    if verifying_otp==otp:
        print("Verified Succesfully")
    else:
        print("Wrong OTP")
validate_email(reciever_email)