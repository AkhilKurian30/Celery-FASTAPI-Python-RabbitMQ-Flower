from celery import Celery
from time import sleep
broker='amqp://guest:guest@127.0.0.1:5672//'
celery_app = Celery(
    'tasks',
    broker=broker,backend='rpc://',
)