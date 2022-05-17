from tkinter import*
from PIL import ImageTk, Image
from database import databaseClass
class Home_Page:
    def __init__(self,root):
        self.root=root
        self.root.title("CIPHER IT")
        self.root.geometry("900x500+220+130")
        self.root.config(bg="#FFF0F5")
        #---------Animation Images-------
        self.im1=ImageTk.PhotoImage(file="image/2.png")
        self.im2=ImageTk.PhotoImage(file="image/3.png")
        self.im3=ImageTk.PhotoImage(file="image/4.png")
        self.lbl_change_image=Label(self.root,bg="white",bd=6,relief=GROOVE)
        self.lbl_change_image.place(x=80,y=50,width=330,height=400)

        self.animate()
        #-------------frame1---------
        title_frame=Frame(self.root,bd=6,relief=GROOVE,bg="white")
        title_frame.place(x=480,y=50,width=330,height=400)
        title=Label(title_frame,text="CIPHER IT",font=("Rockwell",30,"bold"),bg="rosybrown",fg="mint cream",bd=2,relief=RAISED).place(x=0,y=0,relwidth=1)
        lbl1=Label(title_frame,text="To View \nThe Breached Database",font=("Rockwell",20),bg="white",fg="dimgray").place(x=10,y=150,width=300)
        btn1=Button(title_frame,text="Click Here",command=self.database,font=("Rockwell",15),bg="rosybrown",activebackground="brown",fg="mint cream",activeforeground="white",cursor="hand2").place(x=65,y=250,width=200,height=40)
       
    #-----------------functions-------------------    
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate) 


    def database(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=databaseClass(self.new_win)
      
root=Tk()
obj=Home_Page(root)
root.mainloop()