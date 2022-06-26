from tkinter import *
from tkinter import messagebox
from PIL import ImageTk , Image
import os

file = os.path.dirname(__file__)
img = os.path.join(file, "img")

class Login:
    def __init__(self,root):
        self.root =root
        self.root.title('DBMS Student Management System')
        self.root.geometry("1536x844+0+0")

        self.bg_ico = Image.open(os.path.join(img,"bg.jpg"))
        self.bg_ico = self.bg_ico.resize((1300,520), Image.ANTIALIAS)
        self.bg_ico = ImageTk.PhotoImage(self.bg_ico)
        
        self.back_ico = Image.open(os.path.join(img,"back.jpg"))
        self.back_ico = self.back_ico.resize((1536,864), Image.ANTIALIAS)
        self.back_ico = ImageTk.PhotoImage(self.back_ico)

        self.back_img = Label(self.root, image = self.back_ico).place(x=0,y=0)
        
        self.user_ico = Image.open(os.path.join(img,"user.png"))
        self.user_ico = self.user_ico.resize((30,30), Image.ANTIALIAS)
        self.user_ico = ImageTk.PhotoImage(self.user_ico)

        self.lock_ico = Image.open(os.path.join(img,"lock.png"))
        self.lock_ico = self.lock_ico.resize((30,30), Image.ANTIALIAS)
        self.lock_ico = ImageTk.PhotoImage(self.lock_ico)
    
        self.username = StringVar()
        self.password = StringVar()
        
        L_frame = Frame(self.root,bd =3,relief = RIDGE)
        L_frame.place(x=100,y=100,width = 1300,height=600)

        self.bg_img = Label(L_frame, image = self.bg_ico,width = 1300).place(x=0,y=70,relwidth =1)
        title =Label(L_frame,text = "Login System", font=("times new roman", 30, "bold"),bd =10,relief=SUNKEN,bg ='powder blue', fg = 'OrangeRed4' ).pack(side =TOP, fill =X)

        interface = Frame(L_frame, bd =10, relief = RIDGE, bg ='mistyrose')
        interface.place(x=700,y=100,width = 580, height = 450)

        desc = Label(interface, text="Login Here", font=("Goudy old style", 40, "bold"), fg="#d77337", bg="mistyrose").place(x=150,y=0)
        usrnametitle = Label(interface, text="Username", font=("times new roman", 25), bg='mistyrose').place(x=10, y=80)
        usrnametxt = Entry(interface, textvariable =self.username, font =('Helvetica', 17), bd =4, relief=SUNKEN, width = 25)
        self.user_img = Label(interface, image=self.user_ico).place(x=150, y=82)
        usrnametxt.place(x=190, y =82)

        pswtitle = Label(interface, text="Password", font=("times new roman", 25), bg='mistyrose').place(x=10, y=170)
        pswtxt = Entry(interface, textvariable =self.password,show="*", font =('Helvetica', 17), bd =4, relief=SUNKEN, width = 25)
        self.lock_img = Label(interface, image=self.lock_ico).place(x=150, y=173)
        pswtxt.place(x=190, y =172)

        login_btn = Button(interface, text ="LOGIN",font ="arial 12 bold", bd=5,fg = 'Lawn green',bg = 'navy',width =12,height =1,command=self.logfn).place(x=30,y=290)
        reset_btn = Button(interface, text ="RESET",font ="arial 12 bold", bd=5,fg = 'light goldenrod',bg = 'navy',width =12,height =1,command= self.resetfn).place(x=210,y=320)
        exit_btn = Button(interface, text ="EXIT",font ="arial 12 bold", bd=5,fg = 'white',bg = 'navy',width =12,height =1,command = self.exitfn).place(x=390,y=350)

    def logfn(self):
        if self.username.get() == "dbmsproject" and self.password.get() == "123456":
            self.root.destroy()
            import main
            main.Student()
            

        else :
            messagebox.showerror("Denied", "Incorrect Password/UserName")

        self.resetfn()    

    def resetfn(self):
        if self.username.get() or self.password.get():
            self.username.set("") 
            self.password.set("")           

    def exitfn(self):
        res= messagebox.askyesno("EXIT ?","Do You Really Wish To Exit ?")
        if res > 0:
            self.root.destroy()

        else:
            return    


root =Tk()
ob=Login(root)
root.mainloop()        