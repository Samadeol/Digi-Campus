from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from pytz import timezone
from .views import switch

def start():
    s=BlockingScheduler(timezone = settings.TIME_ZONE)
    s.add_job(switch,trigger=CronTrigger(hour="03",minute="26"),id="hi")
    s.start()