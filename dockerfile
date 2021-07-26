FROM python:3.8.5-alpine

#Install ENV
RUN apk update && apk upgrade && apk add bash
# RUN apk add python3-pip
# RUN apk pip install psycopg2-binary

#MKDIR file

#COPY file from local
COPY ["backup.py","secrets.py" ]
#Run file
# RUN ["mkdir","/dev","/qa","/production","/staging" ]

RUN ["python3","./backup.py"]

