from crontab import CronTab
 
my_cron = CronTab(user='trungnguyen')
job = my_cron.new(command='python3 backup1.py')
job.hour.every(2)

my_cron.write()
