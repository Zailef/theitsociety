FROM python:3.5.0
ENV PYTHONBUFFERED 1
RUN mkdir /website
WORKDIR /website
ADD requirements.txt /website/
RUN pip install -r requirements.txt
ADD . /website/
