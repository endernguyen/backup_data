#! /usr/bin/env python3(use run file with out folder )
from secrets import DBUSER,DBNAME,DBPASS,DBHOST
import psycopg2
import os
import datetime
import boto3


def backup():
    client = boto3.client('rds')
    conn = psycopg2.connect(dbname=DBNAME, user=DBUSER, host=DBHOST, password=DBPASS)
    os.system("PGPASSWORD=Trung@123 psql -hlocalhost -p5432 -Utrungnguyen postgres")
    os.system("psql -l")
    os.system('psql -At -c "SELECT datname FROM pg_database WHERE datistemplate = false;" -d postgres > ./Workspace/commercial-infras/lambda_function/src/functions/snapshot-db/test.txt')
    DATE_FORMAT = "%m-%d-%H"
    timestamp = datetime.datetime.now().strftime(DATE_FORMAT)
    with open("./Workspace/commercial-infras/lambda_function/src/functions/snapshot-db/test.txt") as file:
        name = [line.rstrip() for line in file]
        for db in name:
            snapshot_db = './Workspace/snapshot_db/'+ db +"/"+ db + "_" + timestamp+".tar"
            os.system("pg_dump -F t "+ db +"  > "+snapshot_db)
            print("Backup Successfully" )

    # os.system("find .snapshot-db -type f -name 'test.txt' -delete ")

backup()

#Delete old file than 30daysKT
#os.system("find ./snapshot_db -mtime +30 -type f -name '*.tar' ")  #(Find files modified more than 1 or X days(Today is 1))
#os.system("find ./snapshot_db -mtime +30 -type f -name '*.tar' -delete") #(Find files modified last X days)
