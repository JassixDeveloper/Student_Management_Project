from tkinter import *
import os
from tkinter import messagebox
import sqlite3

root=Tk()
root.geometry("1600x900")
root.title("Login")

Canvas(root,width=300,height=300)
img=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\BG.png")      
Label(root,image=img).pack()

username = StringVar()
password = StringVar()

def Database():
    global conn, cursor
    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()
    
def Login(event=None):
    Database()
    if username.get() == "" or password.get() == "":
        messagebox.showinfo("Error","Please complete the required field!")
    else:
        cursor.execute("SELECT * FROM `user` WHERE `username` = ? AND `password` = ?", (username.get(), password.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            username.set("")
            password.set("")
            messagebox.showinfo(text="")
        else:
            messagebox.showinfo("Error","Invalid username or password")
            username.set("")
            password.set("")   
    cursor.close()
    conn.close()
 
def HomeWindow():
    filename='dashboard.py'
    os.system(filename)
    root.destroy()
    exit()

def forget():
    filename='Forget.py'
    os.system(filename)
    root.destroy()
    exit()

def clicked():
    Password_entry['show']=''
    
def Exit():
    root.destroy()
    exit(0)

Head=Label(root,text="A",font=("Comic Sans MS",82),bg="white").place(x=550,y=110)
Head=Label(root,text="dmin",font=("Comic Sans MS",34,"bold"),bg="white").place(x=627,y=181)
Head=Label(root,text="L",font=("Comic Sans MS",82),bg="white").place(x=745,y=110)
Head=Label(root,text="ogin",font=("Comic Sans MS",34,"bold"),bg="white").place(x=806,y=180)

Head_Line=Label(root,text="",bg="black").place(x=561,y=250,width=335,height=2)

label_1=Label(root,text="Username",font=("Lato",14),bg="white").place(x=500,y=320)
Username_Line=Label(root,text="",bg="black").place(x=505,y=375,width=400,height=1)
Username_entry=Entry(root,bg="white",bd="0",font=("Lato",12),textvariable=username).place(x=525,y=353,width=380)

label_2=Label(root,text="Password",font=("Lato",14),bg="white").place(x=500,y=420)
Password_Line=Label(root,text="",bg="black").place(x=505,y=475,width=400,height=1)
Password_entry=Entry(root,show='*',bg="white",bd="0",font=("Lato",12),textvariable=password)
Password_entry['show']='*'
Password_entry.place(x=525,y=453,width=380)

forget=Button(root,text="Forget Password?",bd="0",font=("Lato",12),fg="red",bg="white",activebackground="white",command=forget).place(x=830,y=490)
forget_Line=Label(root,text="",bg="red").place(x=835,y=516,width=121,height=1)

Submit_button=Button(root,text="Submit",font=("Lato",16),bg="#ffa31a",fg="white",command=Login).place(x=550,y=600,width=100)
Exit_button=Button(root,text="Exit",font=("Lato",16),bg="#ffa31a",fg="white",command=Exit).place(x=750,y=600,width=100)

User=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\user.png")
Lock=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\lock.png")
Eye=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\eye.png")

Button(root,image=User,bd="0",bg="white").place(x=501,y=352,width=21,height=22)
Button(root,image=Lock,bd="0",bg="white").place(x=501,y=454,width=21,height=18)
Button(root,image=Eye,bd="0",bg="white",activebackground="white",command=clicked).place(x=875,y=444,width=30,height=30)

Description=Label(root,text="* Please enter Admin Username and Password,",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=560,y=700)
Description1=Label(root,text="Then Press Submit Button",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=640,y=726)

root.mainloop()
