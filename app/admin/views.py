from sqladmin import ModelView

from app.tasks.models import Tasks
from app.users.models import Users


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = 'User'
    name_plural = 'Users'
    icon = 'fa-solid fa-user'


class TasksAdmin(ModelView, model=Tasks):
    column_list = [c.name for c in Tasks.__table__.c] + [Tasks.user]
    name = 'Task'
    name_plural = 'Tasks'
    icon = 'fa-solid fa-book'
