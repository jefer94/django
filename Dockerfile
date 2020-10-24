FROM python:alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

COPY requirements.txt .
# RUN yarn install --production=true && \
#     yarn global add typescript && \
#     yarn add @chocolab/configs && \
#     apk cache clean

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
    # apk cache clean

RUN pip install uwsgi
RUN pip install -r requirements.txt
COPY . .

ENV PORT=8000
EXPOSE 8000
# CMD python manage.py migrate; ./manage.py runserver

CMD ./manage.py collectstatic --noinput; \
    uwsgi --http "0.0.0.0:${PORT}" --module api.wsgi --master --processes 4 --threads 2