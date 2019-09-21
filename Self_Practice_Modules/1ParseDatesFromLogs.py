from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
print("cwd is {0}".format(os.getcwd()))
logfile = os.path.join(os.getcwd(), '1LogFile.log')

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    print (line)
    time_regex = re.compile(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})')
    mo = re.search(time_regex, line)
    date_string = ''
    datetime_obj = ''
    if mo:
        date_string = mo.group()

    print (date_string)
    if date_string:
        time = date_string.replace("T"," ")
        print ("The time in string format is {0}".format(time))
        datetime_obj = datetime.strptime(time,"%Y-%m-%d %H:%M:%S")
    print (datetime_obj)
    return datetime_obj

def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_regex = re.compile(r'supybot Shutdown initiated.$')
    logs_list = []
    for line in loglines:
        mo = re.search(shutdown_regex, line)
        if mo:
            logline = mo.group()
            logs_list.append(line)
    print ("logs_list is {0}".format(logs_list))
    datetime_obj1 = convert_to_datetime(logs_list[0])
    datetime_obj2 = convert_to_datetime(logs_list[-1])
    time_diff = (datetime_obj2 - datetime_obj1)
    print("time_diff is {0}".format(time_diff))


if __name__=="__main__":
    time_between_shutdowns(loglines)

