#!/usr/bin/python
import datetime
import socket
import time
import requests
from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.daemonic = False
sched.start()

def job_function():
    # print("Hello World")
    today = datetime.datetime.today()
    time_stamp = today.ctime()
    socket_name = socket.gethostbyname(socket.gethostname())
    url = 'http://local.host/canteen/test.php'
    query = {'time_stamp': time_stamp,'ip':socket_name}
    res = requests.post(url, data=query)
    # print(res.text)
    time.sleep(20)

# Schedules job_function to be run once each minute
sched.add_cron_job(job_function,  minute='0-59')