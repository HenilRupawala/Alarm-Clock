from plyer import notification # pip install plyer
from tkinter import *
import datetime
import time
import winsound
from threading import *


root = Tk()

root.geometry("400x250")

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm():

    print(CLEAR)
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        time.sleep(1)

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print(CLEAR_AND_RETURN,current_time,set_alarm_time)

        if current_time == set_alarm_time:
            title = 'Alarm'
            message= "It's Time to Wake Up!"
            notification.notify(title = title, message= message, app_icon = None, timeout= 10, toast=False)
            winsound.PlaySound("alarmsound.wav",winsound.SND_FILENAME)
            break

Label(root,text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=20)
Label(root,text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00','01','02','03','04','05','06','07',
         '08','09','10','11','12','13','14','15',
         '16','17','18','19','20','21','22','23','24')
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00','01','02','03','04','05','06','07',
         '08','09','10','11','12','13','14','15',
         '16','17','18','19','20','21','22','23',
         '24','25','26','27','28','29','30','31',
         '32','33','34','35','36','37','38','39',
         '40','41','42','43','44','45','46','47',
         '48','49','50','51','52','53','54','55',
         '56','57','58','59','60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00','01','02','03','04','05','06','07',
         '08','09','10','11','12','13','14','15',
         '16','17','18','19','20','21','22','23',
         '24','25','26','27','28','29','30','31',
         '32','33','34','35','36','37','38','39',
         '40','41','42','43','44','45','46','47',
         '48','49','50','51','52','53','54','55',
         '56','57','58','59','60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(padx=20)

root.mainloop()
