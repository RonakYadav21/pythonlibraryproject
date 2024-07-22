from tkinter import *
import datetime
def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    min=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')
    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_pm.config(text=am)
    lab_hr.after(200,date_time)
    date=datetime.date.today()
    todays_date=date.strftime('%D')
    month=date.strftime('%m')
    year=date.strftime('%Y')
    day=date.strftime("%d")
    lab_date.config(text=todays_date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)


clock=Tk()
clock.title("  Digital clock")
clock.geometry('1000x500')
clock.config(bg="lightblue")
lab_hr=Label(clock,text="00",font=("Time New Roman",25,'bold'),bg="red",fg="black")
lab_hr.place(x=120,y=50,height=120,width=140)
lab_min=Label(clock,text="00",font=("Time New Roman",25,'bold'),bg="red",fg="black")
lab_min.place(x=340,y=50,height=120,width=140)
lab_sec=Label(clock,text="00",font=("Time New Roman",25,'bold'),bg="red",fg="black")
lab_sec.place(x=560,y=50,height=120,width=140)
lab_pm=Label(clock,text="00",font=("Time New Roman",25,'bold'),bg="red",fg="black")
lab_pm.place(x=780,y=50,height=120,width=140)

lab_hr_txt=Label(clock,text="Hr",font=("Time New Roman",20,'bold'),bg="red",fg="black")
lab_hr_txt.place(x=120,y=190,height=40,width=140)

lab_min_txt=Label(clock,text="Min",font=("Time New Roman",20,'bold'),bg="red",fg="black")
lab_min_txt.place(x=340, y=190,height=40,width=140)

lab_sec_txt=Label(clock,text="Sec",font=("Time New Roman",20,'bold'),bg="red",fg="black")
lab_sec_txt.place(x=560,y=190,height=40,width=140)

lab_pm_txt=Label(clock,text="Am/Pm",font=("Time New Roman",20,'bold'),bg="red",fg="black")
lab_pm_txt.place(x=780,y=190,height=40,width=140)

lab_date=Label(clock,text="00",font=("Time New Roman",25,'bold'),bg="red",fg="black")
lab_date.place(x=120,y=300,height=120,width=140)
lab_month=Label(clock,text="00",font=("Time New Roman",25,'bold'),bg="red",fg="black")
lab_month.place(x=340,y=300,height=120,width=140)
lab_year=Label(clock,text="00",font=("Time New Roman",25,'bold'),bg="red",fg="black")
lab_year.place(x=560,y=300,height=120,width=140)
lab_day=Label(clock,text="00",font=("Time New Roman",25,'bold'),bg="red",fg="black")
lab_day.place(x=780,y=300,height=120,width=140)

lab_date_txt=Label(clock,text="Date",font=("Time New Roman",20,'bold'),bg="red",fg="black")
lab_date_txt.place(x=120,y=440,height=40,width=140)

lab_month_txt=Label(clock,text="Month",font=("Time New Roman",20,'bold'),bg="red",fg="black")
lab_month_txt.place(x=340,y=440,height=40,width=140)

lab_year_txt=Label(clock,text="Year",font=("Time New Roman",20,'bold'),bg="red",fg="black")
lab_year_txt.place(x=560,y=440,height=40,width=140)

lab_day_txt=Label(clock,text="Day",font=("Time New Roman",20,'bold'),bg="red",fg="black")
lab_day_txt.place(x=780,y=440,height=40,width=140)

date_time()
clock.mainloop()
