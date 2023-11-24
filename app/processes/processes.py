import smtplib

from pydantic import EmailStr

from app.config import settings
from app.processes.cel import celery_app
from app.processes.email_templates import (
    create_new_task_template,
    create_task_list_template,
)


@celery_app.task()
def send_task_list_email(tasks: dict, email_to: EmailStr):
    email_to_mock = settings.SMTP_USER
    msg_content = create_task_list_template(tasks, email_to_mock)
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)


@celery_app.task()
def send_new_task_email(task: dict, email_to: EmailStr):
    email_to_mock = settings.SMTP_USER
    msg_content = create_new_task_template(task, email_to_mock)
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)