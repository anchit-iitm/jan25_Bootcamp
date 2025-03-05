from celery import Task

from app import celery_app
from models import category
from celery_context import flask_context



@celery_app.task(base=flask_context)
def celery_hello():
    print('Hello, Celery!')
    from time import sleep
    sleep(5)
    cate = category.query.first()
    return cate.name