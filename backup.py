#! /usr/bin/env python3(use run file with out folder )
# schedule run time with region on computer
from secrets import DBUSER,DBNAME,DBPASS,DBHOST
import psycopg2
import os
import datetime
import schedule
import time

def connect():
    conn = psycopg2.connect(dbname=DBNAME ,user=DBUSER)
def backup():
    os.system("psql -V")
    # os.system("mkdir -p -v /home/trungnguyen/Workspace/snapshot_db/{development-account,development-auth,development-batch,development-core,development-customer,development-origination,development-reporting,qa-account,qa-auth,qa-batch,qa-batch,qa-customer,qa-origination,qa-reporting}")
    DATE_FORMAT = "%m-%d-%H"
    timestamp = datetime.datetime.now().strftime(DATE_FORMAT)
    n = ["development-account", "development-auth", "development-batch", "development-core", "development-customer", "development-origination", "development-reporting", "qa-account", "qa-auth", "qa-batch", "qa-batch", "qa-customer", "qa-origination", "qa-reporting"]

    for dir in n:
        snapshot_db = './snapshot_db/'+ dir +"/"+ dir + "_" + timestamp+".tar"
        os.system("pg_dump -F t "+ dir +"  > "+snapshot_db)
        print("Backup Successfully" )

schedule.every(5).seconds.do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)

#Delete old file than 30daysKT
# os.system("find ./snapshot_db -mtime +30 -type f -name '*.tar' ")  #(Find files modified more than 1 or X days(Today is 1))
#os.system("find ./snapshot_db -mtime +30 -type f -name '*.tar' -delete") #(Find files modified last X days)