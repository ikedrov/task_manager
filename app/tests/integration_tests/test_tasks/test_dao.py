import pytest
from fastapi import status

from app.tasks.dao import TasksDAO


class TestTasksCRUD:

    @pytest.mark.parametrize('user_id', [
        (1),
        (-1),
        ('')
    ])
    async def test_get_tasks_for_user(self, user_id):
        tasks = await TasksDAO.get_tasks_for_user(user_id)
        if tasks:
            assert tasks
            for task in tasks:
                assert task['owner_id'] == user_id
        else:
            assert not tasks

    @pytest.mark.parametrize('task_id', [
        (1),
        (-1),
        ('')
    ])
    async def test_get_task_by_id(self, task_id):
        task = await TasksDAO.find_by_id(task_id)
        if task:
            assert task
            assert task['id'] == task_id
        else:
            assert not task

    @pytest.mark.parametrize('title, description, completed, user_id', [
        ('task1', 'task1', False, 1),
        (3, 3, False, 1),
        ('task1', 'task1', False, -1),
        ('', '', False, '')

    ])
    async def test_add_task(self, title, description, completed, user_id):
        new_task = await TasksDAO.add(
            title=title,
            description=description,
            completed=completed,
            owner_id=user_id
        )
        if new_task:
            assert new_task.title == title
            assert new_task.description == description
            assert new_task.completed == completed
            assert new_task.owner_id == user_id
            assert 'Task added successfully'
        else:
            assert not new_task

    @pytest.mark.parametrize('task_id, user_id', [
        (1, 1),
        (-1, -1),
        ('', '')
    ])
    async def test_delete_task(self, task_id, user_id):
        task = await TasksDAO.delete(id=task_id, owner_id=user_id)
        if task:
            assert status.HTTP_204_NO_CONTENT
            assert 'Task deleted successfully'
        else:
            assert not task

    @pytest.mark.parametrize('task_id, completed, user_id', [
        (1, True, 1),
        (-1, True, -1),
        ('', '', '')
    ])
    async def test_update_task(self, task_id, completed, user_id):
        task = await TasksDAO.update(user_id, task_id, completed)
        if task:
            assert 'Task updated successfully'
        else:
            assert not task





