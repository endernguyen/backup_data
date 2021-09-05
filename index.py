import sys
import psycopg2
import os
import datetime
import time
import boto3

def conn():
        conn = psycopg2.connect(host=os.environ['host'], port=os.environ['port'], 
                                dbname=os.environ['db_name'], user=os.environ['user'], 
                                password=os.environ['password'])
        cur = conn.cursor()
        
def backup_files():
    client = boto3.client('rds')
    connect = conn()
    os.system("psql -l")
    os.system('psql -At -c "SELECT datname FROM pg_database WHERE datistemplate = false;" -d postgres > test.txt')
    DATE_FORMAT = "%m-%d-%H"
    timestamp = datetime.datetime.now().strftime(DATE_FORMAT)
    with open("test.txt") as file:
        name = [line.rstrip() for line in file]
        for db in name:
            snapshot_db = 'snapshot_db'+ db +"/"+ db + "_" + timestamp+".tar"
            os.system("pg_dump -F t "+ db +"  > "+snapshot_db)
            print("Backup Successfully" )
            
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
    upload_files('snapshot_db')
    
    
def lambda_handler(event, context):
    connect=conn()
    backup=backup_files()
    upload=upload_files()
