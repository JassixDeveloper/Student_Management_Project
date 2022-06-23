from tkinter import *
from tkinter import messagebox
import os
import turtle
import time
import sqlite3

root=Tk()
root.geometry("1600x900")
root.title("COLLEGE MANAGEMENT SYSTEM")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

Canvas(root,width=300,height=300)
img=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\BG.png")
Label(root,image=img).pack()

username=StringVar()
password=StringVar()
email=StringVar()
confirm=StringVar()

first=StringVar()
last=StringVar()
DOB=StringVar()
gender=StringVar()
ad=StringVar()
no=StringVar()
department=StringVar()

def show_frame(frame):
    frame.tkraise()

def Update(event=None):
    global conn, cursor
    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()

    if username.get() == "" or password.get == "" or email.get() == "" or confirm.get == "":
        messagebox.showinfo("Error","Please complete the required field!")
    else:
        cursor.execute("SELECT * FROM `new user` WHERE `email` = ? AND `username` = ? AND `password` = ?", (email.get(), username.get(), password.get()))
        if cursor.fetchone() is not None:
            email.set("")
            username.set("")
            password.set("")
            confirm.set("")

            fname=first.get()
            lname=last.get()
            date1=DOB.get()
            gender1=gender.get()
            address=ad.get()
            contact=no.get()
            dep=department.get()

            if first.get == "" or last.get() == "" or DOB.get() == "" or gender.get() == "" or ad.get() == "" or no.get() == "":
                messagebox.showinfo("Error","Please complete the required field!")
            else:
                cursor.execute("UPDATE `employee` SET Last_Name=%s, DOB=%s, Gender=%s, Address=%s, Contact_No=%s WHERE First_Name=%s VALUES(?,?,?,?,?,?,?)",(fname,lname,date1,gender1,address,contact,dep))
                conn.commit()
                first.set("")
                last.set("")
                DOB.set("")
                gender.set("")
                ad.set("")
                no.set("")
                messagebox.showinfo("","Successfully Updated!")
        else:
            messagebox.showinfo("Error","Invalid username or password")
            if password.get() != confirm.get():
                messagebox.showinfo("Error", "Password and Confirm Password are not same", icon="warning")
            email.set("")
            username.set("")
            password.set("")
            confirm.set("")
    cursor.close()
    conn.close()

def clear():
    Box1_user_entry.delete(0, END)
    Box1_pas_entry.delete(0, END)
    Box1_email_entry.delete(0, END)
    Box1_cpas_entry.delete(0, END)
    Box2_fname_entry.delete(0, END)
    Box2_lname_entry.delete(0, END)
    DOB.set("")
    gender.set("")
    Box2_ad_entry.delete(0, END)
    Box2_no_entry.delete(0, END)

def back():
    filename='Employee.py'
    os.system(filename)
    root.destroy()
    exit()

def Exit():
    result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

frame1=Frame(root)

for frame in (frame1,):
    frame.place(x=20,y=30,width=1490,height=780)

#================== Frame
frame1_title=Label(frame1,bg="White")
frame1_title.pack(fill='both', expand=True)

Head=Label(frame1,text="Employee Updation Form",font=("Helvetica",50,"bold"),bg="white",fg="#ff9999").place(x=350,y=20)

pic_line1=Label(frame1,text="",bg="#737373").place(x=1080,y=150,width=1,height=580)
pic_line2=Label(frame1,text="",bg="#737373").place(x=1450,y=150,width=1,height=580)
pic_line3=Label(frame1,text="",bg="#737373").place(x=1080,y=730,width=370,height=1)
pic_line4=Label(frame1,text="",bg="#737373").place(x=1080,y=150,width=370,height=1)

box_label=Label(frame1,text="Developed by Bibekanand Kushwaha",font=("Helvetica",13),bg="white",fg="#737373").place(x=1125,y=665)
box_label=Label(frame1,text="Coventry ID:190352",font=("Helvetica",13),bg="white",fg="#737373").place(x=1185,y=690)

college=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\College.png")
pic_button=Button(frame1,text="",bd="0",bg="white",image=college).place(x=1100,y=150,width=330,height=250)

name=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\Name.png")
pic_button1=Button(frame1,text="",bd="0",bg="white",image=name).place(x=1100,y=300,width=330,height=150)

#================== Boxes
Box1_line1=Label(frame1,text="",bg="#737373").place(x=150,y=170,width=1,height=150)
Box1_line2=Label(frame1,text="",bg="#737373").place(x=1030,y=170,width=1,height=150)
Box1_line3=Label(frame1,text="",bg="#737373").place(x=150,y=170,width=880,height=1)
Box1_line4=Label(frame1,text="",bg="#737373").place(x=150,y=320,width=880,height=1)
Box1_label=Label(frame1,text="Account Details",font=("Helvetica",12),bg="white",fg="black").place(x=160,y=158)

Box2_line1=Label(frame1,text="",bg="#737373").place(x=150,y=365,width=1,height=240)
Box2_line2=Label(frame1,text="",bg="#737373").place(x=1030,y=365,width=1,height=240)
Box2_line3=Label(frame1,text="",bg="#737373").place(x=150,y=365,width=880,height=1)
Box2_line4=Label(frame1,text="",bg="#737373").place(x=150,y=605,width=880,height=1)
Box2_label=Label(frame1,text="Personal Details",font=("Helvetica",12),bg="white",fg="black").place(x=160,y=354)

Box3_line1=Label(frame1,text="",bg="#737373").place(x=150,y=650,width=1,height=80)
Box3_line2=Label(frame1,text="",bg="#737373").place(x=1030,y=650,width=1,height=80)
Box3_line3=Label(frame1,text="",bg="#737373").place(x=150,y=650,width=880,height=1)
Box3_line4=Label(frame1,text="",bg="#737373").place(x=150,y=730,width=880,height=1)
Box3_label=Label(frame1,text="Register Options",font=("Helvetica",12),bg="white",fg="black").place(x=160,y=638)
#================== Box1 Content
Box1_user=Label(frame1,text="Username",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=200)
Box1_pas=Label(frame1,text="Password",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=260)
Box1_user_line=Label(frame1,text="",bg="#737373").place(x=255,y=220,width=300,height=1)
Box1_pas_line=Label(frame1,text="",bg="#737373").place(x=255,y=280,width=300,height=1)
Box1_email=Label(frame1,text="Email",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=200)
Box1_cpas=Label(frame1,text="Confirm Password",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=260)
Box1_email_line=Label(frame1,text="",bg="#737373").place(x=625,y=220,width=375,height=1)
Box1_cpas_line=Label(frame1,text="",bg="#737373").place(x=710,y=280,width=290,height=1)
Box1_user_entry=Entry(frame1,text="",bd="0",textvariable=username)
Box1_user_entry.place(x=255,y=200,width=300)
Box1_pas_entry=Entry(frame1,text="",show="*",bd="0",textvariable=password)
Box1_pas_entry.place(x=255,y=260,width=300)
Box1_email_entry=Entry(frame1,text="",bd="0",textvariable=email)
Box1_email_entry.place(x=625,y=200,width=375)
Box1_cpas_entry=Entry(frame1,text="",show="*",bd="0",textvariable=confirm)
Box1_cpas_entry.place(x=710,y=260,width=290)

#================== Box2 Content
Box2_fname=Label(frame1,text="First Name",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=400)
Box2_fname_line=Label(frame1,text="",bg="#737373").place(x=260,y=420,width=295,height=1)
Box2_fname_entry=Entry(frame1,text="",bd="0",textvariable=first)
Box2_fname_entry.place(x=260,y=400,width=300)
Box2_lname=Label(frame1,text="Last Name",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=400)
Box2_lname_line=Label(frame1,text="",bg="#737373").place(x=660,y=420,width=340,height=1)
Box2_lname_entry=Entry(frame1,text="",bd="0",textvariable=last)
Box2_lname_entry.place(x=660,y=400,width=340)

Box2_DOB=Label(frame1,text="DOB",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=465)
Box2_DOB_entry=Entry(frame1,text="DD/MM/YYYY",bd="0",textvariable=DOB).place(x=220,y=470,width=335)
Box2_DOB_line=Label(frame1,text="",bg="#737373").place(x=220,y=488,width=335,height=1)

Box2_gender=Label(frame1,text="Gender",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=465)

genders=["Male","Female","Other"];

droplist=OptionMenu(frame1,gender, *genders)
droplist.config(bd="1",font=("Helvetica",11),fg="#737373")
gender.set('Select Your Gender :')
droplist.place(x=640,y=460,width=360,height=30)

Box2_ad=Label(frame1,text="Address",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=535)
Box2_ad_line=Label(frame1,text="",bg="#737373").place(x=245,y=555,width=310,height=1)
Box2_ad_entry=Entry(frame1,text="",bd="0",textvariable=ad)
Box2_ad_entry.place(x=245,y=535,width=310)
Box2_no=Label(frame1,text="Contact No.",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=535)
Box2_no_line=Label(frame1,text="",bg="#737373").place(x=660,y=555,width=340,height=1)
Box2_no_entry=Entry(frame1,text="",bd="0",textvariable=no)
Box2_no_entry.place(x=660,y=535,width=340)

#================== Box3 Content
Submit_button=Button(frame1,text="Submit",font=("Lato",16),bg="#ffa31a",fg="white",command=Update).place(x=240,y=675,width=100,height=35)
Clear_button=Button(frame1,text="Clear",font=("Lato",16),bg="#ffa31a",fg="white",command=clear).place(x=390,y=675,width=100,height=35)
Fetch_button=Button(frame1,text="Fetch Data",font=("Lato",16),bg="#ffa31a",fg="white").place(x=530,y=675,width=120,height=35)
Back_button=Button(frame1,text="Back",font=("Lato",16),bg="#ffa31a",fg="white",command=back).place(x=690,y=675,width=100,height=35)
Exit_button=Button(frame1,text="Exit",font=("Lato",16),bg="#ffa31a",fg="white",command=Exit).place(x=840,y=675,width=100,height=35)

show_frame(frame1)

root.mainloop()
