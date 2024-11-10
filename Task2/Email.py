# Hello this Python Program is to Send automated mail to "jawaharlal@gmail.com" mail id
# Mail will be send at sharp 04.00 from the sender to the receiver mail-id with input suject and body
# For this User must Specify Real User_Email-id, Password, Subject and Body of the mail
# User_EMail-Id should be gmail-id only and it must not have enables two-step authentication
# Password Should be exact match wtih Case, Speical character and all
# If the Subject and Content is not chnaged of overwritten it will be same as declared.

# Before use make sure for user details or error will be displayed
# also before compiling check for modules installation
# if not use "pip install module-name" command for it

#SMT Server is responsible for networking the code and the email portal
import smtplib              

#Use to Assign text or input data to specific body/uni-centric data input
from email.mime.text import MIMEText  

#use to assign multiple part of email like sender, reciever, subject
from email.mime.multipart import MIMEMultipart  

#used to schedule the mail at certain time slot
import schedule 

# Use for Date and Time
import time
from datetime import datetime

def send_email():
    sender_email = "user_email@gmail.com"
    receiver_email = "jawaharlal@gmail.com"
    password = "password"
    subject = "Enter Subject"
    content = "Enter Email Content"

    # Create a container that assigns the sender mail-id, reciever mail-id and subject of the mail
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Assign the input Body of the mail input by the user defined previously
    msg.attach(MIMEText(content, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    print(f"Email sent to {receiver_email} at {datetime.now()}")

# Schedule the mail to be delivered 4 am
schedule.every().day.at("04:00").do(send_email)

# Continuously run the Code till Time is 4 every day
while True:
    schedule.run_pending()
    time.sleep(1)