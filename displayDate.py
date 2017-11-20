#Emily Murphy
#2017-11-20
#displayDate.py - displays date

from datetime import date
from calendar import weekday

today = date.today().day, date.today().month, date.today().year
todayNum = today.weekday
print(today)
