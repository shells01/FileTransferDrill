# Python course, drill Item 58
import datetime
from datetime import timedelta


# get current time in Portland 
now = datetime.datetime.now()

# time difference with NY and get NY time
tdelta = timedelta(hours = 3)

nydt = now + tdelta

# convert nydt to time object nytime
nytime = datetime.time(nydt.hour, nydt.minute, nydt.second)
print "Time in NY: ", nytime

# time difference with London, and get London time
tdelta2 = timedelta(hours = 8)

londondt = now + tdelta2

# convert londondt to time object londontime
londontime = datetime.time(londondt.hour, londondt.minute, londondt.second) 
print "Time in London: ", londontime


# store's opening and closing times, 9 am to 9 pm
opentime = datetime.time(9,0,0)
closetime = datetime.time(23,0,0)

# determine if New York branch is open or closed
if nytime >= opentime and nytime <= closetime:
    print "The New York branch is open"
else:
    print "The New York branch is closed"

# determine if London branch is open or closed
if londontime >= opentime and londontime <= closetime:
    print "The London branch is open"
else:
    print "The London branch is closed"


