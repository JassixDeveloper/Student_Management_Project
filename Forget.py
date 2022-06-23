from tkinter import *
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("1600x900")
root.title("Forget Password")

Canvas(root,width=300,height=300)
img=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\BG.png")      
Label(root,image=img).pack()

def Update():
    email=e1.get()
    password=e2.get()
    conn=sqlite3.connect('Admin Registered.db')
    with conn:
        cursor=conn.cursor()
        up="Update `user` set password='%s' WHERE email='%s'"%(password,email)
        cursor.execute(up)
        conn.commit()
        messagebox.showinfo("Information","Record Updated")
        
def clicked():
    e2['show']=''

Head=Label(root,text="N",font=("Comic Sans MS",82),bg="white").place(x=540,y=110)
Head=Label(root,text="ew",font=("Comic Sans MS",34,"bold"),bg="white").place(x=631,y=181)
Head=Label(root,text="P",font=("Comic Sans MS",82),bg="white").place(x=721,y=110)
Hea1=Label(root,text="assword",font=("Comic Sans MS",34,"bold"),bg="white").place(x=765,y=195,height=40)

Head_Line=Label(root,text="",bg="black").place(x=553,y=248,width=400,height=2)

label_1=Label(root,text="Email",font=("Lato",14),bg="white").place(x=520,y=400)
New_Line=Label(root,text="",bg="black").place(x=525,y=455,width=400,height=1)
e1=Entry(root,bg="white",bd="0",font=("Lato",12))
e1.place(x=545,y=433,width=380)

label_2=Label(root,text="New Password",font=("Lato",14),bg="white").place(x=520,y=500)
Password_Line=Label(root,text="",bg="black").place(x=525,y=555,width=400,height=1)
e2=Entry(root,bg="white",bd="0",font=("Lato",12))
e2['show']='*'
e2.place(x=545,y=533,width=380)

Submit_button=Button(root,text="Submit",font=("Lato",16),bg="#ffa31a",fg="white",command=Update).place(x=700,y=615,width=100)

Mail=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\mail.png")
Lock=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\lock.png")
New_Lock=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\New Lock.png")
Eye=PhotoImage(file=r"C:\Users\Anmol\Documents\MY VASIYAT\python\Project\assets\eye.png")

Button(root,image=Mail,bd="0",bg="white").place(x=521,y=432,width=21,height=22)
Button(root,image=Lock,bd="0",bg="white").place(x=521,y=535,width=21,height=18)
Button(root,image=Eye,bd="0",bg="white",activebackground="white",command=clicked).place(x=895,y=525,width=30,height=30)
New_Lock_Button=Button(root,image=New_Lock,bd="0",bg="white").place(x=713,y=285)

Description=Label(root,text="* Please enter your Old Password,",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=610,y=700)
Description1=Label(root,text="then enter New Password,",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=643,y=725)
Description2=Label(root,text="and submit it!",fg="#b3b3b3",bg="white",font=("Lato",14)).place(x=695,y=750)

root.mainloop()
