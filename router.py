from fastapi import APIRouter
from tasks import longtime_add
from celery.result import AsyncResult
from fastapi.responses import JSONResponse
import json
from worker import celery_app

router_tasks = APIRouter()


@router_tasks.get('/simple_start_task')
async def call_method():
    print("Invoking Method ")
    task=longtime_add.delay(1,2)
    return task.id


@router_tasks.get('/simple_task_status/')
async def get_status(task_id:str):
    status = celery_app.AsyncResult(task_id)
    print("Invoking Method ")
    return "Status of the Task " + str(status.state)


@router_tasks.get('/simple_task_result/')
async def task_result(task_id):
    result = AsyncResult(task_id).result
    return "Result of the Task " + str(result)