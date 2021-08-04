from tkinter import *
from tkinter import messagebox
from api_data import Weather_Data

def weather_data():
 if loc_entry.get == "" or unit_entry.get() == "":
        messagebox.showerror(title="NO DATA",message="Don't leave any field empty")
 else:

    try:
        loc = loc_entry.get()
        formatted_loc = loc.lower()
        u = unit_entry.get()
        formatted_u = u.lower()
        weather = Weather_Data(formatted_loc,formatted_u)
    except:
        messagebox.showerror(title="404",message="Please enter details validly\n\nOnly enter city or state name.\n\n"
                                                 "units: metric or imperial only")
    else:

     if formatted_u == "metric":
      messagebox.showinfo(title="Weather report",message=f"Temperature in {formatted_loc} is {weather.temp()} degree "
                                                        f"celsius.\n\n"
                                                       f"The weather currently is {weather.atmosphere()}")
     else:
        messagebox.showinfo(title="Weather report",
                            message=f"Temperature in {formatted_loc} is {weather.temp()} degree "
                                    f"fahrenheit.\n\n"
                                    f"The weather currently is {weather.atmosphere()}")



# -----------------------------------------------UI------------------------------------------- #
root = Tk()
root.title("WEATHER APP")
root.config(padx=50,pady=50,bg="white")
# ----------------------labels------------------ #
title = Label(text="LIVE WEATHER",font=("Comic Sans MS",20,"bold"),bg="white")
title.grid(row=0,column=1,pady=50)
location = Label(text="Enter Location: ",bg="white")
location.grid(row=1,column=0,pady=10)
unit = Label(text="Enter units: ",bg="white")
unit.grid(row=2,column=0)
# -----------------------------------entry------------------------ #
loc_entry = Entry(width=35)
loc_entry.focus()
loc_entry.grid(row=1,column=1,pady=10)
unit_entry = Entry(width=35)

unit_entry.grid(row=2,column=1)
# ----------------------button----------------------------- #
check = Button(text="Check weather",bg="white",font=("Comic Sans MS",10,"normal"),command=weather_data)
check.grid(row=3,column=1,pady=20)

root.mainloop()
