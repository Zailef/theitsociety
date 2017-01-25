FROM python:3.5.0
ENV PYTHONUNBUFFERED=0
RUN mkdir /website
WORKDIR /website
COPY requirements.txt /website/
RUN pip install -r requirements.txt
COPY . /website/
