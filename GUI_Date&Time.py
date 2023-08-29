from tkinter import *
from tkinter import messagebox
import time
import datetime as dt


window = Tk()
window.title("Login")
window.geometry("475x180")
window.config(bg="silver")

label1 = Label(window, text="Username", bg="silver", font="Times 22 bold")
label1.grid(row=0, column=0)
entry1 = Entry(window, width=20, bg="white", fg="black", borderwidth=10, font="Times 22 bold")
entry1.grid(row=0, column=1)
label2 = Label(window, text="Password ", bg="silver", font="Times 22 bold")
label2.grid(row=1, column=0)
entry2 = Entry(window, width=20, bg="white", fg="white", borderwidth=10, font="Times 22 bold")
entry2.grid(row=1, column=1)

def Login():
    username = entry1.get()
    password = entry2.get()
    if (username=="tiba" and password=="000"):
        messagebox.showinfo("GUI", "Welcome to digital_clock")
        window2 = Toplevel(window)
        window2.title("Welcome")
        window2.geometry("500x150")
        window2.config(bg="silver")

        label_time = Label(window2, text="Time: ", bg="silver", font="Times 22 bold")
        label_time.grid(row=0, column=0)
        label3 = Label(window2, bg="silver", fg="blue", font="Times 22 bold")
        label3.grid(row=0, column=1)

        def Date_Time():
            time_live = time.strftime("%H:%M:%S")
            label3.config(text=time_live)
            label3.after(200, Date_Time)
        Date_Time()

        date = dt.datetime.now()
        label_date = Label(window2, text="Date: ", bg="silver", font="Times 22 bold")
        label_date.grid(row=1, column=0)
        label4 = Label(window2, text=f"{date:%A, %B %d, %Y}", bg="silver", fg="blue", font="Times 22 bold")
        label4.grid(row=1, column=1)

    elif username != "tiba":
        messagebox.showerror("Invalid", "Invalid Username")
    elif password != "000":
        messagebox.showerror("Invalid", "Invalid Password")
    window.withdraw()

button_login = Button(window, text="Login", fg="white", bg="blue", borderwidth=5, font="Times 22 bold", command=Login).grid(row=2,column=1)

window.mainloop()