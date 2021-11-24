from celery import Celery
from datetime import timedelta

from .config import settings


app = Celery('payment_service', broker=settings.broker_url, include=['tasks'])

if settings.test:
    SCHEDULE = timedelta(seconds=30)
else:
    SCHEDULE = timedelta(minutes=5)

CELERYBEAT_SCHEDULE = {
    'handle_pending_payments': {
        'task': 'scrap_news',
        'schedule': SCHEDULE,
        'options': {'queue': 'scraps'},
        'args': tuple(),
    },
}

app.conf.beat_schedule = CELERYBEAT_SCHEDULE
