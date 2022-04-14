import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_demo.settings')

celery_app = Celery('django_celery_demo')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    return 'Debug Task: Request: {0!r}'.format(self.request)


# celery_app.conf.beat_schedule = {
#     # Executes in every 1 minute
#     'send-notification-in-every-one-minute': {
#          'task': 'my_app.tasks.send_notification',
#          'schedule': crontab()
#         }
# }
