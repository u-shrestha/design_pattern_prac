# use base python image
FROM python:3

ENV PYTHONBUFFERED 1

# set working directory to /app
WORKDIR /app
ADD . /app


# copy requirements.txt to the image
COPY requirements.txt /app/requirements.txt


# install python dependencies
RUN pip install -r requirements.txt

COPY . /app

