import datetime
from Login.models import Profile
from apscheduler.schedulers.background import BackgroundScheduler

start = datetime.time(23, 55, 0)
end = datetime.time(23, 56, 30)
current = datetime.datetime.now().time()

def start():

    global start, end, current
    
    start = datetime.time(23, 55, 0)
    end = datetime.time(23,56,30)
    current = datetime.datetime.now().time()

    scheduler = BackgroundScheduler()
    scheduler.add_job(update_func, 'interval', minutes=1) # check for this every 1 minutes in the 2 minute window
    scheduler.start()

def update_func():

    global start, end, current

    current=datetime.datetime.now().time()
    if(start<= current<= end):

        # print("updating")

        for obj in  Profile.objects.all():
            
            # print("updating2")
            
            obj.e_0 = obj.e_1
            obj.e_1 = obj.e_2
            obj.e_2 = obj.e_3
            obj.e_3 = obj.e_4
            obj.e_4 = obj.e_5
            obj.e_5 = obj.e_6
            obj.e_6 = obj.e_7
            obj.e_7 = obj.e_8
            obj.e_8 = obj.e_9
            obj.e_9 = 0

            obj.save()
