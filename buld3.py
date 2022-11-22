
# *************************** LIBRARY MANAGEMENT **************************

import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from datetime import date
from csv import DictWriter
from functools import partial
win = tk.Tk()
win.title("Bishek Yadav")
style = ttk.Style()
create = True
subm = False
start = False
gogo = 0

# Create Data Frame ---------------------------------
def create_DataFrame():
    global student_df
    global suid
    data = pd.read_csv("student.csv", index_col=False)
    student_df = pd.DataFrame(data)
    suid = student_df["Student ID"].tail(1)
    suid = int(suid)+1
#----------------------------------------------------

# Window Frames --------------------

f1 = tk.Frame(win, borderwidth=8)
f1.place(x=0, y=100, width=500, height=400)
f2 = f1
f3 = f2
f4 = f1
# Clear Submit Frame
def clear_frame():
    for widgets in f1.winfo_children():
        widgets.destroy()
#------------------------------------

def heading():
    title_label = ttk.Label(win, text=" Library Management ",font=("Courier", 20))
    title_label.pack(side=tk.TOP)

    # Button Style __________
    style.configure('W.TButton', font =
                ('calibri', 10, 'bold'),
                    foreground = 'black',
                    bordercolor='#00FF00',
                    borderwidth=4
                    )
    style.configure('pay.TButton', font =
                ('calibri', 15, 'bold'),
                    foreground = '#4da6ff',
                    bordercolor='#808080',
                    borderwidth=4,
                    background = "#b3ffff"
                    )
    style.configure('delete.TButton', font =
                ('calibri', 16, 'bold'),
                    foreground = '#ff3300',
                    bordercolor='#ff0000',
                    borderwidth=4,
                    background = "#ff8566"
                    )
    style.map('delete.TButton', foreground = [('active',"#ffffff")])

    # Button 
    d = 110
    c = 35
    student_button1 = ttk.Button(win, text=" Add Student ", style = 'W.TButton', command=add_student)
    student_button1.place(x=c, y=40, width=100, height=50)

    student_button2 = ttk.Button(win, text=" Delete Student ", style = 'W.TButton', command=delete_student)
    student_button2.place(x=c+d*1, y=40, width=100, height=50)

    issue_button = ttk.Button(win, text=" Book issue ", style = 'W.TButton', command=book_issue)
    issue_button.place(x=c+d*2, y=40, width=100,height=50)

    view_button = ttk.Button(win, text=" Submit ", style = 'W.TButton', command=submit_book)
    view_button.place(x=c+d*3, y=40, width=100, height=50)

def add_student():
    clear_frame()
    # Variable ---------
    name_var = tk.StringVar()
    address_var = tk.StringVar()
    number_var = tk.IntVar()
    deposit_var = tk.IntVar()

    # Lable ---------------------

    id_label = ttk.Label(f1, text=" Student ID ",font=("calibri", 13))
    id_label.place(x=10, y=130-110)

    name_label = ttk.Label(f1, text=" Student Name ",font=("calibri", 13))
    name_label.place(x=10, y=130+50-110)

    address_label = ttk.Label(f1, text=" Address ",font=("calibri", 13))
    address_label.place(x=10, y=130+100-110)

    number_label = ttk.Label(f1, text=" Mob no. ",font=("calibri", 13))
    number_label.place(x=10, y=130+150-110)

    deposit_label = ttk.Label(f1, text=" Deposit Money ",font=("calibri", 13))
    deposit_label.place(x=10, y=130+200-110)

    # Student ID Label ----------------
    def idg():
        idg_label = ttk.Label(f1, text=str(suid),width=30, font=("calibri", 15))
        idg_label.place(x=150, y=125-110, width=300, height=30)
    idg()

    # add Student Entry Box ----------------

    name_entry = ttk.Entry(f1, width=30, font=("calibri", 15), textvariable=name_var)
    name_entry.place(x=150, y=125+50-110, width=300, height=30)
    name_entry.focus()

    address_entry = ttk.Entry(f1, width=30, font=("calibri", 15), textvariable=address_var)
    address_entry.place(x=150, y=125+100-110, width=300, height=30)

    number_entry = ttk.Entry(f1, width=30, font=("calibri", 15), textvariable=number_var)
    number_entry.place(x=150, y=125+150-110, width=300, height=30)

    deposit_entry = ttk.Entry(f1, width=20, font=("calibri", 15), textvariable=deposit_var)
    deposit_entry.place(x=150, y=125+200-110, width=300, height=30)

    # Action Fuction
    def action():
        today = date.today()
        name = name_var.get()
        address = address_var.get()
        try:
            number = number_var.get()
            deposit = deposit_var.get()
        except:
            pass
        sid = student_df["Student ID"].tail(1)
        sid = sid = int(sid)+1

        sdata = {"Student ID":sid,
        "Name":str(name),
        "Number":number,
        "Address": str(address),
        "Deposit Money":deposit,
        "Book issue date":np.nan,
        "Name of book":np.nan,
        "Duration":np.nan,
        "Submit date":np.nan,
        "Charge":np.nan,
        "Late fees":np.nan,
        "Total Amount":np.nan}

        student_data = [sdata]

        if not name:
            # If Name is Given
            print("Name is Not Given")
        elif not address :
            # address is Given
            pass
        elif not number :
            # if number is worng or Not given
            pass
        elif not deposit :
            # if Deposit Money is 0 or Non
            pass
        else:
            # Number Check 10 Digit
            da = student_df[student_df["Number"] == number]
            digit = len(str(number))
            if not digit == 10 :
                print("Wronge Number")

            # And Number Exist in dataFrame or Not
            
            elif da.empty:
                    # Then append in csv File
                with open("student.csv", "a", newline="") as f:
                    dict_writer = DictWriter(f, fieldnames=["Student ID","Name","Number","Address","Deposit Money",
                    "Book issue date","Name of book","Duration","Submit date","Charge","Late fees","Total Amount"])
                    dict_writer.writerow(sdata)

                name_entry.delete(0,tk.END)
                address_entry.delete(0,tk.END)
                number_entry.delete(0,tk.END)
                deposit_entry.delete(0,tk.END)
                
                create_DataFrame()
                idg()

                print(name, address, number, deposit)
            else:
                print("The Given Number is Exist")
                print(name, address, number, deposit)


    # add Student Button ------------------

    ok_button = ttk.Button(f1, text=" OK ", style = 'W.TButton', command=action)
    ok_button.place(x=150, y=400-110, width=200, height=70)

def book_issue():
    clear_frame()

    # variable -----------
    student_id_var = tk.StringVar()
    name_of_book_var = tk.StringVar()
    duration_var = tk.StringVar()

    # Book Issue Lable ---------------------

    sid_label = ttk.Label(f2, text=" Student ID ",font=("calibri", 13))
    book_name_label = ttk.Label(f2, text=" Name of Books ",font=("calibri", 13))
    duration_label = ttk.Label(f2, text=" Duration ",font=("calibri", 13))
    agreement_label = ttk.Label(f2, text="                                               AGREEMENT  \n\n<1> per day charge of book Rs. 6/Book \n<2> Late fees Rs. 12/Day \n<3> Note : Late fees increase up to the book price.",font=("calibri", 13))

    sid_label.place(x=10, y=130-110)
    book_name_label.place(x=10, y=130+50-110)
    duration_label.place(x=10, y=130+100-110)
    agreement_label.place(x=10, y=130+30, width=460)

    # Book Issue Entry ----------------------
    sid_entry = ttk.Entry(f2, width=30, font=("calibri", 15), textvariable=student_id_var)
    book_entry = ttk.Entry(f2, width=30, font=("calibri", 15), textvariable=name_of_book_var)
    duration_entry = ttk.Entry(f2, width=30, font=("calibri", 15), textvariable=duration_var)

    sid_entry.place(x=150, y=125-110, width=300, height=30)
    sid_entry.focus()
    book_entry.place(x=150, y=125+50-110, width=300, height=30)
    duration_entry.place(x=150, y=125+100-110, width=300, height=30)

    # Check Box

    # issue Function -----------
    def ok_issue():
        student_id = 0
        duration = 0
        name_of_book = ""
        if student_id_var.get().isdigit():
            student_id = student_id_var.get()
            student_id = int(student_id)
        if duration_var.get().isdigit():
            duration = duration_var.get()
            duration = int(duration)
            name_of_book = name_of_book_var.get()

        # add Deta in DataFrame (duration, name_of_book, issue date)
        # if student id is Exsist
        if str(student_id).isdigit():
            global student_df
            # Student Number ---------------------------------------
            if len(str(student_id)) == 10 :
                sda = student_df[student_df["Number"] == student_id]
                if sda.empty:
                    print("The given Student Number is not Exist")
                else:
                    # Add data in DataFrame
                    today = date.today()
                    ind = sda.index.tolist()[0]
                    student_df.iat[ind,5] = today.strftime("%d/%m/%Y")
                    student_df.iat[ind,6] = name_of_book
                    student_df.iat[ind,7] = duration
                    student_df.iat[ind,8] = np.nan
                    student_df.iat[ind,9] = np.nan
                    student_df.iat[ind,10] = np.nan
                    student_df.iat[ind,11] = np.nan
                    #print(sda)
                    #print(student_df)
                    student_df.to_csv("student.csv",index=False)
                    data = pd.read_csv("student.csv", index_col=False)
                    student_df = pd.DataFrame(data)

                    sid_entry.delete(0,tk.END)
                    book_entry.delete(0,tk.END)
                    duration_entry.delete(0,tk.END)               
                
            # Student ID -----------------------------------------------
            elif len(str(student_id)) > 3 and len(str(student_id)) < 6 :
                sda = student_df[student_df["Student ID"] == student_id]
                if sda.empty:
                    print("The given Student ID is not Exist")
                else:
                    # Add data in DataFrame
                    today = date.today()
                    ind = sda.index.tolist()[0]
                    student_df.iat[ind,5] = today.strftime("%d/%m/%Y")
                    student_df.iat[ind,6] = name_of_book
                    student_df.iat[ind,7] = duration
                    student_df.iat[ind,8] = np.nan
                    student_df.iat[ind,9] = np.nan
                    student_df.iat[ind,10] = np.nan
                    student_df.iat[ind,11] = np.nan
                    #print(sda)
                    #print(student_df)
                    student_df.to_csv("student.csv",index=False)
                    data = pd.read_csv("student.csv", index_col=False)
                    student_df = pd.DataFrame(data)

                    sid_entry.delete(0,tk.END)
                    book_entry.delete(0,tk.END)
                    duration_entry.delete(0,tk.END)
            else:
                print("The Given Student ID or Number is invalid")

    # Issue Button ----------------------------
    delete_button = ttk.Button(f2, text="ISSUE", style = 'W.TButton', command=ok_issue)
    delete_button.place(x=130, y=400-75, width=200, height=40)



def delete_student():
    clear_frame()
    # variavle ----------
    id_num_var = tk.StringVar()

    sid_label = ttk.Label(f3, text=" Student ID ",font=("calibri", 13))
    sid_label.place(x=10, y=125-110, height=30)

    sid_entry = ttk.Entry(f3, width=30, font=("calibri", 15), textvariable=id_num_var)
    sid_entry.place(x=130, y=125-110, width=200, height=30)
    sid_entry.focus()

    # Show Function
    def show(x,yz):
        student_data = student_df[student_df[x] == int(yz)]
        student_data = student_data.head(1)

        # Delete Deta Function ----------
        def del_data():
            global student_df
            ind = student_data.index.tolist()[0]
            student_df = student_df.drop(ind)
            student_df.to_csv("student.csv",index=False)
            data = pd.read_csv("student.csv", index_col=False)
            student_df = pd.DataFrame(data)

            delete_student()

        if not student_data.empty :
            stu_id = student_data.iat[0,0]
            name = student_data.iat[0,1]
            number = student_data.iat[0,2]
            address = student_data.iat[0,3]
            deposit_money = student_data.iat[0,4]
            book_issue_date = student_data.iat[0,5]
            charge  = student_data.iat[0,9]
            late_fees = student_data.iat[0,10]
            total_amount = student_data.iat[0,11]

            # Lable ----------------------
            XX =f"Student ID : {stu_id}\nStudent Name : {name}\nMobile No. {number}\nAddress : {address}\nDeposit Money : {deposit_money}\nBook issue date : {book_issue_date}\nCharge : {charge}\nLate fees : {late_fees}\nTotal Amount : {total_amount}"
            studetail_label = ttk.Label(f3, text=XX,font=("calibri", 13))
            studetail_label.place(x=10, y=65, width=460)

            # DELETE Button -------------------------
            delete_button = ttk.Button(f3, text=" DELETE ", style ='delete.TButton', command=del_data)
            delete_button.place(x=90, y=400-90, width=300, height=50)

    # Ok Function
    def confirm():

        id_num = id_num_var.get()
        if id_num.isdigit():    
            if len(str(id_num)) == 10 :
                # Student Number ---------------------------------------
                x = "Number"
                show(x,id_num)

            elif len(str(id_num)) > 3 and len(str(id_num)) < 6 :
                # Student ID -----------------------------------------------
                x = "Student ID"
                show(x,id_num)       
        else :
            print("The Given Argument is Not Student ID or Number")

    # OK Button -------------------------
    ok1_button = ttk.Button(f3, text=" OK ", style = 'W.TButton', command=confirm)
    ok1_button.place(x=365, y=15, width=100, height=30)


# ************* SUBMIT_BOOK FUNCTION ********************************************

def submit_book():
    clear_frame()
    
    suid_num_var = tk.StringVar()
    pic = tk.PhotoImage(file="right.png" )

    suid_label = ttk.Label(f1, text=" Student ID ",font=("calibri", 13))
    suid_label.place(x=10, y=10, height=30)

    suid_entry = ttk.Entry(f1, width=30, font=("calibri", 15), textvariable=suid_num_var)
    suid_entry.place(x=130, y=10, width=200, height=30)
    suid_entry.focus()

    def show_amount(sub,list1,index_val):
        global start
        if start :
            global li_label,li_label1,li_label2,pic_label,payed,gogo
            li_label.destroy()
            li_label1.destroy()
            li_label2.destroy()
            if gogo == 1 :
                pic_label.destroy()
            elif gogo == 2:
                payed.destroy()

        sid = f"Student ID : {list1[0]}"
        s_n = f"Student Name : {list1[1]}"
        b_n = f"Book Name : {list1[6]}"
        bid = f"Book issue date : {list1[5]}"
        cha = f"Charge : {list1[-3]}"
        lat = f"Late fees : {list1[-2]}"
        tot = f"Total Amount : {list1[-1]}"
        so = sid+"\n"+s_n+"\n"+b_n+"\n"+bid
        so1 = cha+"\n"+lat
        so2 = tot
        
        # Label -----------------------------------------------
        li_label = ttk.Label(f1, text=so,font=("calibri", 14))
        li_label.place(x=10, y=70, width=470, height=100)

        li_label1 = ttk.Label(f1, text=so1,font=("calibri", 15, "bold"))
        li_label1.place(x=10, y=180, width=470, height=50)

        li_label2 = ttk.Label(f1, text=so2,font=("calibri", 17, "bold"))
        li_label2.place(x=10, y=245, width=300, height=50)


        # Button ---------------------------------------------
        if sub == "Yes" :
            pic_label = tk.Label(f1, image=pic)
            pic_label.place(x=260, y=245, height=51, width=50)
            gogo = 1
            co = index_val
        
        def paying(list2,pos):
            global student_df,gogo,pic_label
            today = date.today()
            student_df.iat[pos,8] = today.strftime("%d/%m/%Y")
            student_df.iat[pos,9] = list2[9]
            student_df.iat[pos,10] = list2[10]
            student_df.iat[pos,11] = list2[11]

            student_df.to_csv("student.csv",index=False)
            data = pd.read_csv("student.csv", index_col=False)
            student_df = pd.DataFrame(data)

            pic_label = tk.Label(f1, image=pic)
            pic_label.place(x=260, y=245, height=51, width=50)
            gogo = 1

            payed.destroy()
            
            print(student_df)

        
        if (sub == "No" and index_val != "No"):
            payed = ttk.Button(f1, text=" Pay ", style='pay.TButton', command=partial(paying, list1,index_val))
            payed.place(x=315, y=320, width=150, height=50)
            gogo = 2

        start = True

    def get_student_data(x,yz):
        student_data = student_df[student_df[x] == yz]
        student_data = student_data.head(1)
        
        #print(student_data)

        if student_data.empty:
            print("No Student Data Avelable")
            global start
            if start :
                global li_label,li_label1,li_label2,pic_label,payed,gogo
                li_label.destroy()
                li_label1.destroy()
                li_label2.destroy()
                if gogo == 1 :
                    pic_label.destroy()
                elif gogo == 2:
                    payed.destroy()

        # IF submit == Yas then
        elif str(student_data.iat[0,8]) != "nan":
            pos = student_data.index.tolist()[0]
            li = student_data.values.tolist()
            li = li[0]
            show_amount("Yes", li,pos)

        # IF submit == No then
        elif str(student_data.iat[0,8]) == "nan":
            pos = student_data.index.tolist()[0]
            li = student_data.values.tolist()
            li = li[0]

            date1 = li[5]
            today = date.today()
            if str(student_data.iat[0,5]) == "nan":
                print("The Student is no issue Book.\n Only Add in Data Base")
                li[5] = "No"
                li[6] = "Not issue"
                li[7] = "No"
                li[8] = "Not issue"
                li[9] = 0
                li[10] = 0
                li[11] = 0
                pos = "No"
                show_amount("nan_", li,pos)
            else:
                issue_date = date(int(date1[6:]),int(date1[3:5]),int(date1[0:2]))
                duration = int(li[7])
                num_days = today - issue_date
                num_days = num_days.days      # Number of Days Between issue date and submit date
 
                if num_days <= (duration+1) :
                    charge = num_days*6
                    late_fees = 0
                    total_amount = charge + late_fees
                elif num_days > (duration+1):
                    charge = (duration+1)*6
                    late_fees = (num_days-(duration+1))*12
                    total_amount = charge + late_fees

                li[8] = today.strftime("%d/%m/%Y")
                li[9] = charge
                li[10] = late_fees
                li[11] = total_amount

                show_amount("No", li,pos)
            
                #print(li)

    def check():
        id_num = suid_num_var.get()
        if id_num.isdigit():
            id_num = int(id_num)
            if len(str(id_num)) == 10 :
                # Student Number ---------------------------------------
                x = "Number"
                get_student_data(x,id_num)

            elif len(str(id_num)) > 3 and len(str(id_num)) < 6 :
                # Student ID -----------------------------------------------
                x = "Student ID"
                get_student_data(x,id_num)

            else:
                print("The Given Number is not Student ID or Student Number")
        else:
            print("The Given Text is not Student ID or Student Number")


    amount_button = ttk.Button(f1, text=" Amount ", style = 'W.TButton', command=check)
    amount_button.place(x=365, y=10, width=100, height=30)


create_DataFrame()
heading()

win.maxsize(500, 500)
win.minsize(500, 500)
win.geometry("500x500")
win.mainloop()