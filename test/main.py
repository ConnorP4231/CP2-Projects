# import datetime  
  
# Get the current date  
# current_date = datetime.datetime.now()  
  
# Get the day of the year  
# day_of_year = current_date.timetuple().tm_yday  
  
# print(day_of_year) 

import matplotlib.pyplot as plt  

categories = ['A', 'B', 'C']  
values = [10, 20, 15]  

plt.bar(categories, values)  

plt.xlabel('Categories')  
plt.ylabel('Values')  
plt.title('Bar Graph Example')  

plt.show()  
