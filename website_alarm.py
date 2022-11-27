import time
import webbrowser

alarm_set = input("Set the website alarm in the form of H:M:S: ")

url = input("Enter URL you want to open when the alarm goes off: ")

real_time = time.strftime("%I:%M:%S")

while real_time != alarm_set:
    print ("The time is " + real_time)
    Actual_Time = time.strftime("%I:%M:%S")
    time.sleep(1)
