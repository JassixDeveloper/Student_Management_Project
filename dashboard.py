from tkinter import *
from tkinter import messagebox
import os
import time
import datetime as dt
import sqlite3
from tkinter import ttk

def show_frame(frame):
    frame.tkraise()

def logout():
    result = messagebox.askquestion('System', 'Are you sure you want to Log Out?', icon="warning")
    if result == 'yes':
        filename='Login.py'
        os.system(filename)

def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   Time.config(text=text_input)
   Time.after(200, digitalclock)

def call():
    result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Update():
    email=e1.get()
    password=e2.get()
    User=u_entry.get()
    conn=sqlite3.connect('Admin Registered.db')

    if e1.get == "" or e2.get() == "" or e3.get() == "" :
        messagebox.showinfo("Error","Please complete the required field!")
    else:
        cursor=conn.cursor()
        up="Update `user` set password='%s' WHERE email='%s'"%(password,email)
        cursor.execute(up)
        conn.commit()
        messagebox.showinfo("Information","Record Updated")
        return()

def s_update(rows):
    view_student_tree.delete(*view_student_tree.get_children())
    for i in rows:
        view_student_tree.insert('','end',values=i)

def e_update(rows):
    view_employee_tree.delete(*view_employee_tree.get_children())
    for i in rows:
        view_employee_tree.insert('','end',values=i)

def c_update(rows):
    view_course_tree.delete(*view_course_tree.get_children())
    for i in rows:
        view_course_tree.insert('','end',values=i)

def d_update(rows):
    view_department_tree.delete(*view_department_tree.get_children())
    for i in rows:
        view_department_tree.insert('','end',values=i)

def stud():
    filename='Student.py'
    os.system(filename)
    root.destroy()
    exit()
    
def emp():
    filename='Employee.py'
    os.system(filename)
    root.destroy()
    exit()
    
def dep():
    filename='Department.py'
    os.system(filename)
    root.destroy()
    exit()
    
def cou():
    filename='Course.py'
    os.system(filename)
    root.destroy()
    exit()
    
def sec():
    filename='Section.py'
    os.system(filename)
    root.destroy()
    exit()
    
def bat():
    filename='Batch.py'
    os.system(filename)
    root.destroy()
    exit()
    
root=Tk()
root.geometry("1600x900")
root.title("Dashboard")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

Canvas(root,width=300,height=300)
img=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\BG1.png")
Label(root,image=img).pack()

global conn, cursor
conn=sqlite3.connect('Database.db')
cursor=conn.cursor()

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)

password=StringVar()
email=StringVar()

for frame in (frame1, frame2, frame3, frame4,):
    frame.place(x=210,y=162,width=1250,height=650)

#==================Home Frame
frame1_title=Label(frame1,bg="#fbca90")
frame1_title.pack(fill='both', expand=True)

c1=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\4.png")

frame1_title_button4=Button(frame1,text="",bd="0",bg="#fbca90",activebackground="white",image=c1).place(x=675,y=355,width=550,height=270)
frame1_title_button3=Button(frame1,text="",bd="0",bg="white",activebackground="white").place(x=40,y=355,width=550,height=270)
frame1_title_button2=Button(frame1,text="",bd="0",bg="white",activebackground="white").place(x=675,y=40,width=550,height=270)
frame1_title_button1=Button(frame1,text="",bd="0",bg="white",activebackground="white").place(x=40,y=40,width=550,height=270)

frame1_title_button3_label=Label(frame1,text="Total",bd="0",bg="white",fg="#ff9999",font=("Helvetica",55,"bold")).place(x=210,y=365)
frame1_title_button3_label=Label(frame1,text="0",bd="0",bg="white",fg="#ff9999",font=("Helvetica",55,"bold")).place(x=275,y=450)
frame1_title_button3_label=Label(frame1,text="Departments",bd="0",bg="white",fg="#ff9999",font=("Helvetica",55,"bold")).place(x=90,y=530)

frame1_title_button2_label=Label(frame1,text="Total",bd="0",bg="white",fg="#ff9999",font=("Helvetica",55,"bold")).place(x=850,y=45)
frame1_title_button2_label=Label(frame1,text="0",bd="0",bg="white",fg="#ff9999",font=("Helvetica",55,"bold")).place(x=920,y=125)
frame1_title_button2_label=Label(frame1,text="Employees",bd="0",bg="white",fg="#ff9999",font=("Helvetica",55,"bold")).place(x=750,y=210)

frame1_title_button1_label=Label(frame1,text="Total",bd="0",bg="white",fg="#ff9999",font=("Helvetica",55,"bold")).place(x=210,y=50)
frame1_title_button1_label=Label(frame1,text="0",bd="0",bg="white",fg="#ff9999",font=("Helvetica",55,"bold")).place(x=275,y=135)
frame1_title_button1_label=Label(frame1,text="Students",bd="0",bg="white",fg="#ff9999",font=("Helvetica",55,"bold")).place(x=145,y=215)

#==================Manage Frame
c2=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\Manage_Pic.png")

frame2_title=Label(frame2, image=c2)
frame2_title.pack(fill='both', expand=True)

Student=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\Student.png")
Employee=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\Employee.png")
Department=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\Department.png")
Course=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\Course.png")
Section=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\Section.png")
Batch=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\Batch.png")

Student_btn=Button(frame2,text="",bd="0",image=Student,bg="white",activebackground="white",command=stud).place(x=209,y=150,width=110,height=100)
Employee_btn=Button(frame2,text="",bd="0",image=Employee,bg="white",activebackground="white",command=emp).place(x=559,y=150,width=110,height=100)
Department_btn=Button(frame2,text="",bd="0",image=Department,bg="white",activebackground="white",command=dep).place(x=918,y=150,width=110,height=100)
Course_btn=Button(frame2,text="",bd="0",image=Course,bg="white",activebackground="white",command=cou).place(x=208,y=379,width=110,height=100)
Section_btn=Button(frame2,text="",bd="0",image=Section,bg="white",activebackground="white",command=sec).place(x=559,y=379,width=110,height=100)
Batch_btn=Button(frame2,text="",bd="0",image=Batch,bg="white",activebackground="white",command=bat).place(x=916,y=380,width=110,height=100)

Student_label=Label(frame2,text="Student",bg="white",fg="#ff9999",font=("Helvetica",18)).place(x=218,y=248)
Employee_label=Label(frame2,text="Employee",bg="white",fg="#ff9999",font=("Helvetica",18)).place(x=557,y=248)
Department_label=Label(frame2,text="Department",bg="white",fg="#ff9999",font=("Helvetica",18)).place(x=907,y=245)
Course_label=Label(frame2,text="Course",bg="white",fg="#ff9999",font=("Helvetica",18)).place(x=220,y=475)
Section_label=Label(frame2,text="Section",bg="white",fg="#ff9999",font=("Helvetica",18)).place(x=570,y=475)
Batch_label=Label(frame2,text="Batch",bg="white",fg="#ff9999",font=("Helvetica",18)).place(x=940,y=480)

#==================View Frame
frame3_title=Label(frame3,bg="white")
frame3_title.pack(fill='both', expand=True)

# ========================================================================
# ============================Displaying Student Information==============
# ========================================================================

student_view_label = Label(frame3, text="View Students Information ", bg="white", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
student_view_label.place(x=170, y=6)

view_student_frame = Frame(frame3, bg="white")
view_student_frame.place(x=10, y=40, height=250, width=575)

style = ttk.Style()
style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="red")
style.configure("Treeview", font=('yu gothic ui', 9, "bold"), foreground="#f29b0f")

scroll_y = Scrollbar(view_student_frame, orient=VERTICAL)
scroll_x = Scrollbar(view_student_frame, orient=HORIZONTAL)
view_student_tree = ttk.Treeview(view_student_frame,
                                        columns=(
                                            "STUDENT ID", "STUDENT NAME", "PHONE NO.", "COURSE ENROLLED"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=view_student_tree.xview)
scroll_y.config(command=view_student_tree.yview)

# ==========================TreeView Heading====================
view_student_tree.heading("STUDENT ID", text="STUDENT ID")
view_student_tree.heading("STUDENT NAME", text="STUDENT NAME")
view_student_tree.heading("PHONE NO.", text="PHONE NO.")
view_student_tree.heading("COURSE ENROLLED", text="COURSE ENROLLED")
view_student_tree["show"] = "headings"

# ==========================TreeView Column====================
view_student_tree.column("STUDENT ID", width=150)
view_student_tree.column("STUDENT NAME", width=150)
view_student_tree.column("PHONE NO.", width=100)
view_student_tree.column("COURSE ENROLLED", width=150)
view_student_tree.pack(fill=BOTH, expand=1)

query="SELECT Student_ID,First_Name,Contact_No,Course FROM `student`"
cursor.execute(query)
rows=cursor.fetchall()
s_update(rows)

# ========================================================================
# =========================Displaying instructor Information==============
# ========================================================================

view_employee_frame = Frame(frame3, bg="white")
view_employee_frame.place(x=640, y=40, height=250, width=575)

employee_view_label = Label(frame3, text="View Employees Information ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
employee_view_label.place(x=770, y=6)

scroll_y_e = Scrollbar(view_employee_frame, orient=VERTICAL)
scroll_x_e = Scrollbar(view_employee_frame, orient=HORIZONTAL)
view_employee_tree = ttk.Treeview(view_employee_frame,
                                        columns=(
                                            "EMPLOYEE ID", "EMPLOYEE NAME", "PHONE NO", "DEPARTMENT"),
                                        xscrollcommand=scroll_x_e.set, yscrollcommand=scroll_y_e.set)
scroll_x_e.pack(side=BOTTOM, fill=X)
scroll_y_e.pack(side=RIGHT, fill=Y)
scroll_x_e.config(command=view_employee_tree.xview)
scroll_y_e.config(command=view_employee_tree.yview)

# ==========================TreeView Heading====================
view_employee_tree.heading("EMPLOYEE ID", text="EMPLOYEE ID")
view_employee_tree.heading("EMPLOYEE NAME", text="EMPLOYEE NAME")
view_employee_tree.heading("PHONE NO", text="PHONE NO")
view_employee_tree.heading("DEPARTMENT", text="DEPARTMENT")
view_employee_tree["show"] = "headings"

# ==========================TreeView Column====================
view_employee_tree.column("EMPLOYEE ID", width=150)
view_employee_tree.column("EMPLOYEE NAME", width=150)
view_employee_tree.column("PHONE NO", width=100)
view_employee_tree.column("DEPARTMENT", width=100)
view_employee_tree.pack(fill=BOTH, expand=1)

query="SELECT Employee_ID,First_Name,Contact_No,Department FROM `employee`"
cursor.execute(query)
rows=cursor.fetchall()
e_update(rows)

# ========================================================================
# =========================Displaying Course Information==============
# ========================================================================

view_course_frame = Frame(frame3, bg="white")
view_course_frame.place(x=10, y=360, height=250, width=575)

course_view_label = Label(frame3, text="View Course Information ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
course_view_label.place(x=170, y=310)

scroll_y_e = Scrollbar(view_course_frame, orient=VERTICAL)
scroll_x_e = Scrollbar(view_course_frame, orient=HORIZONTAL)
view_course_tree = ttk.Treeview(view_course_frame,
                                        columns=(
                                            "COURSE ID", "COURSE NAME", "COURSE DURATION", "COURSE CREDIT"),
                                        xscrollcommand=scroll_x_e.set, yscrollcommand=scroll_y_e.set)
scroll_x_e.pack(side=BOTTOM, fill=X)
scroll_y_e.pack(side=RIGHT, fill=Y)
scroll_x_e.config(command=view_course_tree.xview)
scroll_y_e.config(command=view_course_tree.yview)

# ==========================TreeView Heading====================
view_course_tree.heading("COURSE ID", text="COURSE ID")
view_course_tree.heading("COURSE NAME", text="COURSE NAME")
view_course_tree.heading("COURSE DURATION", text="COURSE DURATION")
view_course_tree.heading("COURSE CREDIT", text="COURSE CREDIT")
view_course_tree["show"] = "headings"

# ==========================TreeView Column====================
view_course_tree.column("COURSE ID", width=50)
view_course_tree.column("COURSE NAME", width=150)
view_course_tree.column("COURSE DURATION", width=100)
view_course_tree.column("COURSE CREDIT", width=100)
view_course_tree.pack(fill=BOTH, expand=1)

query="SELECT Course_ID,Course_Name,Course_Duration,Course_Credit FROM `course`"
cursor.execute(query)
rows=cursor.fetchall()
c_update(rows)

# ========================================================================
# =========================Displaying Department Information==============
# ========================================================================

view_department_frame = Frame(frame3, bg="white")
view_department_frame.place(x=640, y=360, height=250, width=575)

department_view_label = Label(frame3, text="View Department Information ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
department_view_label.place(x=770, y=310)

scroll_y_e = Scrollbar(view_department_frame, orient=VERTICAL)
scroll_x_e = Scrollbar(view_department_frame, orient=HORIZONTAL)
view_department_tree = ttk.Treeview(view_department_frame,
                                            columns=(
                                                "DEPARTMENT ID", "DEPARTMENT NAME", "DEPARTMENT CODE"),
                                            xscrollcommand=scroll_x_e.set, yscrollcommand=scroll_y_e.set)
scroll_x_e.pack(side=BOTTOM, fill=X)
scroll_y_e.pack(side=RIGHT, fill=Y)
scroll_x_e.config(command=view_department_tree.xview)
scroll_y_e.config(command=view_department_tree.yview)

# ==========================TreeView Heading====================
view_department_tree.heading("DEPARTMENT ID", text="DEPARTMENT ID")
view_department_tree.heading("DEPARTMENT NAME", text="DEPARTMENT NAME")
view_department_tree.heading("DEPARTMENT CODE", text="DEPARTMENT CODE")
view_department_tree["show"] = "headings"

# ==========================TreeView Column====================
view_department_tree.column("DEPARTMENT ID", width=50)
view_department_tree.column("DEPARTMENT NAME", width=150)
view_department_tree.column("DEPARTMENT CODE", width=100)
view_department_tree.pack(fill=BOTH, expand=1)

query="SELECT Department_ID,Department_Code,Department_Name FROM `department`"
cursor.execute(query)
rows=cursor.fetchall()
d_update(rows)

#==================Setting Frame
frame4_title=Label(frame4,bg='#fbca90')
frame4_title.pack(fill='both', expand=True)

f4=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\frame4.png")
frame4_img=Button(frame4,text="",bd="0",bg="#fbca90",activebackground="#fbca90",image=f4).place(x=0,y=0,width=1250,height=650)

label=Label(frame4,text="Change Password",bg="white",fg="black",font=("Helvetica",28)).place(x=435,y=55)
line=Label(frame4,text="",bg="black").place(x=447,y=105,width=290,height=1)

u=Label(frame4,text="Username",bg="white",fg="black",font=("Helvetica",16)).place(x=410,y=140)
u_line=Label(frame4,text="",bg="black").place(x=420,y=205,width=300,height=1)
u_entry=Entry(frame4,text="",bd="0")
u_entry.place(x=445,y=185,width=275)
User=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\user.png")
Button(frame4,image=User,bd="0",bg="white").place(x=420,y=180,width=21,height=21)

e=Label(frame4,text="Email",bg="white",fg="black",font=("Helvetica",16)).place(x=410,y=250)
e_line=Label(frame4,text="",bg="black").place(x=420,y=320,width=300,height=1)
e1=Entry(frame4,text="",bd="0")
e1.place(x=445,y=300,width=275)
e_mail=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\mail.png")
Button(frame4,image=e_mail,bd="0",bg="white").place(x=420,y=295,width=21,height=22)

np=Label(frame4,text="New Password",bg="white",fg="black",font=("Helvetica",16)).place(x=410,y=360)
np_line=Label(frame4,text="",bg="black").place(x=420,y=430,width=300,height=1)
e2=Entry(frame4,text="",bd="0")
e2.place(x=445,y=410,width=275)
np_Lock=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\lock.png")
Button(frame4,image=np_Lock,bd="0",bg="white").place(x=420,y=405,width=21,height=18)

cnp=Label(frame4,text="Confirm New Password",bg="white",fg="black",font=("Helvetica",16)).place(x=410,y=470)
cnp_line=Label(frame4,text="",bg="black").place(x=420,y=540,width=300,height=1)
cnp_entry=Entry(frame4,text="",bd="0").place(x=445,y=520,width=275)
cnp_Lock=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\lock.png")
Button(frame4,image=cnp_Lock,bd="0",bg="white").place(x=420,y=515,width=21,height=18)

Submit_button=Button(frame4,text="Submit",font=("Lato",16),bg="#ffa31a",fg="white",command=Update).place(x=540,y=560,width=100)

line=Label(root,text="",bg="black").place(x=40,y=135,width=1520,height=2)

Head=Label(root,text="W",font=("Helvetica",50,"bold"),bg="white",fg="#ff9999").place(x=320,y=51)
Head=Label(root,text="elcome",font=("Helvetica",30),bg="white",fg="#ff9999").place(x=385,y=77)
Head=Label(root,text="T",font=("Helvetica",50,"bold"),bg="white",fg="#ff9999").place(x=530,y=51)
Head=Label(root,text="o",font=("Helvetica",30),bg="white",fg="#ff9999").place(x=565,y=76)
Head=Label(root,text="A",font=("Helvetica",50,"bold"),bg="white",fg="#ff9999").place(x=620,y=51)
Head=Label(root,text="dmin",font=("Helvetica",30),bg="white",fg="#ff9999").place(x=670,y=75)
Head=Label(root,text="R",font=("Helvetica",50,"bold"),bg="white",fg="#ff9999").place(x=780,y=51)
Head=Label(root,text="egisteration",font=("Helvetica",30),bg="white",fg="#ff9999").place(x=830,y=75)

Logout_lbl=Label(root,text="Logout",font=("Helvetica",16,"bold"),bg="white",fg="#ff9999").place(x=1430,y=77)
Home_lbl=Label(root,text="Home",font=("Helvetica",14,"bold"),bg="white",fg="#ff9999").place(x=41,y=303)
Manage_lbl=Label(root,text="Manage",font=("Helvetica",14,"bold"),bg="white",fg="#ff9999").place(x=32,y=407)
View_lbl=Label(root,text="View",font=("Helvetica",14,"bold"),bg="white",fg="#ff9999").place(x=41,y=543)
Setting_lbl=Label(root,text="Settings",font=("Helvetica",14,"bold"),bg="white",fg="#ff9999").place(x=30,y=655)
Exit_lbl=Label(root,text="Exit",font=("Helvetica",14,"bold"),bg="white",fg="#ff9999").place(x=46,y=780)

Profile=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\Profile.png")
Logout=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\logout.png")
Home=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\home.png")
Manage=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\manage.png")
View=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\view.png")
Setting=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\setting.png")
Exit=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\exit.png")
Clock=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\clock.png")

Profile_btn=Button(root,text="",bd="0",image=Profile,bg="white",activebackground="white").place(x=1060,y=70,width=55,height=58)
Logout_btn=Button(root,text="",bd="0",image=Logout,bg="white",activebackground="white",command=logout).place(x=1380,y=75,width=55,height=30)
Home_btn=Button(root,text="",bd="0",image=Home,bg="white",activebackground="white",command=lambda:show_frame(frame1)).place(x=40,y=240,width=60,height=60)
Manage_btn=Button(root,text="",bd="0",image=Manage,bg="white",activebackground="white",command=lambda:show_frame(frame2)).place(x=40,y=360,width=60,height=50)
View_btn=Button(root,text="",bd="0",image=View,bg="white",activebackground="white",command=lambda:show_frame(frame3)).place(x=40,y=480,width=60,height=60)
Setting_btn=Button(root,text="",bd="0",image=Setting,bg="white",activebackground="white",command=lambda:show_frame(frame4)).place(x=40,y=600,width=60,height=60)
Exit_btn=Button(root,text="",bd="0",image=Exit,bg="white",activebackground="white",command=call).place(x=40,y=720,width=60,height=60)
Clock_btn=Button(root,text="",bd="0",image=Clock,bg="white",activebackground="white").place(x=50,y=70,width=60,height=60)

Time=Label(root,font=("Helvetica",20,'bold'), bg="white", fg="black", bd =10)
Time.place(x=100,y=50)
digitalclock()

date=dt.datetime.now()
format_date = f"{date:%a, %b %d %Y}"

Date=Label(root,text=format_date,fg="black",bg="white",font=("helvetica",18,'bold'))
Date.place(x=100,y=90)

profile_label=Label(root,text="js1932002singh@gmail.com",font=("Helvetica",14),fg="green",bg="white").place(x=1105,y=85)
show_frame(frame1)

root.mainloop()
