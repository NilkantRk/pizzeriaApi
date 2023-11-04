# FROM python:3
# ENV PYTHONUNBUFFERED=1

# WORKDIR /code
# COPY requirements.txt ./
# RUN pip install -r requirements.txt
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/
