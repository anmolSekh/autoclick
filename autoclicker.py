import pyautogui
import time
import sys

#set default time intervals to 5 seconds
timer_interval = 5
num_clicks = 2

if len(sys.argv) == 3:
    timer_interval = int(sys.argv[1])
    num_clicks = int(sys.argv[2])
elif len(sys.argv) == 2:
    timer_interval = int(sys.argv[1])

#Dont wait for too long
#Wait at most 10 seconds between clicks
if(timer_interval > 10):
    timer_interval = 10

#make sure we arent clicking too much
#Max number of click should be 10 for now
if(num_clicks > 10):
    num_clicks = 10

while(num_clicks != 0):
    time.sleep(timer_interval)
    pyautogui.click()
    num_clicks = num_clicks-1

    
        
    





