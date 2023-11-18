FROM python:3.11
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install django
RUN pip install requests

ENTRYPOINT ["python", "./AdditionalService/manage.py"]
