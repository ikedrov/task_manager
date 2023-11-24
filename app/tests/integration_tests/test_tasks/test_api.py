import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('title, description, completed, status_code', [
    ('task1', 'some task 1', False, 200),
    ('task2', 'some task 2', 2, 422),
    ('', '', '', 422)
])
async def test_add_and_get_tasks(title, description, completed, status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.post('/tasks', params={
        'title': title,
        'description': description,
        'completed': completed
    })
    assert response.status_code == status_code
    response = await authenticated_ac.get('/tasks')
    if str(status_code) != '422':
        assert response.json()[-1]['title'] == title


@pytest.mark.parametrize('task_id, completed, status_code', [
    (1, False, 200),
    (-1, True, 404),
    ('a', False, 422),
    ('', False, 307)
])
async def test_get_and_update_tasks(task_id, completed, status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.patch(f'/tasks/{task_id}', params={
        'completed': completed
    })
    assert response.status_code == status_code
    response = await authenticated_ac.get(f'/tasks/{task_id}')
    if not (str(status_code).startswith('4'), str(status_code).startswith('3')):
        assert response.json()['completed'] == completed



