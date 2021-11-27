from celery import Celery
from datetime import timedelta

from core.config import settings


app = Celery('data_transfer', broker=settings.broker_url, include=['tasks'])

if settings.debug:
    SCHEDULE = timedelta(seconds=30)
else:
    SCHEDULE = timedelta(minutes=10)

CELERYBEAT_SCHEDULE = {
    'scrap_news': {
        'task': 'scrap_news',
        'schedule': SCHEDULE,
        'options': {
            'queue': 'transfers',
        },
        'args': None,
    },
}

app.conf.beat_schedule = CELERYBEAT_SCHEDULE
