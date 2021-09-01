# schedule run time with region on computer
from secrets import DBUSER,DBNAME,DBPASS,DBHOST
import psycopg2
import os
import datetime
import schedule
import time
import boto3
    
def upload_files(path):
    # Use aws configure 
    session = boto3.Session(profile_name='default')
    s3 = session.resource('s3')
    bucket = s3.Bucket('snapshot-db')
    
    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path)+1:], Body=data)
    
if __name__ == "__main__":
    upload_files
    upload_files('./Workspace/snapshot_db')

upload_files()

# schedule.every(3).seconds.do(upload_files)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

