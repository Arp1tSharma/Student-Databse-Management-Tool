from tkinter import *
from tkinter import ttk
import pymysql
from PIL import ImageTk, Image
from tkinter import messagebox
import os
import smtplib,ssl
import matplotlib.pyplot as plt

file = os.path.dirname(__file__)
img = os.path.join(file, "img")

class Student:
    def __init__(self):

        self.root = Tk()
        
        self.root.title("Data Base Stduent Management System")
        self.root.geometry("1530x800+0+0")
        self.root.resizable(True, False)

        self.back_ico = Image.open(os.path.join(img, "back.jpg"))
        self.back_ico = self.back_ico.resize((1536, 864), Image.ANTIALIAS)
        self.back_ico = ImageTk.PhotoImage(self.back_ico)

        self.bar_ico = Image.open(os.path.join(img, "download.jpg"))
        self.bar_ico = self.bar_ico.resize((120,100), Image.ANTIALIAS)
        self.bar_ico = ImageTk.PhotoImage(self.bar_ico)

        self.logout_ico = PhotoImage(file = os.path.join(img,"logout.png"))
        self.logout_ico = self.logout_ico.subsample(10,10)

        self.linegraph_ico = Image.open(os.path.join(img,"download.png"))
        self.linegraph_ico = self.linegraph_ico.resize((120,100),Image.ANTIALIAS)
        self.linegraph_ico = ImageTk.PhotoImage(self.linegraph_ico)

        self.user_ico = Image.open(os.path.join(img, "user.png"))
        self.user_ico = self.user_ico.resize((30, 30), Image.ANTIALIAS)
        self.user_ico = ImageTk.PhotoImage(self.user_ico)

        self.lock_ico = Image.open(os.path.join(img, "lock.png"))
        self.lock_ico = self.lock_ico.resize((30, 30), Image.ANTIALIAS)
        self.lock_ico = ImageTk.PhotoImage(self.lock_ico)
        
        self.mail_ico = Image.open(os.path.join(img, "mail.png"))
        self.mail_ico = self.mail_ico.resize((30, 30), Image.ANTIALIAS)
        self.mail_ico = ImageTk.PhotoImage(self.mail_ico)

        self.back_img = Label(self.root, image=self.back_ico).place(x=0, y=0)

        title = Label(self.root, text ="Student Management System",bd =10,relief = RAISED,font = ("times new roman",40, "bold"),bg = 'blue4', fg = "light cyan")
        title.pack(side = TOP,fill = X)

        exit_btn = Button(self.root, text ="Exit",font ="arial 12 bold" ,width =10,height =1,bg="white",activebackground = "darkorchid4", fg='firebrick2',command = self.exitfn).place(x=1400,y=25)
        logout_btn = Button(self.root, text="Log Out", font="arial 12 bold", image=self.logout_ico, compound=LEFT,width = 100,command= self.logoutfn).place(x=20, y=25)

        # All Variables
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.marks = DoubleVar()
        self.out_of = DoubleVar()
        self.perctg = DoubleVar()

        self.srch_by = StringVar()
        self.srch_txt = StringVar()


        # Frame for managing data
        M_frame = Frame(self.root,bd =4, relief = RIDGE, bg = "royal blue")
        M_frame.place(x=20,y=100,width = 550, height = 670)

        M_title = Label(M_frame, text = "Manage Students",relief = GROOVE,font = ("times new roman",25,"bold"),bg = 'lavender', fg = "navy")
        M_title.grid(row =0, columnspan =20,pady =20, padx= 150,)

        lbl_roll = Label(M_frame, text="Roll No", font=("times new roman", 20, "bold"), bg="royal blue", fg="lavender")
        lbl_roll.grid(row =1, column =0 ,pady=10,padx =10, sticky = "w")  
        txt_roll = Entry(M_frame, textvariable =self.Roll_No_var, font =('times new roman', 15), bd =5, relief=GROOVE, width = 35)
        txt_roll.grid(row= 1, column =1, pady =10, padx =20, sticky = "w")      

        lbl_name = Label(M_frame, text="Name", font=("times new roman", 20, "bold"), bg="royal blue", fg="lavender")
        lbl_name.grid(row =2, column =0 ,pady=10,padx =10, sticky = "w")  
        txt_name = Entry(M_frame, textvariable =self.name_var, font =('times new roman', 15), bd =5, relief=GROOVE, width = 35)
        txt_name.grid(row= 2, column =1, pady =10, padx =20, sticky = "w")      

        lbl_mail = Label(M_frame, text="Email", font=("times new roman", 20, "bold"), bg="royal blue", fg="lavender")
        lbl_mail.grid(row =3, column =0 ,pady=10,padx =15, sticky = "w")  
        txt_mail = Entry(M_frame, textvariable =self.email_var, font =('times new roman', 15), bd =5, relief=GROOVE, width = 35)
        txt_mail.grid(row= 3, column =1,columnspan =10, pady =10, padx =20, sticky = "w")      

        lbl_gender = Label(M_frame, text="Gender", font=("times new roman", 20, "bold"), bg="royal blue", fg="lavender")
        lbl_gender.grid(row =4, column =0 ,pady=10,padx =10, sticky = "w")  
        comb_gender = ttk.Combobox(M_frame, textvariable =self.gender_var, font = ("times new roman",15),state='readonly', width = 34)
        comb_gender['values'] = ("Male", 'Female', 'Other')
        comb_gender.grid(row=4, column =1, padx=10,pady=10)

        lbl_dob = Label(M_frame, text="D.O.B", font=("times new roman", 20, "bold"), bg="royal blue", fg="lavender")
        lbl_dob.grid(row =5, column =0 ,pady=10,padx =10, sticky = "w")  
        txt_dob = Entry(M_frame, textvariable =self.dob_var, font =('times new roman', 15), bd =5, relief=GROOVE, width = 35)
        txt_dob.grid(row= 5, column =1, pady =10, padx =20, sticky = "w")      

        lbl_cnct = Label(M_frame, text="Contact", font=("times new roman", 20, "bold"), bg="royal blue", fg="lavender")
        lbl_cnct.grid(row =6, column =0 ,pady=10,padx =10, sticky = "w")  
        txt_cnct = Entry(M_frame, textvariable =self.contact_var, font =('times new roman', 15), bd =5, relief=GROOVE, width = 35)
        txt_cnct.grid(row= 6, column =1, pady =10, padx =20, sticky = "w")      
        
        lbl_adrs = Label(M_frame, text="Address", font=("times new roman", 20, "bold"), bg="royal blue", fg="lavender")
        lbl_adrs.grid(row =7, column =0 ,pady=10,padx =10, sticky = "w")  
        self.txt_adrs = Text(M_frame, width = 40, height = 4,font=("",13))
        self.txt_adrs.grid(row=7, column = 1, pady=10,padx=20, sticky = "w")

        # Buttons Frame
        btn_frame= Frame(M_frame,bd=4, relief= GROOVE,bg ="deep sky blue")
        btn_frame.place(x=10,y=530, width = 510)

        add_btn = Button(btn_frame, text ="Add",width =13,height =2,bg = "spring green",activebackground = "lime green",command = self.add_sudents).grid(row= 0,column=0,padx=11,pady=5)
        upd_btn = Button(btn_frame, text ="Update",width =13,height =2,bg = "gold2",activebackground = "gold",command = self.update_data).grid(row= 0,column=1,padx=11,pady=10)
        clr_btn = Button(btn_frame, text ="Clear",width =13,height =2,bg="red",activebackground = "firebrick4",command = self.clear_btn).grid(row= 0,column=2,padx=11,pady=10)
        del_btn = Button(btn_frame, text ="Delete",width =13,height =2,bg="Light Yellow",activebackground = "thistle3",command = self.delete_data).grid(row= 0,column=3,padx=11,pady=10)
        marks_btn = Button(M_frame, text ="Manage Marks",width =43,height =2,bg="white",activebackground = "thistle3",command = self.marks_win).place(x=150 , y= 605)
        
        # Frame for details showing data
        D_frame = Frame(self.root,bd =4, relief = RIDGE, bg = "blue4")
        D_frame.place(x=620,y=100,width = 880, height = 670)

        lbl_search = Label(D_frame, text="Search By", font=("times new roman", 20, "bold"), bg="blue4", fg="mint cream")
        lbl_search.grid(row =0, column =0 ,pady=15,padx =10, sticky = "w")  
        comb_search = ttk.Combobox(D_frame, textvariable = self.srch_by ,font = ("times new roman",15),state='readonly', width = 15)
        comb_search['values'] = ("Roll_No", 'Name', 'Email')
        comb_search.grid(row=0, column =1, padx=10,pady=15) 

        txt_search = Entry(D_frame,textvariable = self.srch_txt ,font =('times new roman', 12), bd =2, relief=SUNKEN, width = 25)
        txt_search.grid(row= 0, column =2, pady =15, padx =20, sticky = "w") 

        search_btn = Button(D_frame, text ="Search",width =13,height =1,bg="LemonChiffon2",activebackground = "lawn green",command = self.search_data).grid(row= 0,column=3,padx=20,pady=12)
        showall_btn = Button(D_frame, text ="Show All",width =13,height =1,bg="cornsilk2",activebackground = "lawn green",command=self.fetch_data).grid(row= 0,column=4,padx=20,pady=12)

        #Frame for tables grid
        T_frame = Frame(D_frame, bd=2, relief=RIDGE, bg="blue4")
        T_frame.place(x=10, y=70, width=850, height=580)

        scroll_x = Scrollbar(T_frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(T_frame,orient = VERTICAL)
        self.Student_table = ttk.Treeview(T_frame, columns=('Roll No', 'Name', 'Email', 'Gender', 'Contact', 'D.O.B', 'Address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill =X)
        scroll_y.pack(side= RIGHT,fill=Y)
        scroll_x.config(command = self.Student_table.xview)
        scroll_y.config(command = self.Student_table.yview)
        self.Student_table.heading("Roll No",text = "Roll No")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email",text = "Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact")
        self.Student_table.heading("D.O.B", text="D.O.B")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column('Roll No',width = 60)
        self.Student_table.column('Name',width = 150)
        self.Student_table.column('Email',width = 150)
        self.Student_table.column('Gender',width = 60)
        self.Student_table.column('Contact',width = 100)
        self.Student_table.column('D.O.B',width = 80)
        self.Student_table.column('Address',width = 200)
        
        self.Student_table.pack(fill = BOTH,expand =1)
        
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.root.mainloop()

    def add_sudents(self):
        
        if self.Roll_No_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error","All Fields Are Required!!")
        else:
            con = pymysql.connect(host = "localhost", user ="root", password="", database = "test")
            cur = con.cursor()
            try :
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s);", (self.Roll_No_var.get(),self.name_var.get(),
                                                                                self.email_var.get(),self.gender_var.get(),
                                                                                self.contact_var.get(),self.dob_var.get(),
                                                                                self.txt_adrs.get('1.0',END)
                                                                                ))
                cur.execute("insert into marks values (%s,'','');",self.Roll_No_var.get())
                con.commit()
                self.fetch_data()
                self.clear_btn()
                con.close()  
                messagebox.showinfo("Success","Record has been inserted!")
            except:
                messagebox.showwarning("Oops!","Something's Wrong please check data!")    

    def fetch_data(self):
        self.srch_txt.set("")
        self.srch_by.set("")
        con = pymysql.connect(host = "localhost", user ="root", password="", database = "test")
        cur = con.cursor()
        cur.execute("Select * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert("",END,values =row)
                con.commit()
        con.close() 

    def clear_btn(self):
        self.gender_var.set("")
        self.Roll_No_var.set("")    
        self.name_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.marks.set(0)
        self.out_of.set(0)
        self.txt_adrs.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        try:
            self.Roll_No_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.dob_var.set(row[5])
            self.txt_adrs.delete("1.0", END)
            self.txt_adrs.insert(END,row[6])
        except:
            del(row)

    def update_data(self):

        if self.Roll_No_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "Fields Are Empty!!")
        else:
            con = pymysql.connect(host = "localhost", user ="root", password="", database = "test")
            cur = con.cursor()
            cur.execute("update students set name =%s,email =%s,gender =%s,contact =%s, dob =%s ,address =%s where roll_no = %s",( self.name_var.get(),
                                                                            self.email_var.get(),self.gender_var.get(),
                                                                            self.contact_var.get(),self.dob_var.get(),
                                                                            self.txt_adrs.get('1.0',END),
                                                                            self.Roll_No_var.get()
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear_btn()
            con.close() 

    def delete_data(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "Fields Are Empty!!")
        else:
            con = pymysql.connect(host="localhost", user="root",
                                password="", database="test")
            cur = con.cursor()
            cur.execute("delete from students where roll_no = %s", self.Roll_No_var.get())
            con.commit()
            self.fetch_data()
            self.clear_btn()
            con.close()
            messagebox.showinfo("Success","Entry Deleted Successfully!")

    def search_data(self):

        if self.srch_by.get() == "" or self.srch_txt.get() == "":
            messagebox.showwarning("Error","All entries are required!")
        else:    
            con = pymysql.connect(host = "localhost", user ="root", password="", database = "test")
            cur = con.cursor()
            cur.execute("Select * from students where "+str(self.srch_by.get())+" LIKE '%"+str(self.srch_txt.get())+"%' ;")
            rows = cur.fetchall()
            if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                            self.Student_table.insert("",END,values =row)
                    con.commit()
            else:
                messagebox.showinfo("Info",'No Such Student Found!..')        
            con.close()

    def exitfn(self):
        ask = messagebox.askyesno("EXIT!!", "Do You Really Want To Exit?")
        if ask>0:
            self.root.destroy()
        else:
            return  

    def logoutfn(self):
        ask = messagebox.askyesno("LOG OUT!!", "Do You Want To Return To Login Portal?")
        if ask > 0:
            self.root.destroy()
            import login

    def perctgcalc(self):
        if not self.out_of.get() < self.marks.get() and self.out_of.get() > 0:
            self.perctg.set((self.marks.get()/self.out_of.get())*100)
        
    def bgrapgh(self):
        con = pymysql.connect(host = "localhost", user ="root", password="", database = "test")
        cur = con.cursor()
        cur.execute("Select count(*),marks from marks group by marks; ")
        mat = cur.fetchall()
        marklist = [item[1] for item in mat]
        count = [item[0] for item in mat]
        plt.figure()
        plt.bar(marklist, count, width= 0.2, color = 'cyan', edgecolor = 'red')
        plt.title(f"Marks Frequency bar graph")
        plt.ylabel('No. of Students')
        plt.xlabel("Marks")
        plt.show()
            
        con.commit()
        con.close()
        
    def lingrapgh(self):
        con = pymysql.connect(host = "localhost", user ="root", password="", database = "test")
        cur = con.cursor()
        cur.execute("Select roll_no,marks from marks; ")
        mat = cur.fetchall()
        marklist = [item[1] for item in mat]
        rolls = [item[0] for item in mat]
        plt.figure()
        plt.plot(rolls,marklist, marker = 'o')
        plt.title("Marks for each student")
        plt.xlabel("Student Roll No.")
        plt.ylabel("Marks Obtained")
        plt.show()
            
        con.commit()
        con.close()
    
    def sendmail(self):
        
        subject = StringVar()    
        username = StringVar()
        password = StringVar()
        at_marks = BooleanVar()
        
        mailtop = Toplevel()
        mailtop.title('Send Email to Students')
        mailtop.geometry("1000x600+300+80")
        mailtop.resizable(False, False)
        
        idpw_frame = Frame(mailtop, bd=2, relief = RIDGE, bg = 'khaki')
        idpw_frame.place(x=10, y=10,width =400,height = 580)
        
        msg_frame = Frame(mailtop, bd=2, relief = GROOVE, bg = 'khaki')
        msg_frame.place(x=440, y=10,width =540,height = 580)
        
        title = Label(idpw_frame, text='Login Here', font =('Goudy old style', 35,'bold'), bd=2, relief = SUNKEN, bg='azure', fg = '#d77337')
        title.grid(row= 0, column = 0,padx=30,pady=10)
        lbl_user = Label(idpw_frame, text="Username",image =self.user_ico, compound =RIGHT, font=("times new roman", 14, "bold"), bg="khaki", fg="black")
        lbl_user.grid(row =1, column =0 ,pady=10,padx =10, sticky = "w")  
        txt_user = Entry(idpw_frame, textvariable =username, font =('times new roman', 14), bd =2, relief=GROOVE, width = 40) 
        txt_user.grid(row= 2, column =0, padx =10, sticky = "w")
        lbl_pswd = Label(idpw_frame, text="Password",image =self.user_ico, compound = RIGHT, font=("times new roman", 14, "bold"), bg="khaki", fg="black")
        lbl_pswd.grid(row =3, column =0 ,pady=10,padx =10, sticky = "w")  
        txt_pswd = Entry(idpw_frame, textvariable =password, show = '*', font =('times new roman', 14), bd =2, relief=GROOVE, width = 40) 
        txt_pswd.grid(row= 4, column =0, padx =10, sticky = "w")
        
        mark_lbl = Label(idpw_frame, text="Attach Marks", font=("times new roman", 14, "bold"), bg="khaki", fg="black").grid(row= 5, column = 0,padx=10,pady=20, sticky = 'w')
        ymark_radio = Radiobutton(idpw_frame, text='YES', variable = at_marks, value = True, font=("times new roman",13), bg= 'khaki',activebackground= 'khaki', activeforeground = 'green',cursor = 'hand2').place(x=80,y=300)
        nmark_radio = Radiobutton(idpw_frame, text='NO', variable = at_marks, value = False, font=("times new roman",13), bg= 'khaki',activebackground= 'khaki', activeforeground = 'green' ,cursor = 'hand2').place(x=160,y=300)
        
        from_lbl = Label(msg_frame, text="From: ", font=("times new roman", 14, "bold"), bg="khaki", fg="black").place(x=10,y=10)
        from_txt = Entry(msg_frame, textvariable = username, font=("times new roman", 14, "bold"), bg="khaki", fg="black", state = 'disabled',width = 40).place(x=77,y=10)
        sub_lbl = Label(msg_frame, text="Subject: ", font=("times new roman", 14, "bold"), bg="khaki", fg="black").place(x=10, y = 50)
        sub_txt = Entry(msg_frame, textvariable = subject, font =('times new roman', 14), bd =2, relief=GROOVE, width = 55).place(x=20,y=90)
        message_lbl = Label(msg_frame, text="Message: ", font=("times new roman", 14, "bold"), bg="khaki", fg="black").place(x=10, y = 120)
        msg_txt = Text(msg_frame, width=55, height=15, font=("", 13))
        msg_txt.place(x=20,y=150)

        def printinfo():
            con = pymysql.connect(host = "localhost", user ="root", password="", database = "test")
            cur = con.cursor()
            cur.execute("Select S.email, M.marks, M.percentage, S.name from students S natural join marks M;")
            mat = cur.fetchall()
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL('smtp.gmail.com',465,context = context)
            con.commit()
            con.close() 
            try:
                server.login(username.get(),password.get())
                emails = [item[0] for item in mat]
                marks = [item[1] for item in mat]
                percs = [item[2] for item in mat]
                names = [item[3] for item in mat]
                
                if at_marks.get():
                    for i in range (len(names)):
                        try:
                            if (emails[i] != "") and ('.in' in emails[i] and '@' in emails[i]):
                                server.sendmail(username.get(), emails[i],  ("Subject: "+str(subject.get()) + '\nHello {name},\n' + str(msg_txt.get('1.0', END)) +"\nYour Marks are : {marks} | Percentage = {perc} ").format(name=names[i], marks=marks[i], perc=percs[i]))
                        except:
                            messagebox.showerror("Domain Error",'Could not send message to domain : {}'.format(emails[i]))
                            
                else:
                    for i in range(len(names)):
                        try:
                            if (emails[i] != "") and ('.in' in emails[i] and '@' in emails[i]):
                                server.sendmail(username.get(), emails[i],  ("Subject: "+str(subject.get()) + '\nHello {name},\n' +str(msg_txt.get('1.0', END))).format(name=names[i]))
                        except:
                            messagebox.showerror("Domain Error",'Could not send message to domain : {}'.format(emails[i]) )
                    
            except:
                res = messagebox.askretrycancel("Access Denied", "Yousername or Password is not correct !")
                if res:
                    mailtop.destroy()
                    self.sendmail()



        send_btn = Button(msg_frame,text= 'SEND', image = self.mail_ico,compound = RIGHT, width = 80, bg = 'palegreen1', command = printinfo).place(x=300, y = 500)
        
        def confirmstat():
            if '@' in username.get() and ('.com' in username.get() or '.in' in username.get()):
                txt_user.config(state = 'disabled')
                txt_pswd.config(state = 'disabled')
            else:
                ret = messagebox.askretrycancel("Domain Error", "Your Username is not correct!")  
                if ret:
                    self.sendmail()
                mailtop.destroy()   

        conf_btn = Button(idpw_frame, text ="CONFIRM",width =15,bg = "spring green",activebackground = "lime green",command = confirmstat).grid(row = 7,column =0,pady =30)
        
    def marks_win(self):

        def fetch_marks():
            con = pymysql.connect(host = "localhost", user ="root", password="", database = "test")
            cur = con.cursor()
            cur.execute("Select S.roll_no, S.name, S.email, M.marks, M.percentage from students S natural join marks M;")
            rows = cur.fetchall()
            if len(rows)!=0:
                    self.marks_table.delete(*self.marks_table.get_children())
                    for row in rows:
                            self.marks_table.insert("",END,values =row)
                    con.commit()
            con.close() 

        def ins_marks():
            if self.Roll_No_var.get() == "" or self.name_var.get() == "":
                messagebox.showerror("Error", "Student is not selected!!")
                top.destroy()
                self.marks_win()
            else:
                con = pymysql.connect(host = "localhost", user ="root", password="", database = "test")
                cur = con.cursor()
                cur.execute("update marks set marks =%s,percentage =%s where roll_no = %s;",( self.marks.get(),
                                                                                self.perctg.get(),
                                                                                self.Roll_No_var.get()
                                                                                ))
                con.commit()
                self.clear_btn()
                fetch_marks()
                con.close() 

        top = Toplevel()
        top.title("Marks Window!")
        top.geometry("1200x700+120+50")
        top.resizable(False, False)

# Manage Frame 
        Dt_frame = Frame(top, bd =2, relief = GROOVE, bg = 'blue4')
        Dt_frame.place(x=10, y=10, width = 400, height = 660)

        M_title = Label(Dt_frame, text = "Marks & Percentage",relief = GROOVE,font = ("times new roman",25,"bold"),bg = 'lavender', fg = "navy")
        M_title.grid(row =0, columnspan =20,pady =20, padx= 10)

        lbl_roll = Label(Dt_frame, text="Roll No", font=("times new roman", 14, "bold"), bg="blue4", fg="lavender")
        lbl_roll.grid(row =1, column =0 ,pady=10,padx =10, sticky = "w")  
        txt_roll = Entry(Dt_frame, textvariable =self.Roll_No_var, font =('times new roman', 14), bd =2, relief=GROOVE, width = 24, state = 'disabled') 
        txt_roll.grid(row= 1, column =1, pady =10, padx =10, sticky = "w")      

        lbl_name = Label(Dt_frame, text="Name", font=("times new roman", 14, "bold"), bg="blue4", fg="lavender")
        lbl_name.grid(row =2, column =0 ,pady=10,padx =10, sticky = "w")  
        txt_name = Entry(Dt_frame, textvariable =self.name_var, font =('times new roman', 14), bd =2, relief=GROOVE, width = 24, state = 'disabled')
        txt_name.grid(row= 2, column =1, pady =10, padx =10, sticky = "w")

        lbl_mail = Label(Dt_frame, text="Email", font=("times new roman", 14, "bold"), bg="blue4", fg="lavender")
        lbl_mail.grid(row =3, column =0 ,pady=10,padx =15, sticky = "w")  
        txt_mail = Entry(Dt_frame, textvariable =self.email_var, font =('times new roman', 14), bd =2, relief=GROOVE, width = 24, state = 'disabled')
        txt_mail.grid(row= 3, column =1,columnspan =10, pady =10, padx =10, sticky = "w")

        lbl_marks = Label(Dt_frame, text="Marks", font=("times new roman", 14, "bold"), bg="blue4", fg="lavender")
        lbl_marks.grid(row =4, column =0 ,pady=10,padx =15, sticky = "w")  
        txt_marks = Entry(Dt_frame, textvariable =self.marks, font =('times new roman', 14), bd =2, relief=GROOVE, width = 10)
        txt_marks.grid(row= 4, column =1,columnspan =10, pady =10, padx =10, sticky = "w")
        
        lbl_outof = Label(Dt_frame, text="Out OF", font=("times new roman", 14, "bold"), bg="blue4", fg="lavender")
        lbl_outof.grid(row =5, column =0 ,pady=10,padx =15, sticky = "w")  
        txt_outof = Entry(Dt_frame, textvariable = self.out_of, font =('times new roman', 14), bd =2, relief=GROOVE, width =10)
        txt_outof.grid(row= 5, column =1,columnspan =10, pady =10, padx =10, sticky = "w")
    
        conf_btn = Button(Dt_frame, text ="Confirm",width =15,bg = "spring green",activebackground = "lime green",command = self.perctgcalc).place(x=280,y=290)

        lbl_percnt = Label(Dt_frame, text="Percentage", font=("times new roman", 14, "bold"), bg="blue4", fg="lavender")
        lbl_percnt.grid(row =6, column =0 ,pady=10,padx =15, sticky = "w")  
        txt_percnt = Entry(Dt_frame, textvariable =self.perctg, font =('times new roman', 12), bd =2, relief=GROOVE, width = 25, state = 'disabled')
        txt_percnt.grid(row= 6, column =1,columnspan =10, pady =10, padx =10, sticky = "w")

        Mbtn_frame= Frame(Dt_frame,bd=4, relief= RAISED,bg ="deep sky blue")
        Mbtn_frame.place(x=10,y=420, height =220, width = 380)

        insert_btn = Button(Mbtn_frame, text='Update Marks', width=48, height =2, bg="DarkOliveGreen2", activebackground="lime green", command = ins_marks).place(x=10, y=10)
        bargraph_btn = Button(Mbtn_frame,text = 'BARGRAPH', image = self.bar_ico, compound = TOP, width =160,height=130,bg = 'plum2',activebackground = 'purple3',command= self.bgrapgh).place(x=10,y = 60)
        linegraph_btn = Button(Mbtn_frame,text = 'LINEGRAPH', image = self.linegraph_ico, compound = TOP, width =160,height=130,bg = 'plum2',activebackground = 'purple3', command = self.lingrapgh).place(x=190,y = 60)
        
# Table view!
        D_frame = Frame(top, bd=4, relief=RIDGE, bg="blue4")
        D_frame.place(x=420, y=10, width=740, height=660)

        sendmail_btn = Button(D_frame,text= 'SEND MAIL', image = self.mail_ico,compound = RIGHT, width = 120, bg = 'snow', command = self.sendmail).place(x=580,y=8)

        T_frame = Frame(D_frame, bd=2, relief=RIDGE, bg="blue4")
        T_frame.place(x=10, y=60, width=700, height=580)

        scroll_x = Scrollbar(T_frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(T_frame,orient = VERTICAL)
        self.marks_table = ttk.Treeview(T_frame, columns=('Roll No', 'Name', 'Email', 'Marks', 'Percentage'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill =X)
        scroll_y.pack(side= RIGHT,fill=Y)
        scroll_x.config(command = self.marks_table.xview)
        scroll_y.config(command = self.marks_table.yview)
        self.marks_table.heading("Roll No",text = "Roll No")
        self.marks_table.heading("Name", text="Name")
        self.marks_table.heading("Email",text = "Email")
        self.marks_table.heading("Marks", text="Marks")
        self.marks_table.heading("Percentage", text="Percentage")
        self.marks_table['show']='headings'
        self.marks_table.column('Roll No',width = 60)
        self.marks_table.column('Name',width = 110)
        self.marks_table.column('Email',width = 190)
        self.marks_table.column('Marks',width = 80)
        self.marks_table.column('Percentage',width = 80)

        def Mget_cursor(ev):
            cursor_row = self.marks_table.focus()
            contents = self.marks_table.item(cursor_row)
            row = contents['values']
            self.Roll_No_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.marks.set(row[3])
            self.perctg.set(row[4])
            mark= self.marks.get()
            perc =self.perctg.get()
            outta = 0
            if not perc == 0:
                outta =(mark/perc)*100
            if outta - outta//1 > 0.05:
                outta = outta//1 + 1
            elif outta//1 < outta:
                outta = (outta//1)
            self.out_of.set(outta)        
        
        self.marks_table.pack(fill=BOTH, expand=1)
        fetch_marks()
        self.marks_table.bind("<ButtonRelease-1>",Mget_cursor)
     
