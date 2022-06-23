from tkinter import *
from tkinter import messagebox
import sqlite3
import smtplib
import random
import os

root=Tk()
root.geometry("1600x900")
root.title("Sign up")

Canvas(root,width=300,height=300)
img=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\BG.png")      
Label(root,image=img).pack()

email=StringVar()
username=StringVar()
password=StringVar()

def Database():
    global conn, cursor
    conn=sqlite3.connect('Database.db')
    cursor=conn.cursor()

def Exit():
    result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Register():
    Database()
    
    email1=email.get()
    username1=username.get()
    password1=password.get()
    
    if email.get == "" or username.get() == "" or password.get() == "" :
        messagebox.showinfo("Error","Please complete the required field!")
    else:
        cursor.execute('CREATE TABLE IF NOT EXISTS `user`(email TEXT,username TEXT,password VAR)')
        cursor.execute("SELECT * FROM `user` WHERE `username` = ?", [username.get()])
        if cursor.fetchone() is not None:
            messagebox.showinfo("Error","Username is already taken")
        else:
            cursor.execute("INSERT INTO `user` (email, username, password) VALUES(?,?,?)",(email1,username1,password1))
            conn.commit()
            email.set("")
            username.set("")
            password.set("")
            messagebox.showinfo("","Successfully Created!")
        cursor.close()
        conn.close()

def callback():
    filename='Login.py'
    os.system(filename)
    root.destroy()
    exit()

def clicked():
    Pas_entry['show']=''
    
Head=Label(root,text="A",font=("Comic Sans MS",82),bg="white").place(x=485,y=92)
Head=Label(root,text="dmin",font=("Comic Sans MS",34,"bold"),bg="white").place(x=560,y=161)
Head=Label(root,text="R",font=("Comic Sans MS",82),bg="white").place(x=685,y=94)
Head=Label(root,text="egisteration",font=("Comic Sans MS",34,"bold"),bg="white").place(x=755,y=161)

Head_Line=Label(root,text="",bg="black").place(x=500,y=230,width=514,height=2)

label_1=Label(root,text="Email",font=("Lato",14),bg="white").place(x=500,y=300)
Em_Line=Label(root,text="",bg="black").place(x=505,y=352,width=400,height=1)
Em_entry=Entry(root,bg="white",bd="0",font=("Lato",12),textvariable=email).place(x=525,y=330,width=380)

label_2=Label(root,text="Username",font=("Lato",14),bg="white").place(x=500,y=400)
User_Line=Label(root,text="",bg="black").place(x=505,y=455,width=400,height=1)
User_entry=Entry(root,bg="white",bd="0",font=("Lato",12),textvariable=username).place(x=525,y=433,width=380)

label_3=Label(root,text="Password",font=("Lato",14),bg="white").place(x=500,y=500)
Pas_Line=Label(root,text="",bg="black").place(x=505,y=555,width=400,height=1)
Pas_entry=Entry(root,bg="white",bd="0",font=("Lato",12),textvariable=password)
Pas_entry['show']='*'
Pas_entry.place(x=525,y=533,width=380)

lbl_result = Label(root, text="", font=("Lato",14)).place(x=510,y=615)

Submit_button=Button(root,text="Submit",font=("Lato",16),bg="#ffa31a",fg="white",command=Register).place(x=510,y=615,width=100)
Login_button=Button(root,text="Login",font=("Lato",16),bg="#ffa31a",fg="white",command=callback).place(x=690,y=615,width=100)
Exit_button=Button(root,text="Exit",font=("Lato",16),bg="#ffa31a",fg="white",command=Exit).place(x=870,y=615,width=100)

Mail=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\mail.png")
User=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\user.png")
Lock=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\lock.png")
Eye=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\eye.png")

Button(root,image=Mail,bd="0",bg="white").place(x=500,y=330,width=21,height=22)
Button(root,image=User,bd="0",bg="white").place(x=500,y=432,width=21,height=22)
Button(root,image=Lock,bd="0",bg="white").place(x=500,y=536,width=21,height=18)
Button(root,image=Eye,bd="0",bg="white",activebackground="white",command=clicked).place(x=875,y=525,width=30,height=30)

Description=Label(root,text="* Please enter Admin details and Submit,",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=570,y=700)
Description1=Label(root,text="Do not forget to store it in safe place,",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=590,y=725)
Description2=Label(root,text="You will need it while logging in!",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=600,y=750)

root.mainloop()
