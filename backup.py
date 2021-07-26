#! /usr/bin/env python3(use run file with out folder )
from secrets import DBUSER,DBNAME,DBPASS,DBHOST
import psycopg2
import os
import datetime

conn = psycopg2.connect(dbname=DBNAME ,user=DBUSER)
os.system("psql -V")
DATE_FORMAT = "%Y-%m-%d-%H"
timestamp = datetime.datetime.now().strftime(DATE_FORMAT)
n = ["dev", "qa", "staging", "production"]

for dir in n:
    backup_filename = './database-bk/'+ dir +"/"+ dir + "_" + timestamp+".tar"
    os.system("pg_dump -F t "+ dir +"  > "+backup_filename)
    print("Backup Successfully" )


#Delete old file than 30daysKT
os.system("find ./database-bk -mtime +3 -type f -name '*.tar' ")  #(Find files modified more than 1 or X days(Today is 1))
#os.system("find ./database-bk -mtime +30 -type f -name '*.tar' -delete") #(Find files modified last X days)