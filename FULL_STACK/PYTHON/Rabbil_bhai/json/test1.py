import datetime
"""
current_date = datetime.datetime.now()
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.time())
print(current_date.weekday)
print(current_date.hour)
print(current_date.minute)
print(current_date.second)

""" 
"""
current_date = datetime.datetime.now()
formated_date = current_date.strftime("%d/%m/%Y")
""" 
""" 
date1 = datetime.datetime(2024,7,1)
date2 = datetime.datetime(2024,9,1)
difference = date1-date2
print(difference)
""" 