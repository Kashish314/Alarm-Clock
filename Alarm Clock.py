#ALARM_CLOCK

#importing-libraries
from tkinter import *;
import datetime;
import time;
import winsound;

def alarm(alarm_timer):
    while True:
        time.sleep(1)                           
        current_time= datetime.datetime.now()    
        now= current_time.strftime("%H:%M:%S")
        date= current_time.strftime("%d/%m/%y")
        print("DATE:", date)
        print(now)        
        if (now == alarm_timer):
            print("Wake Up! Wake Up! It's a brand new day!")
            winsound.Beep(2000,3000)
            break
            
def actual_time():
    alarm_timer= f"{hour.get()}:{min.get()}:{sec.get()}" 
    alarm(alarm_timer)
    
clock= Tk()

#clock-box-formatting
clock.title("ALARM CLOCK")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24hr format!", fg="red",bg="black",font="Arial").place(x=90,y=120)
addTime= Label(clock, text="Hour: Min: Sec", font=60).place(x=120)
setYourAlarm= Label(clock, text="WAKE UP TIME: ", fg="blue", relief="solid", font=("Helevetica",7,"bold")).place(x=15, y=30)

#variales
hour= StringVar()
min= StringVar()
sec= StringVar()

#time-to-set-alarm
hourTime= Entry(clock, textvariable= hour, bg="pink", width=15).place(x=110,y=30)
minTime= Entry(clock, textvariable= min, bg="pink", width=15).place(x=150,y=30)
secTime= Entry(clock, textvariable= sec, bg="pink", width=15).place(x=200,y=30)

#time-input-by-user
submit= Button(clock, text="Set Alarm", fg="blue", width=10, command= actual_time).place(x=130,y=70)
clock.mainloop()
