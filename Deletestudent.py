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
g=StringVar()
ad=StringVar()
no=StringVar()
s=StringVar()
c=StringVar()
b=StringVar()
se=StringVar()

def show_frame(frame):
    frame.tkraise()

def Delete(event=None):
    global conn, cursor
    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()

    if username.get() == "" or password.get == "" or email.get() == "" or confirm.get == "":
        messagebox.showinfo("Error","Please complete the required field!")
    else:
        cursor.execute("SELECT * FROM `user` WHERE `email` = ? AND `username` = ? AND `password` = ?", (email.get(), username.get(), password.get()))
        if cursor.fetchone() is not None:
            email.set("")
            username.set("")
            password.set("")
            confirm.set("")

            fname=first.get()
            lname=last.get()
            date1=DOB.get()
            gender1=g.get()
            address=ad.get()
            contact=no.get()
            shift1=s.get()
            course1=c.get()
            bat=b.get()
            section1=se.get()
        
            if first.get == "" or last.get() == "" or DOB.get() == "" or g.get() == "" or ad.get() == "" or no.get() == "" or s.get() == "" or c.get() == "" or b.get() == "" or se.get() == "":
                messagebox.showinfo("Error","Please complete the required field!")
            else:
                cursor.execute("DELETE FROM `student` WHERE First_Name=%s, Last_Name=%s VALUES(?,?)",(fname,lname))
                conn.commit()
                first.set("")
                last.set("")
                DOB.set("")
                g.set("")
                ad.set("")
                no.set("")
                s.set("")
                c.set("")
                b.set("")
                se.set("")
                messagebox.showinfo("","Successfully Created!")
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

def back():
    filename='Student.py'
    os.system(filename)
    root.destroy()
    exit()

def clear():
   e1.delete(0, END)
   e2.delete(0, END)
   e3.delete(0, END)
   e4.delete(0, END)
   e5.delete(0, END)
   e6.delete(0, END)
   e7.delete(0, END)
   e8.delete(0, END)
   DOB.set("")
   g.set("")
   s.set("")
   c.set("")
   se.set("")
   b.set("")
   
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

Head=Label(frame1,text="Student Deletion Form",font=("Helvetica",50,"bold"),bg="white",fg="#ff9999").place(x=400,y=20)

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

Box2_line1=Label(frame1,text="",bg="#737373").place(x=150,y=365,width=1,height=280)
Box2_line2=Label(frame1,text="",bg="#737373").place(x=1030,y=365,width=1,height=280)
Box2_line3=Label(frame1,text="",bg="#737373").place(x=150,y=365,width=880,height=1)
Box2_line4=Label(frame1,text="",bg="#737373").place(x=150,y=645,width=880,height=1)
Box2_label=Label(frame1,text="Personal Details",font=("Helvetica",12),bg="white",fg="black").place(x=160,y=354)

Box3_line1=Label(frame1,text="",bg="#737373").place(x=150,y=670,width=1,height=60)
Box3_line2=Label(frame1,text="",bg="#737373").place(x=1030,y=670,width=1,height=60)
Box3_line3=Label(frame1,text="",bg="#737373").place(x=150,y=670,width=880,height=1)
Box3_line4=Label(frame1,text="",bg="#737373").place(x=150,y=730,width=880,height=1)
Box2_label=Label(frame1,text="Register Options",font=("Helvetica",12),bg="white",fg="black").place(x=160,y=658)
#================== Box1 Content
Box1_user=Label(frame1,text="Username",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=200)
Box1_pas=Label(frame1,text="Password",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=260)
Box1_user_line=Label(frame1,text="",bg="#737373").place(x=255,y=220,width=300,height=1)
Box1_pas_line=Label(frame1,text="",bg="#737373").place(x=255,y=280,width=300,height=1)
Box1_email=Label(frame1,text="Email",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=200)
Box1_cpas=Label(frame1,text="Confirm Password",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=260)
Box1_email_line=Label(frame1,text="",bg="#737373").place(x=625,y=220,width=375,height=1)
Box1_cpas_line=Label(frame1,text="",bg="#737373").place(x=710,y=280,width=290,height=1)
e1=Entry(frame1,text="",bd="0",textvariable=username)
e1.place(x=255,y=200,width=300)
e2=Entry(frame1,show='*',text="",bd="0",textvariable=password)
e2.place(x=255,y=260,width=300)
e3=Entry(frame1,text="",bd="0",textvariable=email)
e3.place(x=625,y=200,width=375)
e4=Entry(frame1,show='*',text="",bd="0",textvariable=confirm)
e4.place(x=710,y=260,width=290)

#================== Box2 Content
Box2_fname=Label(frame1,text="First Name",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=400)
Box2_fname_line=Label(frame1,text="",bg="#737373").place(x=260,y=420,width=295,height=1)
e5=Entry(frame1,text="",bd="0",textvariable=first)
e5.place(x=260,y=400,width=300)
Box2_lname=Label(frame1,text="Last Name",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=400)
Box2_lname_line=Label(frame1,text="",bg="#737373").place(x=660,y=420,width=340,height=1)
e6=Entry(frame1,text="",bd="0",textvariable=last)
e6.place(x=660,y=400,width=340)

Box2_DOB=Label(frame1,text="DOB",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=445)
Box2_DOB_entry=Entry(frame1,text="DD/MM/YYYY",bd="0",textvariable=DOB).place(x=220,y=450,width=335)
Box2_DOB_line=Label(frame1,text="",bg="#737373").place(x=220,y=468,width=335,height=1)

Box2_gender=Label(frame1,text="Gender",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=445)

genders=['Male','Female','Other'];

droplist=OptionMenu(frame1,g, *genders)
droplist.config(bd="1",font=("Helvetica",11),fg="#737373")
g.set('Select Your Gender :')
droplist.place(x=640,y=440,width=365,height=30)

Box2_ad=Label(frame1,text="Address",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=495)
Box2_ad_line=Label(frame1,text="",bg="#737373").place(x=245,y=515,width=310,height=1)
e7=Entry(frame1,text="",bd="0",textvariable=ad)
e7.place(x=245,y=495,width=310)
Box2_no=Label(frame1,text="Contact No.",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=495)
Box2_no_line=Label(frame1,text="",bg="#737373").place(x=660,y=515,width=340,height=1)
e8=Entry(frame1,text="",bd="0",textvariable=no)
e8.place(x=660,y=495,width=340)

Box2_shift=Label(frame1,text="Shift",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=545)

shifts=['Morning','Afternoon','Evening'];

droplist=OptionMenu(frame1,s, *shifts)
droplist.config(width=3,bd="1",font=("Helvetica",11),fg="#737373")
s.set('Select Your Shift :')
droplist.place(x=240,y=540,width=315,height=30)

Box2_batch=Label(frame1,text="Batch",font=("Helvetica",12),bg="white",fg="black").place(x=170,y=595)

batch=[2021,2022,2023,2024,2025,2026];

droplist=OptionMenu(frame1,b, *batch)
droplist.config(bd="1",font=("Helvetica",11),fg="#737373")
b.set('Select Your Batch : ')
droplist.place(x=240,y=590,width=315,height=30)

Box2_ce=Label(frame1,text="Course Enrolled",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=545)

courses=['B.com','B.A.','B.Tech','B.CA','M.com','M.A.','M.Tech','M.CA'];

droplist=OptionMenu(frame1,c, *courses)
droplist.config(bd="1",font=("Helvetica",11),fg="#737373")
c.set('Select Your Course : ')
droplist.place(x=695,y=540,width=315,height=30)

Box2_section=Label(frame1,text="Section",font=("Helvetica",12),bg="white",fg="black").place(x=570,y=595)

sections=['A','B','C','D','E','F'];

droplist=OptionMenu(frame1,se, *sections)
droplist.config(width=3,bd="1",font=("Helvetica",11),fg="#737373")
se.set('Select Your Section : ')
droplist.place(x=695,y=590,width=315,height=30)

#================== Box3 Content
Submit_button=Button(frame1,text="Submit",font=("Lato",16),bg="#ffa31a",fg="white",command=Delete).place(x=240,y=685,width=100,height=35)
Clear_button=Button(frame1,text="Clear",font=("Lato",16),bg="#ffa31a",fg="white",command=clear).place(x=390,y=685,width=100,height=35)
Fetch_button=Button(frame1,text="Fetch Data",font=("Lato",16),bg="#ffa31a",fg="white").place(x=530,y=685,width=120,height=35)
Back_button=Button(frame1,text="Back",font=("Lato",16),bg="#ffa31a",fg="white",command=back).place(x=690,y=685,width=100,height=35)
Exit_button=Button(frame1,text="Exit",font=("Lato",16),bg="#ffa31a",fg="white",command=Exit).place(x=840,y=685,width=100,height=35)

show_frame(frame1)

root.mainloop()
