import random
import smtplib

def send_otp(otp, recipient_email):
    # Set your email credentials
    EMAIL_ADDRESS = "rutuja.u.sawant@gmail.com"
    EMAIL_PASSWORD = "qjpt vgcw qhlr kwaz"

    # Set the email subject and body
    subject = "OTP"
    body = f"Your OTP is: {otp}"

    # Connect to the email server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # Send the email
    server.sendmail(EMAIL_ADDRESS, recipient_email, f"Subject: {subject}\n\n{body}")

    # Disconnect from the server
    server.quit()

def generate_otp():
    # Generate a random 6-digit OTP
    return random.randint(100000, 999999)

# Set the recipient's email address
recipient_email = "dontknowabc2001@gmail.com"

# Generate and send the OTP
otp = generate_otp()
send_otp(otp, recipient_email)

print("OTP sent successfully!")