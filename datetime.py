import datetime

def days_in_month(year, month):
    
    given=datetime.date(year, month,1)
    if month==12:
        subsequent=datetime.date(year+1,1,1)
    else:
        subsequent=datetime.date(year, month+1,1)
        
    number_of_days=subsequent-given
    return number_of_days.days

def is_valid_date(year, month, day):
   
    if  (datetime.MINYEAR<=year<=datetime.MAXYEAR)\
and (1<=month<=12) and(0<day<=days_in_month(year, month)):
        return True
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
   
    if (not is_valid_date(year1, month1, day1)) or\
(not is_valid_date(year2, month2, day2)) or \
(datetime.date(year2, month2,day2)<=datetime.date(year1, month1,day1)):
        return 0
    else:
        number_of_days_between=datetime.date(year2, month2,day2)-datetime.date(year1, month1,day1)
        return number_of_days_between.days

def age_in_days(year, month, day):
    
    if (not is_valid_date(year, month, day))\
or (datetime.date(year, month,day)>=datetime.date.today()):
        return 0
    else:
        age_days=datetime.date.today()-datetime.date(year, month,day)
        return age_days.days
