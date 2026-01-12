day=int(input("Enter day: "))
month=int(input("Month (b/w1&12): "))
year=int(input("year (yyyy): "))
month-=1
if(year%4==0):
    yr="leap"
else:
    yr="not leap"
if(yr=="leap"):
    montd=[31,29,31,30,31,30,31,31,30,31,30,31]
else:
    montd=[31,28,31,30,31,30,31,31,30,31,30,31]
    monthname=["January","February","March","April","May","June","July","August","September","Octuber","November","December"]
    noofdays=int(montd[month])
    day+=1
if((day)>(noofdays)):
    day=day-noofdays
    month+=1
if(month>11):
    month=0
    year+=1
print(day,monthname[month],year)