import datetime
from datetime import date

my_date = datetime.datetime.today()

d2 = my_date.strftime("%B")
d3 = my_date.strftime("%d")

def check_date_number(date):
    d = date
    d2 = d[len(date)-4]
    if d2 == '0':
        d = d[1:]

    return d

def adjust_date(date):
    d = date[len(date)-1]
    d2 = date[len(date)-2]

    if d == '1' and d2 != '1':
        adjusted_date = date + 'st'
    elif d == '2' and d2 != '1':
        adjusted_date = date + 'nd'
    elif d == '3' and d2 != '1':
        adjusted_date = date + 'rd'
    else:
         adjusted_date = date + 'th'

    return check_date_number(adjusted_date)


def getDate():
    d1 = my_date.strftime("%B") #Current date's month
    d2 = my_date.strftime("%d") #Current day in month
    d2 = adjust_date(d2) #Adds wording at end of date (ex. 10 == 10th)
    d3 = my_date.strftime("%w") #Current weekday as a number
    print(d1,d2,d3) #for reference internal
    return d1, d2, d3

d1, d2, d3 = getDate()

print (d1, d2, d3)