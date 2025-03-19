import datetime  
  
# Get the current date  
current_date = datetime.datetime.now()  
  
# Get the day of the year  
day_of_year = current_date.timetuple().tm_yday  
  
print(day_of_year)  
