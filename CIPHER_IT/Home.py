from tkinter import*
from PIL import ImageTk, Image
class Home_Page:
    def __init__(self,root):
        self.root=root
        self.root.title("CIPHER IT")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #---------Animation Images-------
        self.im1=ImageTk.PhotoImage(file="image/2.png")
        self.im2=ImageTk.PhotoImage(file="image/3.png")
        self.im3=ImageTk.PhotoImage(file="image/4.png")
        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=200,y=130,width=400,height=458)

        self.animate()
        #-------------frame1---------
        title_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        title_frame.place(x=800,y=110,width=370,height=460)
        title=Label(title_frame,text="CIPHER IT",font=("Rockwell",30,"bold"),bg="#fafafa").place(x=0,y=0,relwidth=1)
        lbl1=Label(title_frame,text="To View The Breached Database",font=("Rockwell",17),bg="white",fg="#767171").place(x=10,y=100)
        btn1=Button(title_frame,text="Click Here",font=("Rockwell",15),bg="dodgerblue4",activebackground="navy",fg="mint cream",activeforeground="white",cursor="hand2").place(x=85,y=170,width=200,height=40)
        lbl2=Label(title_frame,text="To Guess The Password",font=("Rockwell",17),bg="white",fg="#767171").place(x=55,y=260)
        btn2=Button(title_frame,text="Click Here",font=("Rockwell",15),bg="dodgerblue4",activebackground="navy",fg="mint cream",activeforeground="white",cursor="hand2").place(x=85,y=330,width=200,height=40)
    #-----------------functions-------------------    
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)    
root=Tk()
obj=Home_Page(root)
root.mainloop()