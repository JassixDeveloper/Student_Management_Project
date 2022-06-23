from tkinter import *
import os
from tkinter import messagebox
import sqlite3

root=Tk()
root.geometry("1600x900")
root.title("New Admin")

Canvas(root,width=300,height=300)
img=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\BG.png")      
Label(root,image=img).pack()

username = StringVar()
password = StringVar()
email = StringVar()

def Database():
    global conn, cursor
    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()

def Register():
    Database()
    
    email1=email.get()
    username1=username.get()
    password1=password.get()
    
    if email.get == "" or username.get() == "" or password.get() == "" :
        messagebox.showinfo("Error","Please complete the required field!")
    else:
        cursor.execute('CREATE TABLE IF NOT EXISTS `new user`(email TEXT,username TEXT,password VAR)')
        cursor.execute("SELECT * FROM `new user` WHERE `username` = ?", [username.get()])
        if cursor.fetchone() is not None:
            messagebox.showinfo("Error","Username is already taken")
        else:
            cursor.execute("INSERT INTO `new user` (email, username, password) VALUES(?,?,?)",(email1,username1,password1))
            conn.commit()
            email.set("")
            username.set("")
            password.set("")
            messagebox.showinfo("","Successfully Created!")
            HomeWindow()
        cursor.close()
        conn.close()
 
def HomeWindow():
    filename='AdminLogin.py'
    os.system(filename)
    root.destroy()
    exit()

def Exit():
    result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def clicked():
    Password_entry['show']=''

def Back():
    filename='Employee.py'
    os.system(filename)
    root.destroy()
    exit()

Head=Label(root,text="A",font=("Comic Sans MS",60),bg="white").place(x=515,y=100)
Head=Label(root,text="dd",font=("Comic Sans MS",34),bg="white").place(x=575,y=140)
Head=Label(root,text="N",font=("Comic Sans MS",60),bg="white").place(x=644,y=100)
Head=Label(root,text="ew",font=("Comic Sans MS",34),bg="white").place(x=715,y=140)
Head=Label(root,text="A",font=("Comic Sans MS",60),bg="white").place(x=790,y=100)
Head=Label(root,text="dmin",font=("Comic Sans MS",34),bg="white").place(x=845,y=140)

Head_Line=Label(root,text="",bg="black").place(x=515,y=205,width=440,height=2)

label_1=Label(root,text="Email",font=("Lato",14),bg="white").place(x=500,y=280)
Email_Line=Label(root,text="",bg="black").place(x=505,y=335,width=400,height=1)
Email_entry=Entry(root,bg="white",bd="0",font=("Lato",12),textvariable=email).place(x=525,y=311,width=380)

label_2=Label(root,text="Username",font=("Lato",14),bg="white").place(x=500,y=370)
Username_Line=Label(root,text="",bg="black").place(x=505,y=435,width=400,height=1)
Username_entry=Entry(root,bg="white",bd="0",font=("Lato",12),textvariable=username).place(x=525,y=411,width=380)

label_3=Label(root,text="Password",font=("Lato",14),bg="white").place(x=500,y=480)
Password_Line=Label(root,text="",bg="black").place(x=505,y=535,width=400,height=1)
Password_entry=Entry(root,show='*',bg="white",bd="0",font=("Lato",12),textvariable=password)
Password_entry['show']='*'
Password_entry.place(x=525,y=511,width=380)

Submit_button=Button(root,text="Submit",font=("Lato",16),bg="#ffa31a",fg="white",command=Register).place(x=510,y=600,width=120)
Back_button=Button(root,text="Back",font=("Lato",16),bg="#ffa31a",fg="white",command=Back).place(x=685,y=600,width=120)
Exit_button=Button(root,text="Exit",font=("Lato",16),bg="#ffa31a",fg="white",command=Exit).place(x=860,y=600,width=120)

Mail=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\mail.png")
User=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\user.png")
Lock=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\lock.png")
Eye=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\eye.png")

Button(root,image=Mail,bd="0",bg="white").place(x=501,y=312,width=21,height=22)
Button(root,image=User,bd="0",bg="white").place(x=501,y=412,width=21,height=22)
Button(root,image=Lock,bd="0",bg="white").place(x=501,y=514,width=21,height=18)
Button(root,image=Eye,bd="0",bg="white",activebackground="white",command=clicked).place(x=875,y=505,width=30,height=30)

Description=Label(root,text="* Please enter Admin details and Submit,",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=560,y=700)
Description=Label(root,text="Do not forget to store it in safe place,",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=575,y=725)
Description1=Label(root,text="You will need it while logging in!",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=596,y=750)

root.mainloop()
