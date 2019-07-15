FROM python:3.7.2-alpine

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD python manage.py run -h 0.0.0.0

