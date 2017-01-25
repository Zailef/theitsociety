FROM python:3.5.0
ENV PYTHONUNBUFFERED=0
RUN mkdir /website
WORKDIR /website
COPY requirements.txt /website/
RUN pip install -r requirements.txt
COPY . /website/
RUN python3 manage.py collectstatic --noinput
RUN chmod 754 /website/ && chmod -R 755 /website/static/
VOLUME /website/static

