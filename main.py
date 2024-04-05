from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk  # pip install pillow
import random, os
from tkinter import messagebox
import tempfile
from time import strftime
import sqlite3
from subprocess import call


class GroceryLogin(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.root.title("Grocery Login")
        self.root.geometry("500x600+0+0")
        self.root.state('zoomed')
        self.root.config(bg='white')
        self.frame = Frame(self.root, bg='white')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.photo = ImageTk.PhotoImage(file='BG1.jpg')
        lb_bg = Label(self.root, image=self.photo)
        lb_bg.place(x=0, y=0, relwidth=1, relheight=1)

        img8 = Image.open("Avatar-grocery.ico")
        img8 = img8.resize((180, 120), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b2 = Button(self.root, image=self.photoimg8, relief=RAISED, borderwidth=3)
        b2.place(x=620, y=160)

        # ==========================Frames=====================================

        self.LoginFrame = LabelFrame(self.root, width=405, height=100, text="Login", font=('arial', 10, 'bold'),
                                      relief='ridge', bg='#c91212', bd=10)
        self.LoginFrame.place(x=500, y=308)

        self.LoginFrame1 = Frame(self.root, width=405, height=80,
                                     relief='ridge', bg='#0d3b0f', bd=10)
        self.LoginFrame1.place(x=500, y=407)

        # ==========================================Labels=================================================
        self.lblUsername = Label(self.LoginFrame, text='Username', font=("arial", 10, "bold"), bg="#c91212",
                                 fg="cornsilk")
        self.lblUsername.place(x=0,y=0)

        self.txtUsername = Entry(self.LoginFrame, font=("arial", 10, "bold"), bd=6, textvariable=self.Username,
                                 width=23)
        self.txtUsername.place(x=80,y=0)

        self.l2 = tk.Label(self.LoginFrame, text="",font=("arial", 10, "bold"), width=10,bg='#c91212',fg='white')

        self.l2.place(x=270,y=5)

        self.txtUsername.bind("<Enter>", self.on_enter)
        self.txtUsername.bind("<Leave>", self.on_leave)

        self.lblPassword = Label(self.LoginFrame, text='Password', font=("arial", 10, "bold"),  bg="#c91212",
                                 fg="cornsilk")
        self.lblPassword.place(x=0,y=33)

        self.txtPassword = Entry(self.LoginFrame, font=("arial", 10, "bold"), show='*', bd=6,
                                 textvariable=self.Password, width=23)
        self.txtPassword.place(x=80,y=33)

        self.l3 = tk.Label(self.LoginFrame, text="",font=("arial", 8, "bold"), width=14,bg='#c91212',fg='white')

        self.l3.place(x=270,y=35)

        self.txtPassword.bind("<Enter>", self.onEnter)
        self.txtPassword.bind("<Leave>", self.onLeave)


        # -==============================================Buttons=========================================================
        self.btnLogin = Button(self.LoginFrame1, text='Login', width=14, font=("arial", 10, "bold"), bg="#0088f7",
                               fg="cornsilk",command=self.Login_System,cursor="hand2")
        self.btnLogin.place(x=0,y=13)

        self.btnReset = Button(self.LoginFrame1, text='Reset', width=14, font=("arial", 10, "bold"), bg="#0088f7",
                               fg="cornsilk", command=self.iReset,cursor="hand2")
        self.btnReset.place(x=130,y=13)

        self.btnExit = Button(self.LoginFrame1, text='Exit', width=14, font=("arial", 10, "bold"), bg="#0088f7",
                              fg="cornsilk", command=self.iExit,cursor="hand2")
        self.btnExit.place(x=260,y=13)

        # ===============================================================================================================
    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())
        if (user == str(123)) and pas == str(123):
            self.Login_window()


        else:
            messagebox.showinfo("Grocery Login System", "Invalid login Details")
            self.Username.set("")
            self.Password.set("")

    def iReset(self):
        self.Username.set("")
        self.Password.set("")

    def iExit(self):
        self.iExit = messagebox.askyesno("Grocery Login System", "Confirm if you want to exit")
        if self.iExit > 0:
            self.root.destroy()
            return

    def on_enter(self, event):
        self.l2.configure(text="HELLO USER")
    def on_leave(self, enter):
        self.l2.configure(text="")
        

    def onEnter(self, event):
        self.l3.configure(text="WRITE PASSWORD")
    def onLeave(self, enter):
        self.l3.configure(text="")
    

    def Login_window(self):
        self.root.withdraw()
        self.SalesWindow = Toplevel(self.root)
        self.obj = Bill_App(self.SalesWindow)


        #Bill================================================
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Grocery Store Software")

        #***************variables**********
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        # Product Categories list
        self.Category=["Select Option","Vegetable","Lifestyle","Mobiles"]

        #SunCatVegetable
        self.SubCatVegetables=["vegies","Snacks","Fruits"]
        self.vegies=["Potato","Cabbage","Capsicum"]
        self.price_Potato=15
        self.price_Cabbage=50
        self.price_Capsicum=40

        self.T_snacks=['Chips','Biscuits','Cold Drinks']
        self.price_Chips=20
        self.price_Biscuits=35
        self.price_Colddrinks=60

        self.Fruits=['Apple','PineApple','Grapes']
        self.price_Apple=100
        self.price_Pine=80
        self.price_Grapes=120

        #SubLifestyle
        self.SubCatLifestyle=["Bath Soap","Face Creame","Hair Oil"]
        self.Bath_Soap=["Lifebuoy","Lux","Santoor","pears"]
        self.price_life=20
        self.price_lux=30
        self.price_Santoor=25
        self.price_pears=30

        self.Face_Creame=['Fair&Lovely','Ponds','Olay','Garnier']
        self.price_fair=80
        self.price_ponds=100
        self.price_Olay=120
        self.price_Garnier=90

        self.Hair_oil=['Parachute','Jasmine','Bajaj']
        self.price_parachute=75
        self.price_Jasmine=50
        self.price_Bajaj=30

        #selfCatMobiles
        self.SubCatMobiles=["iphone","Samsung","Xiaomi","Realme"]
        self.iphone=['iphone 11','iphone 12','iphone 13']
        self.price_I11=65000
        self.price_I12=98000
        self.price_I13=15000

        self.Samsung=['Samsung F22','Samsung M16','Samsung M21']
        self.price_sF22=14999
        self.price_sM16=12999
        self.price_sM21=18000

        self.Xiaomi=['Redmi10','Redmi10sPro','Mi9pro']
        self.price_R10=13000
        self.price_R10s=17000
        self.price_Mi9pro=11999

        self.Realme=['Realme7pro','Realme8','Realme8pro']
        self.price_R7pro=14000
        self.price_R8=16000
        self.price_R8pro=18000

        #image1
        img=Image.open("image/image1.jpg")
        img=img.resize((500,152),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lb1_img=Label(self.root,image=self.photoimg)
        lb1_img.place(x=0,y=0,width=500,height=130)

        #image2
        img_1=Image.open("image/image2.jpeg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lb1_img_1=Label(self.root,image=self.photoimg_1)
        lb1_img_1.place(x=500,y=0,width=459,height=130)

        #image3
        img_2=Image.open("image/image3.jpeg")
        img_2=img_2.resize((500,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lb1_img_2=Label(self.root,image=self.photoimg_2)
        lb1_img_2.place(x=960,y=0,width=439,height=130)

        lb1_title=Label(self.root,text='MERRY\U0001f600GROCERY STORE AND MINI MALL',font=("times new roman",35,"bold"),bg="white",fg="red")
        lb1_title.place(x=0,y=130,width=1400,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text=string)
            lb1.after(1000, time)

        lb1 =Label(lb1_title,font=('times new roman',16,'bold'),background='white',foreground='blue')
        lb1.place(x=15,y=0,width=120,height=45)
        time()

        img9 = Image.open("database.png")
        img9 = img9.resize((40, 40), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(lb1_title, image=self.photoimg9, borderwidth=2,command=self.Maxwindow)
        b1.place(x=1300, y=0)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1370,height=620)

        #Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",14,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lb1_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lb1_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lb1CustName=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Name",bd=4)
        self.lb1CustName.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,stick=W,padx=5,pady=2)

        self.lb1Email=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Email",bd=4)
        self.lb1Email.grid(row=2,column=0,stick=W,padx=5,pady=2)

        def on_click(event):
            self.Email.configure(state=NORMAL)
            self.Email.delete(0, END)

            # make the callback only work once
            self.Email.unbind('<Button-1>', on_click_id)
        self.Email=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.Email.grid(row=2,column=1,stick=W,padx=5,pady=2)

        self.Email.insert(0, "example123@gmail.com")
        self.Email.configure(state=DISABLED)
        on_click_id = self.Email.bind('<Button-1>', on_click)


        #product Frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",14,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=580,height=140)

        #Category
        self.lb1Category=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select categories ",bd=4)
        self.lb1Category.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"),width=15,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


        #sub category
        self.lb1SubCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Sub categories ",bd=4)
        self.lb1SubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=15,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,stick=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #Product Name
        self.lb1product=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lb1product.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=15,state="readonly")
        self.ComboProduct.grid(row=2,column=1,stick=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lb1price=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Price",bd=4)
        self.lb1price.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=15,state="readonly")
        self.ComboPrice.grid(row=0,column=3,stick=W,padx=5,pady=2)

        #Qty
        self.lb1Qty=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select Quantity",bd=4)
        self.lb1Qty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=15,state="readonly")
        self.ComboQty.grid(row=1,column=3,stick=W,padx=5,pady=2)

        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10,bg="white")
        MiddleFrame.place(x=0,y=150,width=980,height=340)

        #image4
        img4=Image.open("image/image4.jpeg")
        img4=img4.resize((450,240),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lb1_img4=Label(MiddleFrame,image=self.photoimg4)
        lb1_img4.place(x=0,y=0,width=450,height=220)

        #image5
        img_5=Image.open("image/image5.jpg")
        img_5=img_5.resize((490,230),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        lb1_img_5=Label(MiddleFrame,image=self.photoimg_5)
        lb1_img_5.place(x=470,y=0,width=460,height=220)

        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=958,y=15,width=500,height=40)

        self.lb1Bill=Label(Search_Frame,font=("arial",12,"bold"),bg="red",fg="white",text="Bill No.")
        self.lb1Bill.grid(row=0,column=0,stick=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=29)
        self.txt_Entry_Search.grid(row=0,column=1,stick=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)

        #RightFrame bill area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=960,y=45,width=380,height=340)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",11,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",14,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=384,width=1340,height=130)

        self.lb1SubTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Sub Total",bd=4)
        self.lb1SubTotal.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=20,textvariable=self.sub_total)
        self.EntrySubTotal.grid(row=1,column=1,stick=W,padx=5,pady=2)

        self.lb1_tax=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="GST",bd=4)
        self.lb1_tax.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=20,textvariable=self.tax_input)
        self.txt_tax.grid(row=2,column=1,stick=W,padx=5,pady=2)

        self.lb1AmountTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Total",bd=4)
        self.lb1AmountTotal.grid(row=3,column=0,stick=W,padx=5,pady=2)

        self.EntryAmountTotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=20,textvariable=self.total)
        self.EntryAmountTotal.grid(row=3,column=1,stick=W,padx=5,pady=2)

        #Buttom Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngeneratebill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.Btngeneratebill.grid(row=0,column=1)

        self.BtnSavebill=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnSavebill.grid(row=0,column=3)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnPrint.grid(row=0,column=4)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnClear.grid(row=0,column=5)

        self.BtnExit=Button(Btn_Frame,command=self.destroyi,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnExit.grid(row=0,column=6)
        self.welcome()
        self.l=[]
        self.temp=[]
        self.temp1=[]
    #*************************Function Declaration*************
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        self.temp.append(self.product.get())
        print(self.temp)
        self.temp1.append(str(self.prices.get()))
        print(self.temp1)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

        self.p=','.join(self.temp)
        print(self.p)
        self.p1=','.join(self.temp1)
        print(self.p1)

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"WELCOME TO GROCERY STORE & MINI MALL")
        self.textarea.insert(END,'\n*******************************************')
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n=======================================")
        self.textarea.insert(END,f"\n Products\t\t QTY\t Price")
        self.textarea.insert(END,"\n=======================================\n")



    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please add to cart product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ***********************************")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n***********************************")

        if len(self.c_phone.get())!=10:
            messagebox.showerror("Error","Please Enter 10 Digit No.")    

    def save_bill(self):
            
            if not self.c_phone.get():
                    messagebox.showerror("Error","Mobile no field required")
            elif not self.c_name.get():
                    messagebox.showerror("Error","Customer Name required")
            elif not self.c_email.get():
                    messagebox.showerror("Error","Email field required")
            elif not self.product.get():
                    messagebox.showerror("Error","Product Name required")                
            else:
                    try:
                        conn=sqlite3.connect("mydata.db")
                        my_cursor=conn.cursor() 
                        messagebox.showinfo("INFO","Database created and Successfully Connected to SQLite.")
                        my_cursor.execute("""CREATE TABLE IF NOT EXISTS RECEIPT(bill_no INTEGER PRIMARY KEY,
                                                                                                                c_phone INTEGER,
                                                                                                                c_name TEXT,
                                                                                                                c_email TEXT,
                                                                                                                product TEXT,
                                                                                                                Qty TEXT,
                                                                                                                prices TEXT,
                                                                                                                total TEXT ) """)
                        
                        my_cursor.execute("INSERT INTO RECEIPT VALUES(?,?,?,?,?,?,?,?)",
                            [int(self.bill_no.get()),int(self.c_phone.get()),self.c_name.get(),self.c_email.get(),self.p,
                            self.qty.get(),self.p1,self.total.get()])
                        conn.commit()
                        conn.close()
                        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
                    except Exception as ex:
                        messagebox.showinfo("INFO",ex)


            if op>0:
                self.bill_data=self.textarea.get(1.0,END)
                f1=open('Bills/'+str(self.bill_no.get())+".txt",'w')
                f1.write(self.bill_data)
                op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()}saved successfully")
                f1.close()                    



    def iprint(self):

        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")



    def find_bill(self):
        found="no"
        for i in os.listdir("Bills"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'Bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")
                

        
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()

    def Categories(self,event=""):
        if self.Combo_Category.get()=="Vegetable":
            self.ComboSubCategory.config(value=self.SubCatVegetables)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Lifestyle":
            self.ComboSubCategory.config(value=self.SubCatLifestyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="vegies":
            self.ComboProduct.config(value=self.vegies)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Snacks":
            self.ComboProduct.config(value=self.T_snacks)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Fruits":
            self.ComboProduct.config(value=self.Fruits)
            self.ComboProduct.current(0)

        #Lifestyle
        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.Bath_Soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face Creame":
            self.ComboProduct.config(value=self.Face_Creame)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)

        #Mobiles
        if self.ComboSubCategory.get()=="iphone":
            self.ComboProduct.config(value=self.iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Xiaomi":
            self.ComboProduct.config(value=self.Xiaomi)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Realme":
            self.ComboProduct.config(value=self.Realme)
            self.ComboProduct.current(0)


    def price(self,event=""):
        #vegies
        if self.ComboProduct.get()=="Potato":
            self.ComboPrice.config(value=self.price_Potato)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Cabbage":
            self.ComboPrice.config(value=self.price_Cabbage)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Capsicum":
            self.ComboPrice.config(value=self.price_Capsicum)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Snacks
        if self.ComboProduct.get()=="Chips":
            self.ComboPrice.config(value=self.price_Chips)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Biscuits":
            self.ComboPrice.config(value=self.price_Biscuits)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Cold Drinks":
            self.ComboPrice.config(value=self.price_Colddrinks)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Fruits
        if self.ComboProduct.get()=="Apple":
            self.ComboPrice.config(value=self.price_Apple)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="PineApple":
            self.ComboPrice.config(value=self.price_Pine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Grapes":
            self.ComboPrice.config(value=self.price_Grapes)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Bath Soap
        if self.ComboProduct.get()=="Lifebuoy":
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_Santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="pears":
            self.ComboPrice.config(value=self.price_pears)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Face creame
        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_Olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_Garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Hair oil
        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_parachute)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jasmine":
            self.ComboPrice.config(value=self.price_Jasmine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_Bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #iphone
        if self.ComboProduct.get()=="iphone 11":
            self.ComboPrice.config(value=self.price_I11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="iphone 12":
            self.ComboPrice.config(value=self.price_I12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="iphone 13 ":
            self.ComboPrice.config(value=self.price_I13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Samsung
        if self.ComboProduct.get()=="Samsung F22":
            self.ComboPrice.config(value=self.price_sF22)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M16":
            self.ComboPrice.config(value=self.price_sM16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M21":
            self.ComboPrice.config(value=self.price_sM21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Redmi
        if self.ComboProduct.get()=="Redmi10":
            self.ComboPrice.config(value=self.price_R10)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Redmi10sPro":
            self.ComboPrice.config(value=self.price_R10s)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mi9pro":
            self.ComboPrice.config(value=self.price_Mi9pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #realme
        if self.ComboProduct.get()=="Realme7pro":
            self.ComboPrice.config(value=self.price_R7pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Realme8":
            self.ComboPrice.config(value=self.price_R8)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Realme8pro":
            self.ComboPrice.config(value=self.price_R8pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

    def destroyi(self):
        self.destroyi = messagebox.askyesno("Merry Grocery Store ","Confirm if you want to exit")
        if self.destroyi > 0:
            self.root.destroy()
            return

    def Maxwindow(self):
        #root.destroy()
        call(['python','maximize.py'])


if __name__ == '__main__':
    root = Tk()
    obj = GroceryLogin(root)
    root.mainloop()
