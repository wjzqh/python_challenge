from datetime import *
 
def isleap(year):
    #class datetime.date(year, month, day) 
    d = date(year, 3, 1)
    #class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, hours=0, weeks=0)
    return (d - timedelta(days=1)).day == 29

for year in range(1006, 2000, 10):
    #weekday返回日期是星期几，[0, 6]，0表示星期一
    if isleap(year) and date(year, 1, 26).weekday() == 0:
        print year
#the year is 1756, and the date is 1756.1.27.The 27th is significant, because that's the birthdate of Mozart.