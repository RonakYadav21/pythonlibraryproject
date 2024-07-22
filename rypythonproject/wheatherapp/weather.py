from tkinter  import * 
import tkinter as tk
#from PIL import Image, ImageTk
import datetime 
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
import requests
import json
import pytz

root=Tk()
root.title("WEATHER APP")
root.geometry('1200x900')
root.config(bg="lightblue")
#icon

def getweather():
     city= textfield.get()
     goelocator=Nominatim(user_agent="geoapiExerxcise")
     location=goelocator.geocode(city)
    
   # to find timezpone 
     obj=TimezoneFinder()
     result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
     time_zone.config(text=result)
     long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

     local_time=datetime.datetime.now()
     currenttime=local_time.strftime("%I:%M %p")
     clock.config(text=currenttime)


#weathher 
     api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+ "&lon="+str(location.longitude)+"units=metric&exclude=hourly,daily&appid={011f44d90229ff7b472d49e5580d1833}"
     json_data=requests.get(api)
     data=json_data.json()
     main=data['main']

            
#current
     temp= main['temp']
     humidity=json_data['current']['humidity']
     pressure=json_data['current']['pressure']
     wind_speed=json_data['current']['wind_speed']
     description=json_data['curretn'][0]['description']
     lab6.config(text=(temp,"°C"))
     
# create an instance of photoimage by passing file path as arguments
image_icon=PhotoImage(file="D:\\rypythonproject\\wheatherapp\\cloud.png")
#set the icon of the tkinter window
root.iconphoto(False,image_icon)
#s_image=PhotoImage(file="wheatherapp/serachbar.png")
search_label=Label(root,bg='black').place(x=380,y=150, height=30,width=300)
seach_icon=PhotoImage(file="D:\\rypythonproject\\wheatherapp\\searchicon.png")
s_icon=Button(root,image=seach_icon, cursor='hand2',borderwidth=0 ,command=getweather).place(x=660,y=151, width=20,height=28)

outer_lab=Label(root,bg='black')
outer_lab.pack()
outer_lab.place(x=70,y=150,height=120,width=200)
lab1= Label(root,text="Temperature ", bg="black" ,fg='white')
lab1.place(x=73,y=155)
lab2=Label(root,text=" Humidity",bg='black',fg='white')
lab2.place(x=73,y=175)
lab3=Label(root,text="Pressure",bg='black',fg='white')
lab3.place(x=73,y=195)
lab4=Label(root,text=" Wind Speed",bg='black',fg='white')
lab4.place(x=73,y=215)
lab5=Label(root,text=" Description",bg='black',fg='white')
lab5.place(x=73,y=235)

lab6=Label(root,bg='black',fg='white')
lab6.place(x=180,y=155)
lab7=Label(root,bg='black',fg='white')
lab7.place(x=180,y=175)
lab8=Label(root,text=" ",bg='black',fg='white')
lab8.place(x=180,y=195)
lab9=Label(root,text=" ",bg='black',fg='white')
lab9.place(x=180,y=215)
lab10=Label(root,text=" ",bg='black',fg='white')
lab10.place(x=180,y=235)

textfield=Entry(root,border=0,fg="white",bg='black',font=('poppins',15,'bold'),width=15,justify='center')
textfield.place(x=430,y=150 ,width=220,height=30)

frame=Frame(root,bg='black',height=250,width=1500)
frame.pack(side=BOTTOM)
fristbox=PhotoImage(file="D:\\rypythonproject\\wheatherapp\\horizontalrect.png")
f_box=Label(frame,image=fristbox ,bg='black').place(x=30, y=25) 

secondbox=PhotoImage(file="D:\\rypythonproject\\wheatherapp\\rect.png")
s_box=Label(frame,image=secondbox,bg='black').place(x=320,y=25)
thirdbox=PhotoImage(file="D:\\rypythonproject\\wheatherapp\\rect.png ")
t_box=Label(frame,image=thirdbox,bg="black").place(x=470,y=25)
fourthbox=PhotoImage(file="D:\\rypythonproject\\wheatherapp\\rect.png")
f_box=Label(frame,image=fourthbox,bg="black").place(x=620,y=25)

fivethbox=PhotoImage(file="D:\\rypythonproject\\wheatherapp\\rect.png")
fi_box=Label(frame,image=fourthbox,bg="black").place(x=770,y=25)

fivethbox=PhotoImage(file="D:\\rypythonproject\\wheatherapp\\rect.png")
fi_box=Label(frame,image=fourthbox,bg="black").place(x=920,y=25)
sixbox=PhotoImage(file="D:\\rypythonproject\\wheatherapp\\rect.png")
Label(frame,image=fourthbox,bg="black").place(x=1070,y=30)

#clock
clock=Label(root,text=" ",font=("helvetica",30,'bold'),fg='white',bg='lightblue')
clock.place(x=70,y=30)

#timezone
time_zone=Label(root,text=" ",font=("helvetica",20,'bold'),fg='white',bg='lightblue')
time_zone.place(x=1000,y=20)

long_lat=Label(root,text=" ",font=("helvetica",15,'bold'),fg='white',bg='lightblue')
long_lat.place(x=1000,y=80)



root.mainloop()



