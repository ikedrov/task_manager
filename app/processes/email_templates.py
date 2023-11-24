from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def create_task_list_template(tasks: dict, email_to: EmailStr):
    email = EmailMessage()
    email['Subject'] = 'Task list'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f""" 
            <h1>Your task list</h1>
            Here is it:
            {tasks}
        """,
        subtype='html'
    )
    return email


def create_new_task_template(task: dict, email_to: EmailStr):
    email = EmailMessage()
    email['Subject'] = 'New Task'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f""" 
            <h1>Your task</h1>
            Here is it:
            {task}
        """,
        subtype='html'
    )
    return email