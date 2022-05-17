from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from database import*
class crackClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("700x300+220+130")
        self.root.title("Crack The Password")
        self.root.config(bg="#FFF0F5")
        self.root.focus_force()
        #-------all variable-------------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phno=StringVar()
        self.var_email=StringVar()
        self.var_gpass=StringVar()
        self.var_fname1=StringVar()
        self.var_lname1=StringVar()
        self.var_gender1=StringVar()
        self.var_dob1=StringVar()
        self.var_phno1=StringVar()
        self.var_email1=StringVar()
        
        #---------------title----------------
        title=Label(self.root,text="crack the password using the given data",font=("rockwell",20),bg="rosybrown",fg="mint cream", justify=CENTER).place(x=0,y=0,width=700,height=40)
        #-----------------contents-------------------------------
        #--------------------row1------------------------
        lbl_fname=Label(self.root,text="First Name",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=50,y=60)
        lbl_lname=Label(self.root,text="Last Name",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=50,y=120) 
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=50,y=180)
        
        txt_fname=Entry(self.root,textvariable=self.var_fname,font=("rockwell",15),bg="ivory",state='readonly').place(x=150,y=60,width=180)
        txt_lname=Entry(self.root,textvariable=self.var_lname,font=("rockwell",15),bg="ivory",state='readonly').place(x=150,y=120,width=180)
        txt_gender=Entry(self.root,textvariable=self.var_gender,font=("rockwell",15),bg="ivory",state='readonly').place(x=150,y=180,width=180)        
        #--------------------row2------------------------
        lbl_dob=Label(self.root,text="DOB",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=350,y=60)
        lbl_phno=Label(self.root,text="Phone No",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=350,y=120)
        lbl_email=Label(self.root,text="E Mail",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=350,y=180)         
        
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("rockwell",15),bg="ivory",state='readonly').place(x=450,y=60,width=180)
        txt_phno=Entry(self.root,textvariable=self.var_phno,font=("rockwell",15),bg="ivory",state='readonly').place(x=450,y=120,width=180)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("rockwell",15),bg="ivory",state='readonly').place(x=450,y=180,width=180)
        lbl_gpass=Label(self.root,text="enter the guesed password ",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=50,y=240)
        txt_gpass=Entry(self.root,textvariable=self.var_gpass,font=("rockwell",15),bg="ivory").place(x=300,y=240,width=200)
        btn_get_data=Button(self.root,text="get data",font=("rockwell",15),command=self.get_data,bg="rosy brown",fg="mint cream",cursor="hand2").place(x=510,y=240,width=80,height=28)
        btn_check=Button(self.root,text="check",font=("rockwell",15),bg="rosy brown",fg="mint cream",cursor="hand2").place(x=597,y=240,width=80,height=28) 
         
        
    #--------------------func-----------------------------------
    def get_data(self): 
        self.var_fname.set(self.var_fname1)
        self.var_lname.set(self.var_lname1)
        self.var_gender.set(self.var_gender1)
        self.var_dob.set(self.var_dob1)
        self.var_phno.set(self.var_phno1)
        self.var_email.set(self.var_email1) 
        print(self.var_email1)  
           
            
        
if __name__=="__main__":
    root=Tk()
    obj=crackClass(root)
    root.mainloop()
