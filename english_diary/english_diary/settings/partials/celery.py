from celery.schedules import crontab


# Using Redis
# http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html

BROKER_URL = 'redis://localhost:6379/0'

CELERY_ACCEPT_CONTENT = ['pickle', 'json']

CELERYBEAT_SCHEDULE = {
    # Executes everyday at 21:00 P.M
    'send-write-diary-mail': {
        'task': 'users.tasks.send_write_diary_email.SendWriteDiaryEmailTask',
        'schedule': crontab(
            hour=21,
            minute=0,
        ),
    },
}
