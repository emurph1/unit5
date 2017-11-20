#Emily Murphy
#2017-11-20
#displayDate.py - displays date

from datetime import date
from calendar import weekday

months = ['January','February','March', 'April', 'May','June','July','August','September','October','November','December']
days - ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

print('Today is', days[date.today().day],',', months[date.today().month],',',date.today().day,',',date.today().year)