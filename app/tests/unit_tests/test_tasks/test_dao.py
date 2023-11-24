import pytest

from app.tasks.dao import TasksDAO


@pytest.mark.parametrize('task_id, exists', [
        (1, True),
        (-1, False),
        ('qwerty@qw.com', False)
    ])
async def test_find_task_by_id(task_id, exists):
    task = await TasksDAO.find_one_or_none(id=task_id)
    if exists:
        assert task
        assert task['id'] == task_id
    else:
        assert not task


