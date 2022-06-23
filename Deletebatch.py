from tkinter import *
from tkinter import messagebox
import os
import sqlite3

root=Tk()
root.geometry("1600x900")
root.title("BATCH REGISTERATION FORM")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

Canvas(root,width=300,height=300)
img=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\BG.png")
Label(root,image=img).pack()

def show_frame(frame):
    frame.tkraise()

bname=StringVar()
byear=StringVar()
intake=StringVar()

def Delete():
    global conn, cursor
    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()

    name1=bname.get()
    year1=byear.get()
    intake1=intake.get()
            
    if bname.get == "" or byear.get() == "" or intake.get == "":
        messagebox.showinfo("Error","Please complete the required field!")
    else:
        cursor.execute("DELETE FROM `batch` WHERE Batch_Name=%s) VALUES(?)",(name1))
        conn.commit()
        bname.set("")
        byear.set("")
        intake.set("")
        messagebox.showinfo("","Successfully Deleted!")
        cursor.close()
        conn.close()

def clear():
    box_content1_entry.delete(0, END)
    box_content2_entry.delete(0, END)
    intake.set("")

def back():
    filename='Batch.py'
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

Head=Label(frame1,text="Batch Deletion Form",font=("Helvetica",50,"bold"),bg="white",fg="#ff9999").place(x=400,y=20)

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

content_box_line1=Label(frame1,text="",bg="#737373").place(x=150,y=200,width=850,height=1)
content_box_line2=Label(frame1,text="",bg="#737373").place(x=150,y=650,width=850,height=1)
content_box_line3=Label(frame1,text="",bg="#737373").place(x=150,y=200,width=1,height=450)
content_box_line4=Label(frame1,text="",bg="#737373").place(x=1000,y=200,width=1,height=450)
content_box_label=Label(frame1,text="Batch Details",font=("Helvetica",13),bg="white",fg="black").place(x=160,y=188)

box_content1=Label(frame1,text="Batch Name",font=("Helvetica",13),bg="white",fg="black").place(x=320,y=300)
box_content1_line=Label(frame1,text="",bg="#737373").place(x=425,y=320,width=355,height=1)
box_content1_entry=Entry(frame1,text="",bd="0",textvariable=bname)
box_content1_entry.place(x=430,y=300,width=350)

box_content2=Label(frame1,text="Batch Year",font=("Helvetica",13),bg="white",fg="black").place(x=320,y=360)
box_content2_line=Label(frame1,text="",bg="#737373").place(x=415,y=380,width=365,height=1)
box_content2_entry=Entry(frame1,text="",bd="0",textvariable=byear)
box_content2_entry.place(x=420,y=360,width=360)

box_content3=Label(frame1,text="Batch Intake",font=("Helvetica",13),bg="white",fg="black").place(x=320,y=420)

months=['January','February','March','April','May','June','July','August','September','October','November','December'];

droplist=OptionMenu(frame1,intake, *months)
droplist.config(bd="1",font=("Helvetica",11),fg="#737373")
intake.set('Select Your Intake :')
droplist.place(x=425,y=415,width=350,height=30)

Submit_button=Button(frame1,text="Submit",font=("Lato",16),bg="#ffa31a",fg="white",command=Delete).place(x=220,y=560,width=100,height=40)
Clear_button=Button(frame1,text="Clear",font=("Lato",16),bg="#ffa31a",fg="white",command=clear).place(x=370,y=560,width=100,height=40)
Fetch_button=Button(frame1,text="Fetch Data",font=("Lato",16),bg="#ffa31a",fg="white").place(x=520,y=560,width=120,height=40)
Back_button=Button(frame1,text="Back",font=("Lato",16),bg="#ffa31a",fg="white",command=back).place(x=690,y=560,width=100,height=40)
Exit_button=Button(frame1,text="Exit",font=("Lato",16),bg="#ffa31a",fg="white",command=Exit).place(x=840,y=560,width=100,height=40)

show_frame(frame1)

root.mainloop()
