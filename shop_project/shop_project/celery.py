import os
from celery import Celery

# seta o modulo settings para o programa 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')

app = Celery('shop_project')

app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()
