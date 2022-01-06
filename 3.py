# Write a Python program to calculate the number of days between two dates.
#   Sample dates : (2014, 7, 2), (2014, 7, 11)

import datetime as dt  # datetime module imported and used

date1 = dt.datetime(2014, 7, 2)  # Creating date using datetime() constructor
date2 = dt.datetime(2014, 7, 11)

# output no of days between 2 date
print("No of days between date 2014-07-2 and 2014-07-11 is\n", (date2 - date1).days)