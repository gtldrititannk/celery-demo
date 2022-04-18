import string
import datetime

from celery import shared_task
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from django_celery_demo.celery import celery_app


@shared_task()
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(10)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)


@celery_app.task(bind=True)
def send_notification(self):
    print("\n\n Hi am notification !")
    print("\n\n Datetime Now [Date] --> ", datetime.datetime.now().date())
    print("\n\n Datetime Now [Time] --> ", datetime.datetime.now().time())
    print("\n\n Datetime Now [Hour] --> ", datetime.datetime.now().time().hour)
    print("\n\n Datetime Now [Minute] --> ", datetime.datetime.now().time().minute)
    print("\n\n Datetime After Adding 15 Minutes --> ", datetime.datetime.now() + datetime.timedelta(minutes=15))
    return 'Notification Sent!'
