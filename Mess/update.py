from celery.schedules import crontab
from .views import switch
CELERYBEAT_SCHEDULE = {
    # Executes every Monday morning at 7:30 A.M
    'every-monday-morning': {
        'task': switch,
        'schedule': crontab(hour=3, minute=35, day_of_week=1),
        'args': (16, 16),
    },
}