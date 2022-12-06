FROM python:3.9-slim-buster
WORKDIR /project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python","manage.py","runserver","0.0.0.0:8000"]
