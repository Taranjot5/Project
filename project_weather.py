from tkinter import *
import requests
from datetime import *
from tkinter import messagebox

root=Tk()
root.title("weather app")
root.geometry("900x900")

# root.resizeable(False,False)

def getweather():

    try:
        city=textfield.get()
        api_key="e7d825140e3cc2bc2f59652adcbdb835"

        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid="
        final_url = weather_url + api_key
        weather_data = requests.get(final_url).json()
        # print(weather_data)

        # print(weather_data)
        wind_speed=weather_data["wind"]['speed']
        hmdt=weather_data['main']['humidity']
        description=weather_data['weather'][0]['description']
        pressur=weather_data['main']['pressure']
        main=weather_data['weather'][0]['main']
        temp=int(((weather_data['main']['temp'])-273.15))
        date_time=datetime.now().strftime("%d%b%Y   %H:%M")

        w.config(text=(wind_speed))
        h.config(text=(hmdt))
        d.config(text=(description))
        p.config(text=(pressur))
        label6.config(text=(date_time))
        c.config(text=(main,"|","feels","like",temp,"°"))
        t.config(text=(temp,"°"))

    except Exception:
        messagebox.showerror("weather app","City not found")


textfield=Entry(root,justify="center",width=17,font=("poppin",25,"bold"))
textfield.place(x=290,y=20)
textfield.insert(0,"enter the location")
textfield.configure(state=DISABLED)

def on_click(event):
    textfield.configure(state=NORMAL)
    textfield.delete(0,END)

    # make the callback only work once
    textfield.unbind('<Button-1>',on_click_id)

on_click_id=textfield.bind('<Button-1>',on_click)

search_icon=PhotoImage(file="glass.png")

myimage_search_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",command=getweather)
myimage_search_icon.place(x=620,y=26)


#logo
logo_image=PhotoImage(file="icon.png")
logo=Label(image=logo_image)
logo.place(x=300,y=100)

#label
label1=Label(root,text="wind",font=("helvetica",15,"bold"))
label1.place(x=110,y=470)

label2=Label(root,text="humidity",font=("helvetica",15,"bold"))
label2.place(x=250,y=470)

label3 = Label(root, text="pressure", font=("helvetica", 15, "bold"))
label3.place(x=430, y=470)

label4 = Label(root, text="description", font=("helvetica", 15, "bold"))
label4.place(x=650, y=470)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=630,y=200)
c = Label(font=("arial", 15, "bold"))
c.place(x=600, y=300)

w = Label(text="...", font=("arial", 20, "bold"))
w.place(x=120,y=500)
h = Label(text="...", font=("arial", 20, "bold"))
h.place(x=280,y=500)
p = Label(text="...", font=("arial", 20, "bold"))
p.place(x=450, y=500)
d = Label(text="...", font=("arial", 20, "bold"))
d.place(x=670, y=500)

#date_time
label5 = Label(text="current date & time",font=("arial", 15, "bold"))
label5.place(x=50,  y=180)
label6 = Label(font=("arial",15,"bold"))
label6.place(x=50, y=230)


root.mainloop()