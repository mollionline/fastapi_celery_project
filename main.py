from project import create_app
from celery import Celery

app = create_app()


celery = app.celery_app
