FROM python:3.11

WORKDIR /task_manager

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /task_manager/docker/*.sh

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]