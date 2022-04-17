# Pull official base image
# amazon-linux2 버전용
FROM python:3.8-slim-buster
# set work directory
WORKDIR /usr/src/app
# set envirement variable
# .pyc 파일 no 생성
ENV PYTHONDONTWRITEBYTECODE 1
# buffering 하지 않음
ENV PYTHONUNBUFFERED 1
# 도커에 작업 내용 복사
COPY . /usr/src/app/
# install dependencies
RUN pip3.8 install --no-cache-dir -U pip
RUN pip3.8 install --upgrade --ignore-installed pip setuptools
RUN pip3.8 install ez_setup
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
# 가상환경에서 작성한 모듈들 설치
RUN pip3.8 install --no-cache-dir -r requirements.txt