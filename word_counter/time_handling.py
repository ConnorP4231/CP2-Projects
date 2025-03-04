from datetime import datetime #A module for time

time = datetime.now() #The time

format_time = str(time.strftime("%Y-%m-%d %H:%M:%S")) #Formats the time so it doesn't give a one millionth of a second.