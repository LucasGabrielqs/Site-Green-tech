# pull official base image
FROM python:3.10.5-alpine

# set work directory
#WORKDIR /usr/src/delegadomotos
RUN mkdir /home/app 
WORKDIR /home/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /home/app/static

#ENV HOME=/home/delegadomotos
#ENV APP_HOME=/home/delegadomotos/web
#RUN mkdir $APP_HOME
#RUN mkdir $APP_HOME/staticfiles
#WORKDIR $APP_HOME



#RUN sed -i 's/\r$//g' /usr/src/delegadomotos/entrypoint.sh
#

# copy project
COPY . .

COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

CMD [ "sh" , "./entrypoint.sh"]
#ENTRYPOINT ["./entrypoint.sh"]

