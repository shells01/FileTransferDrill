# Shelly Ahn
# Python Course, The Tech Academy
# Datetime Drill
# Python 2.7
# Tested on Windows 7
"""
Scenario:
The company you work for just opened 2 branches.
One is in NYC, the other is in London.
They need a program to find out if the branches are open based on the
current time of the Headquarters here in Portland.
The hours of both branches are 9 am - 9 pm in their own time zone.

Task:
Create code that will use current time of the Portland HQ
to find out the time in NYC & London branches,
then compare the time with the branches' hours to see if they are open.

Print out if each of the 2 branches are open or closed.
"""

import datetime
from datetime import timedelta

# get current time in Portland 
now = datetime.datetime.now()
print "Current local date and time in Portland, OR: ", now

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
