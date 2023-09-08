import os
from celery import Celery

celery_app = Celery('celery', broker=f"pyamqp://guest@{os.environ.get('rabbit_host', 'localhost')}//")


@celery_app.task
def sender(email):
    print('This email to %s' % email)
    with open('111.txt', 'w') as f:
        f.write('This email to %s' % email)
    return True
