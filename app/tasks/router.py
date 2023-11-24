
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_cache.decorator import cache
from pydantic import TypeAdapter

from app.exceptions import NoTaskException, NoTaskForUserException
from app.processes.processes import send_new_task_email, send_task_list_email
from app.tasks.dao import TasksDAO
from app.tasks.schemas import STasks
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.get('')
# @cache(expire=60)
async def get_tasks(current_user: Users = Depends(get_current_user)) -> list[STasks]:
    tasks = await TasksDAO.get_tasks_for_user(user_id=current_user.id)
    tasks_json = jsonable_encoder(tasks)
    # send_task_list_email.delay(tasks_json, current_user.email)
    if not tasks:
        raise NoTaskForUserException
    return tasks


@router.get('/{task_id}')
async def get_task(task_id: int, current_user: Users = Depends(get_current_user)):
    task = await TasksDAO.find_by_id(task_id)
    if not task:
        raise NoTaskForUserException
    return task


@router.post('')
async def add_task(title: str, description: str, completed: bool, current_user: Users = Depends(get_current_user)):
    task = await TasksDAO.add(current_user.id, title, description, completed)
    task = TypeAdapter(STasks).validate_python(task).model_dump()
    # send_new_task_email.delay(task, current_user.email)
    return 'Task added successfully'
    # return task


@router.delete('/{task_id}', status_code=204)
async def delete_task(task_id: int, current_user: Users = Depends(get_current_user)):
    task = TasksDAO.delete(id=task_id, owner_id=current_user.id)
    if not task:
        raise NoTaskException
    return 'Task deleted successfully'


@router.patch('/{task_id}')
async def update_task(task_id: int, completed: bool, current_user: Users = Depends(get_current_user)):
    task = await TasksDAO.update(current_user.id, task_id, completed)
    if not task:
        raise NoTaskException
    return 'Task updated successfully'
    # return task
