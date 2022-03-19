from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from Login.models import Profile

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_it, 'interval', minutes=5) # check for this every 5 minutes
    scheduler.start()

def send_it():
    
    # 5 minute window
    start = datetime.time(23, 30, 0)
    end = datetime.time(23, 35, 0)
    current = datetime.datetime.now().time()

    if (start <= current <= end):
        usr_email_ids = Profile.objects.all().values_list('email')
        to_email=[u[0] for u in usr_email_ids]

        send_mail(
        'Subject',
        'Message.',
        'from@example.com',
        to_email,
        fail_silently=False,
    )

# https://docs.djangoproject.com/en/4.0/_modules/django/core/mail/
# send_mail and send_mass_mail methods()
# +
# set the following in the settings.py file:
#
# EMAIL_HOST_USER = 'your_email'
# EMAIL_HOST_PASSWORD = 'your password'



