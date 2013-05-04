#/usr/bin env python
#-*- encoding:utf-8 -*-

#Oct.30 12:45 p.m. 
def apply(date_str):
    date_str = str(date_str)
    f = date_str[:10].split("-")  # ['2012', '10', '30']
    h = date_str[11:19].split(":")# ['14', '45', '34']
    return month_letter(int(f[1])) + str(f[2]) + " " + am_pm_hour(int(h[0])) + ":" + h[1] + am_pm(h[0])

def am_pm_hour(hour):
    if hour > 12:
        return str((hour-12))
    else:
        return str(hour)  
 

def am_pm(hour):
    if int(hour) > 12:
        return " p.m."
    else:
        return " a.m." 

def month_letter(month_number):
    month_number = str(month_number)
    month = {'1': 'Jan.', 
             '2': 'Feb.', 
             '3': 'Mar.', 
             '4': 'Apr.', 
             '5': 'May.', 
             '6': 'Jun.', 
             '7': 'Jul.', 
             '8': 'Aug.', 
             '9': 'Sep.', 
             '10': 'Oct.', 
             '11': 'Nov.', 
             '12': 'Dec.'}  
    return month[month_number]  

#'2012-10-30 14:34:49.441405+00:00'