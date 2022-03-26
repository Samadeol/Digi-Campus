import smtplib
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
# from Login.models import Profile
from Hall.models import hallPresence

# 5 minute window
start = datetime.time(23, 30, 0)
end = datetime.time(23, 31, 1)
current = datetime.datetime.now().time()

def start():

    global start, end, current
    
    # 5 minute window
    start = datetime.time(23, 30, 0)
    end = datetime.time(23,31 ,1)
    current = datetime.datetime.now().time()

    scheduler = BackgroundScheduler()
    scheduler.add_job(send_it, 'interval', minutes=1) # check for this every 1 minutes in the 2 minute window
    scheduler.start()


def send_it():

    global start,end, current
    
    # 2 minute window
    current = datetime.datetime.now().time()
    # print(str(current) + " - C")

    if (start <= current <= end):
        
        # for x in hallPresence.objects.all():
        #         if (x.in_hall == True):
        #             usr_email_ids.append(x.user.profile.email[0])
        to_email=[x.user.profile.email for x in hallPresence.objects.all() if (x.in_hall == True)]
        print(to_email)

        # print("sex is on the way!")
        # # Python code to illustrate Sending mail from 
        # # your Gmail account 
        
        # # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # # start TLS for security
        s.starttls()
        
        # # Authentication
        s.login("digicampus352", "digi@campus")
        
        # # message to be sent
        # message = "You are requested to vacate the hall as soon as possible"
        message = 'Subject: {}\n\n{}'.format("DigiCampus Hall Notice", "You are requested to vacate the Hall asap.")

        # # sending the mail
        s.sendmail("digicampus352", to_email, message)
        
        # # terminating the session
        s.quit()
