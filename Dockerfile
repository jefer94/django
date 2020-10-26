FROM python:alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENV PORT=8000
EXPOSE 8000
CMD ./manage.py migrate && ./manage.py runserver 0.0.0.0:8000
