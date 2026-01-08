day=int(input("Enter day: "))
if(day>31)|(day<1):
    print("invalid input!! Start the program again")
    exit()
month=int(input("Month (b/w1&12): "))
if((month!=1)|(month!=3)|(month!=5)|(month!=7)|(month!=8)|(month!=10)|(month!=12))&(day>30):
    print("invalid input!! Start the program again")
    exit()
if (month>12)|(month<1):
    print("invalid input!! Start the program again")
    exit()
year=int(input("year (yyyy): "))
if year<1:
    print("invalid input!! Start the program again")
    exit()
elif(year%4!=0)&(day>=29):
    print("invalid input!! Start the program again")
    exit()
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