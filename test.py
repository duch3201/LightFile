import os
from datetime import datetime
import sys
import time

output_path = "   42069"
win_username = os.getlogin()
app_root_path = os.path.dirname(os.path.realpath(__file__))

#history file
histfileopn = "history.lfh"
date_text = "date: "
time_text = "time: "

os.chdir(app_root_path)
current_datetime = datetime.now()
current_time = datetime.now().time()

# creating / opening the historu.lfh file

history = open(histfileopn, 'w')
test1 = print(date_text,":  " ,current_datetime)
test2 = print(time_text,":  " ,current_time)
test3 = print("file_location:  ",output_path)
current_datetime = current_datetime.strftime('%m/%d/%y')
time = time.strftime("   %H:%M:%S") 
history.write(current_datetime)
history.write(time)
history.write(output_path)
history.close()

print(output_path)