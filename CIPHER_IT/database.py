from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class databaseClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Breached Database")
        self.root.config(bg="#FFF0F5")
        self.root.focus_force()
        #-------all variable-------------------
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_slno=StringVar()
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phno=StringVar()
        self.var_email=StringVar()
        self.var_hpass=StringVar()
        
        #--------------------search frame--------------------------------
        SearchFrame=LabelFrame(self.root,text="Search for data",font=("rockwell",12),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        #----------------------option---------------
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","fname","email","gender","phoneno"),state='readonly', justify=CENTER,font=("rockwell",15))
        cmb_search.place(x=10,y=10,width=180,height=26)
        cmb_search.current(0)
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("rockwell",15),bg="ivory").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("rockwell",15),bg="rosybrown",fg="mint cream",cursor="hand2").place(x=440,y=10,width=130,height=27)
        #---------------title----------------
        title=Label(self.root,text="Account Details",font=("rockwell",15),bg="rosybrown",fg="mint cream", justify=CENTER).place(x=0,y=100,width=1200)
        #-----------------contents-------------------------------
        #--------------------row1------------------------
        lbl_slno=Label(self.root,text="Slno",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=50,y=150)
        lbl_fname=Label(self.root,text="First name",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=400,y=150) 
        lbl_lname=Label(self.root,text="Last name",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=750,y=150)
        
        txt_slno=Entry(self.root,textvariable=self.var_slno,font=("rockwell",15),bg="ivory",state='readonly').place(x=150,y=150,width=180)
        txt_fname=Entry(self.root,textvariable=self.var_fname,font=("rockwell",15),bg="ivory",state='readonly').place(x=500,y=150,width=180)
        txt_lname=Entry(self.root,textvariable=self.var_lname,font=("rockwell",15),bg="ivory",state='readonly').place(x=850,y=150,width=180)        
        #--------------------row2------------------------
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=50,y=190)
        lbl_dob=Label(self.root,text="DOB",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=400,y=190)
        lbl_phno=Label(self.root,text="Phone No",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=750,y=190)         
        
        txt_gender=Entry(self.root,textvariable=self.var_gender,font=("rockwell",15),bg="ivory",state='readonly').place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("rockwell",15),bg="ivory",state='readonly').place(x=500,y=190,width=180)
        txt_phno=Entry(self.root,textvariable=self.var_phno,font=("rockwell",15),bg="ivory",state='readonly').place(x=850,y=190,width=180)
        #--------------------------row3----------------------------
        lbl_email=Label(self.root,text="email",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=50,y=230)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("rockwell",15),bg="ivory",state='readonly').place(x=150,y=230,width=230)
        lbl_hpass=Label(self.root,text="Hashed password",font=("times new roman",15),bg="#FFF0F5",fg="dim gray").place(x=400,y=230)
        txt_hpass=Entry(self.root,textvariable=self.var_hpass,font=("rockwell",15),bg="ivory",state='readonly').place(x=600,y=230,width=350)   

        btn_rtable=Button(self.root,text="crack password using rainbow table",command=self.rainbow,font=("rockwell",15),bg="rosy brown",fg="mint cream",cursor="hand2").place(x=50,y=270,width=400,height=28)
        btn_brut=Button(self.root,text="crack password by bruth force method",font=("rockwell",15),bg="rosy brown",fg="mint cream",cursor="hand2").place(x=500,y=270,width=400,height=28)
        #---------------------account details-------------------------
        de_frame=Frame(self.root,bd=3,relief=RIDGE)
        de_frame.place(x=0,y=320,relwidth=1,height=180)

        scrolly=Scrollbar(de_frame,orient=VERTICAL)
        scrollx=Scrollbar(de_frame,orient=HORIZONTAL)

        self.detailsTable=ttk.Treeview(de_frame,columns=("slno","fname","lname","gender","dob","phno","email","hashed password"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.detailsTable.xview)
        scrolly.config(command=self.detailsTable.yview)
        self.detailsTable.heading("slno",text="slno")
        self.detailsTable.heading("fname",text="first name")
        self.detailsTable.heading("lname",text="last name")
        self.detailsTable.heading("gender",text="gender")
        self.detailsTable.heading("dob",text="dob")
        self.detailsTable.heading("phno",text="phno")
        self.detailsTable.heading("email",text="email")
        self.detailsTable.heading("hashed password",text="hashed password")        
        self.detailsTable["show"]="headings"
        self.detailsTable.pack(fill=BOTH,expand=1)
        self.detailsTable.column("slno",width=20)
        self.detailsTable.column("fname",width=60)
        self.detailsTable.column("lname",width=60)
        self.detailsTable.column("gender",width=30)
        self.detailsTable.column("dob",width=90)
        self.detailsTable.column("phno",width=100)
        self.detailsTable.column("email",width=100)
        self.detailsTable.column("hashed password",width=150)        
        self.detailsTable.pack(fill=BOTH,expand=1)
        self.detailsTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
 #-------------------------functionality---------------------------------------
    def get_data(self,ev): 
        f=self.detailsTable.focus()
        content=(self.detailsTable.item(f))
        row=content['values']        
        self.var_slno.set(row[0])
        self.var_fname.set(row[1])
        self.var_lname.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_phno.set(row[5])
        self.var_email.set(row[6])        
        self.var_hpass.set(row[7])
       
        


    def show(self):
        con=sqlite3.connect(database=r'hacked.db')
        cur=con.cursor()
        try:
            cur.execute("select * from Hacked_Database")
            rows=cur.fetchall()
            self.detailsTable.delete(*self.detailsTable.get_children())
            for row in rows:
                self.detailsTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}',parent=self.root)   


    def search(self):  
        con=sqlite3.connect(database=r'hacked.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":   
                messagebox.showerror("Error","Search Input is required",parent=self.root)
            else:            
                cur.execute("select * from Hacked_Database where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:        
                    self.detailsTable.delete(*self.detailsTable.get_children())
                    for row in rows:
                        self.detailsTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)      
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}',parent=self.root)        

    def rainbow(self): 
        if self.var_fname.get()=="":
            messagebox.showerror("Error","No record selected",parent=self.root)
        else:    
            fname=self.var_fname.get()
            lname=self.var_lname.get()
            gender=self.var_gender.get()
            dob=self.var_dob.get()
            phno=self.var_phno.get()
            email=self.var_email.get()
            self.root.destroy()
            os.system("python rainbowTable.py")
        

    
        


if __name__=="__main__":
    root=Tk()
    obj=databaseClass(root)
    root.mainloop()
