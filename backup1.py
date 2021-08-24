#! /usr/bin/env python3(use run file with out folder )
from secrets import DBUSER,DBNAME,DBPASS,DBHOST
import psycopg2
import os
import datetime
def conn():
    conn = psycopg2.connect(dbname=DBNAME ,user=DBUSER)
os.system("psql -V")

DATE_FORMAT = "%Y-%m-%d"
timestamp = datetime.datetime.now().strftime(DATE_FORMAT)
n = ["development-account", "development-auth", "development-batch", "development-core", "development-customer", "development-origination", "development-reporting", "qa-account", "qa-auth", "qa-batch", "qa-batch", "qa-customer", "qa-origination", "qa-reporting"]

for dir in n:
    backup_filename = '~/Workspace/snapshot_db/'+ dir +"/"+ dir + "_" + timestamp+".tar"
    os.system("pg_dump -F t "+ dir +"  > "+backup_filename)
    print("Backup Successfully" )


#Delete old file than 30daysKT
# os.system("find ./backup_file -mtime +30 -type f -name '*.tar' ")  #(Find files modified more than 1 or X days(Today is 1))
#os.system("find ./database-bk -mtime +30 -type f -name '*.tar' -delete") #(Find files modified last X days)