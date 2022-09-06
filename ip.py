import datetime
from random import randint

def ip ():
    full_ip = [str(randint(0, 255)) for i in range(4)]
    for i in range(len(full_ip)):
        if int(full_ip[i]) >= 0 and int(full_ip[i]) < 10:
            full_ip[i] = "00" + full_ip[i]
        elif int(full_ip[i]) >= 10 and int(full_ip[i]) < 100:
            full_ip[i] = "0" + full_ip[i]
    return '.'.join(full_ip)

def date_ip ():
    year = randint(2000, 2021)
    month = randint(1, 12)
    day = 0
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = randint(1, 31)
    elif month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) :
        day = randint(1, 29)
    elif month == 2 and not(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        day = randint(1, 28)
    else:
        day = randint(1, 30)
        
    date = datetime.datetime(year, month, day, randint(0, 23), randint(0, 59), randint(0, 59))
    return date.strftime(" %Y:%m:%d %H:%M:%S")

file = open('first_ip.txt', 'w', encoding="utf-8")
for i in range(1000):
    
    year = randint(2000, 2021)
    month = randint(1, 12)
    day = 0
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = randint(1, 31)
    elif month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) :
        day = randint(1, 29)
    elif month == 2 and not(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        day = randint(1, 28)
    else:
        day = randint(1, 30)
        
    date = datetime.datetime(year, month, day, randint(0, 23), randint(0, 59), randint(0, 59))
    file.write(ip() + date_ip() + "\n")
file.close()