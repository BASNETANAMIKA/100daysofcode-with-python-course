from datetime import timedelta, datetime
import time

timer = input("enter time is seconds for timer: ")
time_interval = datetime.strptime(timer, "%S").second
# print ("start_time_str is {0}".format(time_interval))
delta = timedelta(seconds=time_interval)

start = input("Press enter to start timer ")
start_time = datetime.today()
print("the start time is [{0}]".format(start_time))

end_time = start_time + delta
print("the end_time is [{0}]".format(end_time))

while True:
    # print(datetime.today())
    if datetime.today() >= end_time:
        print("your time is up - {0} seconds and the time is [{1}]".format(time_interval, time.ctime()))
        break
