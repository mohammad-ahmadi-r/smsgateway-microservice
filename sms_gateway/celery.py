import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sms_gateway.settings')

app = Celery('sms_gateway')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()