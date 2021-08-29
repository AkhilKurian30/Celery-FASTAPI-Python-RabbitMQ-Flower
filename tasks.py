
from worker import celery_app
import json
from time import sleep

@celery_app.task
def longtime_add(x, y):
    print('Got Request - Starting work ')
    sleep(10)
    print('Work Finished ')
    print(x + y)
    return x + y