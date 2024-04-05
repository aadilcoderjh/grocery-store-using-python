from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from time import strftime
from datetime import date

# ===========================Details Window=======================================
class MAXIMIZE:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Store")
        self.root.geometry("1550x800+0+0")
        self.root.state('zoomed')  # open main_frame_window in maximize state.

# =========================Heading====================================================
        lbltitle = Label(self.root, text="MERRY GROCERY\U0001f600", bd=15, relief=RIDGE
                         , bg="white", fg="red", font=("times new roman", 35, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)


# =========================DateTime=============================================
        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text=string)
            lb1.after(1000, time)

        lb1 = Label(lbltitle, font=('times new roman', 11, 'bold'), background='white', foreground='blue')
        lb1.place(x=0, y=20, width=120, height=40)
        time()

        today = date.today()
        string = today.strftime("%d/%m/%Y")
        lb1.config(text=string)

        lb1 = Label(lbltitle, font=('times new roman', 11, 'bold'), background='white', foreground='blue')
        lb1.place(x=1200, y=20, width=120, height=40)
        time()

 # ===================================Search BY================================================
        DataSearchFrame = Frame(self.root, bd=12, relief=RIDGE, padx=0)
        DataSearchFrame.place(x=0, y=93, width=1360, height=55)

        lblSearch = Label(DataSearchFrame, font=("arial", 15, "bold"), text="Bill No:", bg="red", fg="white",relief=RAISED)
        lblSearch.place(x=0, y=0, width=250, height=30)

        # variable2
        self.searchTxt_var = StringVar()
        txtSearch = Entry(DataSearchFrame, textvariable=self.searchTxt_var, bd=3, relief=RIDGE, width=100,
                          font=("arial", 12, "bold"))
        txtSearch.place(x=270, y=0, width=220, height=30)

        searchBtn = Button(DataSearchFrame, text="SEARCH", padx=9, font=("arial", 12, "bold"), relief=RAISED, bd=5,
                           bg="red", fg="white",
                           command=self.search_data)  # lambda:ApolloPharmacy.search_data)
        searchBtn.place(x=500, y=2, width=180, height=28)

        showAll = Button(DataSearchFrame, text="SHOW ALL", padx=10, font=("arial", 12, "bold"), relief=RAISED, bd=5,
                         bg="red", fg="white",
                         command=self.fetch_data)
        showAll.place(x=700, y=2, width=180, height=28)

        # ======================================================================
        DataFrame = LabelFrame(self.root, bd=15, text="BILL RECEIPTS", font=("arial", 12, "bold"),
                               bg="orangered", fg="white")
        DataFrame.place(x=0, y=150, width=1360, height=545)

        # ====================================Main Table & scrollbar ====================================

        Table_frame = Frame(DataFrame, bd=5, relief=SUNKEN)
        Table_frame.place(x=0, y=0, width=1325, height=505)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.receipt_table = ttk.Treeview(Table_frame, column=("bill_no", "c_phone", "c_name", "c_email", "product",
                                                                "Qty","prices", "total"), xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.receipt_table.xview)
        scroll_y.config(command=self.receipt_table.yview)

        self.receipt_table["show"] = "headings"

        self.receipt_table.heading("bill_no", text="Bill No")
        self.receipt_table.heading("c_phone", text="Mobile No")
        self.receipt_table.heading("c_name", text="Customer Name")
        self.receipt_table.heading("c_email", text="Email")
        self.receipt_table.heading("product", text="Product")
        self.receipt_table.heading("Qty", text="Quantity")
        self.receipt_table.heading("prices", text="Prices")
        self.receipt_table.heading("total", text="Total+Tax")
        self.receipt_table.pack(fill=BOTH, expand=0)

        self.receipt_table.column("bill_no", width=2)
        self.receipt_table.column("c_phone", width=60)
        self.receipt_table.column("c_name", width=50)
        self.receipt_table.column("c_email", width=80)
        self.receipt_table.column("product", width=240)
        self.receipt_table.column("Qty", width=1)
        self.receipt_table.column("prices", width=90)
        self.receipt_table.column("total", width=10)
        self.fetch_data()

    # =======================================================================
    def fetch_data(self):
        conn = sqlite3.connect("mydata.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from RECEIPT")
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.receipt_table.delete(*self.receipt_table.get_children())
            for i in row:
                self.receipt_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def search_data(self):
        conn = sqlite3.connect("mydata.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from RECEIPT where " + str(
            "bill_no  LIKE '" + str(self.searchTxt_var.get()) + "%'"))
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.receipt_table.delete(*self.receipt_table.get_children())
            for i in rows:
                self.receipt_table.insert("", END, values=i)
            conn.commit()
        else:
            messagebox.showinfo("Invalid data", "Data not available")
        conn.close()
        

if __name__ == '__main__':
    root = Tk()
    obj = MAXIMIZE(root)
    root.mainloop()
