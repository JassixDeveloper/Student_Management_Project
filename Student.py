from tkinter import *
from tkinter import messagebox
import os
import sqlite3
from tkinter import ttk

def show_frame(frame):
    frame.tkraise()

def dashboard():
    filename='dashboard.py'
    os.system(filename)
    root.destroy()
    exit()

def Add():
    filename='Addstudent.py'
    os.system(filename)
    root.destroy()
    exit()

def Update():
    filename='Updatestudent.py'
    os.system(filename)
    root.destroy()
    exit()

def Delete():
    filename='Deletestudent.py'
    os.system(filename)
    root.destroy()
    exit()

def update(rows):
    student_tree.delete(*student_tree.get_children())
    for i in rows:
        student_tree.insert('','end',values=i)

def search():
    q2=q.get()
    query="SELECT * FROM `student` WHERE First_Name LIKE '%"+q2+"%' OR Last_Name LIKE '%"+q2+"%'"
    cursor.execute(query)
    rows=cursor.fetchall()
    update(rows)

def clear_search(events):
    search_entry.delete(0, "end")

def view():
    query="SELECT * FROM `student`"
    cursor.execute(query)
    rows=cursor.fetchall()

def do_popup(event):
        popup = Menu(frame1, tearoff=0)
        popup.add_command(label="UPDATE", command=Update)
        popup.add_separator()
        popup.add_command(label="DELETE", command=Delete)
        popup.add_separator()
        popup.add_command(label="FETCH")

        try:
            popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            popup.grab_release()

global conn, cursor
conn=sqlite3.connect('Database.db')
cursor=conn.cursor()

root=Tk()
root.geometry("1600x900")
root.title("Student Management Dashboard")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

Canvas(root,width=300,height=300)
img=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\BG2.png")      
Label(root,image=img).pack()

q=StringVar()

lbl=Label(root,text="Student Management Dashboard",fg="#ff9999",font=("Helvetica",46,"bold"),bg="white").place(x=330,y=40)
lbl=Label(root,text="Student Management Options",fg="#ff9999",font=("Helvetica",14),bg="white").place(x=85,y=250)

Box=Label(root,text="",bg="#a6a6a6").place(x=70,y=263,width=2,height=470)
Box=Label(root,text="",bg="#a6a6a6").place(x=70,y=263,width=18,height=2)
Box=Label(root,text="",bg="#a6a6a6").place(x=338,y=263,width=60,height=2)
Box=Label(root,text="",bg="#a6a6a6").place(x=398,y=263,width=2,height=470)
Box=Label(root,text="",bg="#a6a6a6").place(x=70,y=733,width=330,height=2)

search_entry=Entry(root,highlightthickness=0,relief=FLAT,bg="white",fg="#6b6a69",font=("yu gothic ui semibold",12))
search_entry.place(x=600,y=167,width=550)
search_txt="Search here.........."
search_entry.insert(0,search_txt)
search_entry.bind("<1>",clear_search)
search_line=Label(root,text="",bg="#a6a6a6").place(x=600,y=195,width=550,height=2)
        
Search=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\Search.png")
View=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\view1.png")

Btn=Button(root,text="",image=Search,bd="0",bg="white",activebackground="white",command=search).place(x=1170,y=170,width=30,height=30)
search_btn=Button(root,text="Search",bd="0",bg="white",activebackground="white",font=("Helvetica",10),fg="#a6a6a6",command=search).place(x=1200,y=174)

Btn=Button(root,text="",image=View,bd="0",bg="white",activebackground="white",command=view).place(x=1280,y=170,width=28,height=28)
view_btn=Button(root,text="View All",bd="0",bg="white",activebackground="white",font=("Helvetica",10),fg="#a6a6a6",command=view).place(x=1315,y=174)

btn=Button(root,text="ADD STUDENT",fg="white",font=("Helvetica",15),bg="#f88600",bd="0",activebackground="#f88600",command=Add).place(x=170,y=329)
btn=Button(root,text="UPDATE STUDENT",fg="white",font=("Helvetica",15),bg="#f88600",bd="0",activebackground="#f88600",command=Update).place(x=150,y=406)
btn=Button(root,text="DELETE STUDENT",fg="white",font=("Helvetica",15),bg="#f88600",bd="0",activebackground="#f88600",command=Delete).place(x=150,y=485)
btn=Button(root,text="GO TO DASHBOARD",fg="white",font=("Helvetica",15),bg="#f88600",bd="0",activebackground="#f88600",command=dashboard).place(x=140,y=565)

'''s1=StringVar()
s2=StringVar()

Select1=['Search','Sort'];
Select2=['Ascending','Descending'];

droplist=OptionMenu(root,s1, *Select1)
droplist.config(width=3,bd="1",font=("Helvetica",11),fg="#737373")
s1.set('Search :')
droplist.place(x=500,y=165,width=95,height=35)

droplist=OptionMenu(root,s2, *Select2)
droplist.config(width=3,bd="1",font=("Helvetica",11),fg="#737373")
s2.set('Sort By :')
droplist.place(x=620,y=165,width=100,height=35)'''

frame1=Frame(root)

for frame in (frame1,):
    frame.place(x=455,y=210,width=1046,height=589)

#================== Frame
tree_view_frame = Frame(frame1, bg="white")
tree_view_frame.place(x=0,y=0,height=589,width=1046)

style = ttk.Style()
style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="red")
style.configure("Treeview", font=('yu gothic ui', 9, "bold"), foreground="#f29844")

scroll_x = Scrollbar(tree_view_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(tree_view_frame, orient=VERTICAL)
student_tree = ttk.Treeview(tree_view_frame,
columns=(
"STUDENT ID","FNAME", "LNAME", "DOB", "GENDER", "ADDRESS",
"CONTACT NO", "SHIFT", "COURSE ENROLLED", "BATCH", "SECTION"),
xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=student_tree.xview)
scroll_y.config(command=student_tree.yview)

# ==========================TreeView Heading====================
student_tree.heading("STUDENT ID", text="STUDENT ID")
student_tree.heading("FNAME", text="FNAME")
student_tree.heading("LNAME", text="LNAME")
student_tree.heading("DOB", text="DOB")
student_tree.heading("GENDER", text="GENDER")
student_tree.heading("ADDRESS", text="ADDRESS")
student_tree.heading("CONTACT NO", text="CONTACT NO")
student_tree.heading("SHIFT", text="SHIFT")
student_tree.heading("COURSE ENROLLED", text="COURSE ENROLLED")
student_tree.heading("BATCH", text="BATCH")
student_tree.heading("SECTION", text="SECTION")
student_tree["show"] = "headings"

query="SELECT * FROM `student`"
cursor.execute(query)
rows=cursor.fetchall()
update(rows)

# ==========================TreeView Column====================
student_tree.column("STUDENT ID", width=100)
student_tree.column("FNAME", width=170)
student_tree.column("LNAME", width=170)
student_tree.column("ADDRESS", width=150)
student_tree.column("GENDER", width=150)
student_tree.column("CONTACT NO", width=150)
student_tree.column("DOB", width=150)
student_tree.column("SHIFT", width=150)
student_tree.column("COURSE ENROLLED", width=150)
student_tree.column("BATCH", width=100)
student_tree.column("SECTION", width=100)
student_tree.pack(fill=BOTH, expand=1)
student_tree.bind("<Button-3>",do_popup)

show_frame(frame1)

root.mainloop()
