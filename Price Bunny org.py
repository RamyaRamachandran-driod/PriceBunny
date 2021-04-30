from tkinter import *
import time
import os
from tkinter import ttk
import cv2
from plyer import notification
import tkinter.ttk as ttk
import csv
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar import DateEntry
import datetime
from pandas import DataFrame as df
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from notification import notifyme

global username_x
global password_x
global name_x
global occu_x


def month_tracker(month):
    switch = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',
    }
    return switch.get(month, 1)


def main_screen():
    global root
    # Main Window
    root = Tk()
    root.title("PriceBunny - Home")
    root.geometry("680x610")
    root.iconbitmap("icon.ico")
    bg = PhotoImage(file="Web_Photo_Editor.png")
    my_label = Label(root, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    Label(text="Choose Login Or Register", bg="gold", width="300", height="2", font=("Times New Roman", 14)).pack()
    Label(text="").pack(pady=150)
    Button(text="Login", height="2", width="30", font=("Times New Roman", 16), command=login,bg="black",fg="white").pack()
    #Label(text="").pack(pady=30)
    Button(text="Register", height="2", width="30", font=("Times New Roman", 16), command=registration,bg="black",fg="white").pack(pady=30)

    root.mainloop()


def registration():
    global username
    global password
    global name
    global occu

    global username_entry
    global password_entry
    global name_entry
    global occu_entry

    global rscreen

    rscreen = Toplevel(root)
    rscreen.title("PriceBunny - Registration")
    rscreen.geometry("500x500")
    rscreen.iconbitmap("icon.ico")

    bg = PhotoImage(file="REG (2).png")
    my_label = Label(rscreen, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    username = StringVar()
    password = StringVar()
    name = StringVar()
    occu = StringVar()

    Label(rscreen, text="Plug in your details!", bg="pink", height="2", width="45", font=("Times New Roman", 15)).pack()
    Label(rscreen, text="").pack(pady=50)

    name_label = Label(rscreen, text="Enter your Name", font=("times new roman", 14))
    name_label.pack()
    name_entry = Entry(rscreen, width="50", textvariable=name)
    name_entry.pack()

    occu_label = Label(rscreen, text="Enter your Occupation", font=("times new roman", 14))
    occu_label.pack()
    occu_entry = Entry(rscreen, width="50", textvariable=occu)
    occu_entry.pack()

    username_label = Label(rscreen, text="A fancy Username ", font=("times new roman", 14))

    username_label.pack()
    username_label.pack()
    username_label.pack()
    username_label.pack()
    username_label.pack()
    username_label.pack()
    username_label.pack()
    username_label.pack()

    username_entry = Entry(rscreen, width="50", textvariable=username)
    username_entry.pack()
    username_label.pack()
    username_label.pack()
    username_label.pack()
    username_label.pack()
    username_label.pack()
    username_label.pack()

    password_label = Label(rscreen, text="A fancier Password", font=("times new roman", 14))
    password_label.pack()
    password_label.pack()
    password_label.pack()
    password_label.pack()
    password_label.pack()
    password_label.pack()
    password_label.pack()

    password_entry = Entry(rscreen, width="50", textvariable=password, show='*')
    password_entry.pack()
    password_entry.pack()
    password_entry.pack()
    password_entry.pack()

    Label(rscreen, text="").pack()

    Button(rscreen, text="Register!", width=10, height=1, bg="black",fg="white", font=("times new roman", 14),
           command=user_rinfo).pack()

    rscreen.mainloop()


# to save user information
def user_rinfo():
    global username_x
    global password_x
    global name_x
    global occu_x
    username_x = username.get()
    password_x = password.get()
    name_x = name.get()
    occu_x = occu.get()
    list_of_files = os.listdir()

    def username_taken():
        def delete_username_taken_screen():
            username_taken_screen.destroy()

        username_taken_screen = Toplevel(rscreen)
        username_taken_screen.title("PriceBunny - Oops!")
        username_taken_screen.geometry("250x200")
        username_taken_screen.iconbitmap("icon.ico")
        bg = PhotoImage(file="goldBG.png")
        my_label = Label(username_taken_screen, image=bg)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)

        Label(username_taken_screen, text="Username Taken", font=("Times New Roman bold", 14), bg="white", height="2",
              width="36").pack()
        Button(username_taken_screen, text="Retry", font=("Times New Roman bold", 14), bg="Black", fg="white",
               command=delete_username_taken_screen).pack(pady=30)
        username_taken_screen.mainloop()

    if username_x not in list_of_files:
        file = open(username_x, "w+")
        file.write(name_x.capitalize() + "\n")
        file.write(occu_x.capitalize().casefold() + "\n")
        file.write(username_x + "\n")
        file.write(password_x)

        file.close()

        Label(rscreen, text="Registration Success!", bg="light green", font=("times new roman", 13)).pack()  #########
        time.sleep(1)
        name_entry.delete(0, END)
        occu_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        username_taken()

    rscreen.destroy()


def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    login_screen = Toplevel(root)
    login_screen.title("PriceBunny - Login")
    login_screen.geometry("400x400")
    login_screen.iconbitmap("icon.ico")

    bg = PhotoImage(file="Price BunnyLOGIN.png")
    my_label = Label(login_screen, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(login_screen, text="Please enter details below to login", bg="black", fg="white", height="2", width="45",
          font=("times new roman", 14)).pack()
   # Label(login_screen, text="").pack(pady=10)

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Enter your Username: ", font=("times new roman", 13)).pack(pady=10)
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()

   # Label(login_screen, text="").pack(pady=10)
    Label(login_screen, text="Enter your Password", font=("times new roman", 13)).pack(pady=10)
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    #Label(login_screen, text="").pack(pady=5)
    Button(login_screen, text="Login", width=10, height=1, font=("times new roman", 13),
           command=login_verification,bg="black",fg="white").pack(pady=10)
    login_screen.mainloop()


def login_verification():
    print("working...")
    login_verify()


def login_verify():
    global username_x
    global list_of_files
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    # a list of registered users
    list_of_files = os.listdir()

    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            username_x = username1
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("PriceBunny - Login Success")
    login_success_screen.geometry("250x200")
    login_success_screen.iconbitmap("icon.ico")
    bg = PhotoImage(file="goldBG.png")
    my_label = Label(login_success_screen, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(login_success_screen, text="Login Success", font=("Times New Roman bold", 14), bg="white", height="2",
          width="36").pack()

    Button(login_success_screen, text="Okay!", font=("Times New Roman bold", 14), bg="Black", fg="white",
           command=delete_login_success).pack(pady=30)
    login_success_screen.mainloop()


def delete_login_success():
    login_success_screen.destroy()
    dashboard()
    notifyme("HEY USER!!! Have you done any shopping today?",
             "If YES, don't forget to enter your expenses in PriceBunny :) ")

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("PriceBunny - Oops!")
    password_not_recog_screen.geometry("250x200")
    password_not_recog_screen.iconbitmap("icon.ico")
    bg = PhotoImage(file="goldBG.png")
    my_label = Label(password_not_recog_screen, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(password_not_recog_screen, text="Invalid Password", font=("Times New Roman bold", 14), bg="white", height="2",
          width="36").pack()
    Button(password_not_recog_screen, text="Retry", font=("Times New Roman bold", 14), bg="Black", fg="white",
           command=delete_password_not_recognised).pack(pady=30)

    password_not_recog_screen.mainloop()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("PriceBunny - Oops!")
    user_not_found_screen.geometry("250x200")
    user_not_found_screen.iconbitmap("icon.ico")
    bg = PhotoImage(file="goldBG.png")
    my_label = Label(user_not_found_screen, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    Label(user_not_found_screen, text="User Not Found", font=("Times New Roman bold", 14), bg="white", height="2",
          width="36").pack()
    Button(user_not_found_screen, text="Retry", font=("Times New Roman bold", 14), bg="Black", fg="white",
           command=delete_user_not_found_screen).pack(pady=30)
    user_not_found_screen.mainloop()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# *************************************************************************************************************************************************
def dashboard():
    login_screen.destroy()
    root.wm_state("icon")
    global bal

    def profile():
        def close():
            prof.destroy()

        def cp():
            global cp
            cp = Toplevel(prof)
            cp.title("PriceBunny - Change Password")
            cp.geometry("500x450")
            bg = PhotoImage(file="goldBG.png")
            my_label = Label(cp, image=bg)
            my_label.place(x=0, y=0, relwidth=1, relheight=1)
            Label(cp, text="For security reasons, please fill in details", font=("Times New Roman bold", 16),
                  bg="white", height="3", width="60", justify=LEFT).pack()

            def occup_not_recognised():
                def delete_occup_not_recognised():
                    occup_not_recog_screen.destroy()

                occup_not_recog_screen = Toplevel(cp)
                occup_not_recog_screen.title("PriceBunny - Oops!")
                occup_not_recog_screen.geometry("250x200")
                occup_not_recog_screen.iconbitmap("icon.ico")
                bg = PhotoImage(file="goldBG.png")
                my_label = Label(occup_not_recog_screen, image=bg)
                my_label.place(x=0, y=0, relwidth=1, relheight=1)

                Label(occup_not_recog_screen, text="Invalid Occupation", font=("Times New Roman bold", 14), bg="white",
                      height="2", width="36").pack()
                Button(occup_not_recog_screen, text="Retry", font=("Times New Roman bold", 14), bg="Black", fg="white",
                       command=delete_occup_not_recognised).pack(pady=30)
                occup_not_recog_screen.mainloop()

            def username_not_found():
                def delete_username_not_found_screen():
                    username_not_found_screen.destroy()

                username_not_found_screen = Toplevel(cp)
                username_not_found_screen.title("PriceBunny - Oops!")
                username_not_found_screen.geometry("250x200")
                username_not_found_screen.iconbitmap("icon.ico")
                bg = PhotoImage(file="goldBG.png")
                my_label = Label(username_not_found_screen, image=bg)
                my_label.place(x=0, y=0, relwidth=1, relheight=1)

                Label(username_not_found_screen, text="Username Not Found", font=("Times New Roman bold", 14),
                      bg="white", height="2", width="36").pack()
                Button(username_not_found_screen, text="Retry", font=("Times New Roman bold", 14), bg="Black",
                       fg="white", command=delete_username_not_found_screen).pack(pady=30)
                username_not_found_screen.mainloop()

            def change_pwd():
                def password_changes_done():
                    def go_back():
                        cpwd.destroy()
                        cp.destroy()
                        prof.destroy()

                    new_password = newp_entry.get()
                    file = open(username2, "r")
                    lines = file.read().splitlines()
                    old_password = lines[3].strip()
                    print("Old password: ", old_password)
                    lines[3] = new_password
                    print("Changed password: ", lines[3])
                    file.close()
                    file = open(username2, "r+")
                    file.write("\n".join(lines))
                    file.flush()
                    file.close()
                    Label(cpwd, text="Password Changed!", bg="light green", font=("times new roman", 13)).pack()
                    time.sleep(1)
                    Button(cpwd, text="Go back to Dashboard", font=("Times New Roman bold", 14), bg="Black", fg="white",
                           command=go_back).pack(pady=30)

                cpwd = Toplevel(cp)
                cpwd.title("PriceBunny - Modify Password")
                cpwd.geometry("500x450")
                bg = PhotoImage(file="goldBG.png")
                my_label = Label(cpwd, image=bg)
                my_label.place(x=0, y=0, relwidth=1, relheight=1)

                Label(cpwd, text="Please fill in your new password", font=("Times New Roman bold", 16), bg="white",
                      height="3", width="60", justify=LEFT).pack()

                newp_entry = StringVar()

                newp_label = Label(cpwd, text="New password: ", font=("times new roman", 15)).pack(pady=10)
                newp_cp_entry = Entry(cpwd, textvariable=newp_entry, show="*")
                newp_cp_entry.pack()

                Button(cpwd, text="Done", font=("Times New Roman bold", 14), bg="Black", fg="white",
                       command=password_changes_done).pack(pady=30)

                cpwd.mainloop()

            def change():
                global username2
                global list_of_files
                username2 = username_verify.get()
                occup2 = occup_verify.get()

                username_cp_entry.delete(0, END)
                occup_cp_entry.delete(0, END)

                # a list of registered users
                list_of_files = os.listdir()

                if username2 in list_of_files:
                    file1 = open(username2, "r")
                    verify = file1.read().splitlines()
                    if occup2.casefold() in verify:
                        username_x = username2

                        change_pwd()  # password changing

                    else:
                        occup_not_recognised()  # wrong occupation
                else:
                    username_not_found()

            username_verify = StringVar()
            occup_verify = StringVar()

            user_label = Label(cp, text="Enter your Username: ", font=("times new roman", 13)).pack(pady=10)
            username_cp_entry = Entry(cp, textvariable=username_verify)
            username_cp_entry.pack()

            Label(prof, text="").pack()

            occup_label = Label(cp, text="Enter your Occupation", font=("times new roman", 13)).pack(pady=10)
            occup_cp_entry = Entry(cp, textvariable=occup_verify)
            occup_cp_entry.pack()

            Label(prof, text="").pack()

            Button(cp, text="Done", width="25", height="3", font=("times new roman bold", 10), bg="black", fg="white",
                   command=change).pack(pady=30)

            cp.mainloop()

        # profile
        global prof
        prof = Toplevel(dash)
        prof.title("PriceBunny - User Profile")
        prof.geometry("500x450")
        prof.iconbitmap("icon.ico")
        bg = PhotoImage(file="goldBG.png")
        my_label = Label(prof, image=bg)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)

        file = open(username_x, "r")
        x = file.readlines()
        output = "Hi " + x[0].strip() + "!!" + " \nOccupation:\t" + x[1].strip() + "\nUsername:\t" + x[
            2].strip() + "\nPsst! Your password is protected!"

        Label(prof, text=output, font=("Times New Roman bold", 12), bg="white", height="5", width="56",
              justify=LEFT).pack()
        Button(prof, text="Change Password", font=("Times New Roman bold", 12), bg="Black", fg="white", height="3",
               width="20", justify=LEFT, command=cp).pack(pady=70)
        Button(prof, text="Close", font=("Times New Roman bold", 12), bg="Black", fg="white", height="3", width="20",
               command=close).pack(pady=30)

        prof.mainloop()

    def options1():
        op = Toplevel(dash)
        op.title("PriceBunny - Your Expenses")
        op.iconbitmap("icon.ico")
        # op.configure(bg="gold")
        op.geometry("350x300")

        bg = PhotoImage(file="goldBG.png")
        my_label = Label(op, image=bg)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)

        def add_income():
            GUI = Toplevel(op)
            GUI.title('PriceBunny')
            GUI.iconbitmap("icon.ico")
            GUI.geometry('600x540')

            bg = PhotoImage(file="goldBG(1).png")
            Label(GUI, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

            LDate = ttk.Label(GUI, text='Date', font=(None, 18))
            LDate.grid(row=0, column=0, padx=5, pady=5, sticky='w')
            # to create the tab give row and column with pad lenght 5 in x axis and 5 in y axis

            EDate = DateEntry(GUI, width=19, background='pink', foreground='white', font=(None, 18))
            EDate.grid(row=0, column=1, padx=5, pady=5, sticky='w')

            # Tab 3 (Expense)
            LIncome = ttk.Label(GUI, text='Income', font=(None, 18))
            LIncome.grid(row=2, column=0, padx=5, pady=5, sticky='w')
            # to create the tab give row and column with pad lenght 5 in x axis and 5 in y axis

            Income = StringVar()

            EIncome = ttk.Entry(GUI, textvariable=Income, font=(None, 18))
            EIncome.grid(row=2, column=1, padx=5, pady=5, sticky='w')

            # to create table which saves the user data
            TVList = ['Date', 'Income', 'Description']
            TVExpense = ttk.Treeview(GUI, column=TVList, show='headings', height=7)
            for i in TVList:
                TVExpense.heading(i, text=i.title())
            TVExpense.grid(row=4, column=0, padx=5, pady=5, sticky='w', columnspan=3)

            def AddIncome():
                x = EDate.get()
                y = '-'
                z = Income.get()
                expense = 0
                tracker(x, z, expense, y)
                data = [x, z, y]
                TVExpense.insert('', 'end', values=data)

            BF1Add = Button(GUI, text='Add', command=AddIncome,bg="black",fg="white",font=("times new roman bold", 12))
            BF1Add.grid(row=3, column=1, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

            def checkIf(month):
                try:
                    df = pd.read_csv(f'{month}.csv')
                    return df.empty
                except:
                    return True

            def tracker(date1, income, expense, particular="-"):
                data = {
                    'Date': date1,
                    'Description': particular,
                    'Income': income,
                    'Expenses': expense
                }
                database = df.from_dict(data, orient='index')
                database = database.transpose()
                decide = 'a'
                check = False
                year, month, date = date1[5:7], date1[0], date1[2:4]
                month = int(month)
                curr_month = month_tracker(month)
                if checkIf(curr_month):
                    decide = 'w'
                    check = True
                database.to_csv(f'{curr_month}.csv', mode=decide, header=check, index=False)

            GUI.mainloop()

        def addexpense1():
            GUI = Toplevel(op)
            GUI.title('PriceBunny')
            GUI.iconbitmap("icon.ico")
            GUI.geometry('600x540')

            bg = PhotoImage(file="goldBG(1).png")
            Label(GUI, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

            LDate = ttk.Label(GUI, text='Date', font=(None, 18))
            LDate.grid(row=0, column=0, padx=5, pady=5, sticky='w')
            # to create the tab give row and column with pad lenght 5 in x axis and 5 in y axis

            EDate = DateEntry(GUI, width=19, background='pink', foreground='white', font=(None, 18))
            EDate.grid(row=0, column=1, padx=5, pady=5, sticky='w')

            # Tab 2 (Title)
            LTitle = ttk.Label(GUI, text='Description', font=(None, 18))
            LTitle.grid(row=1, column=0, padx=5, pady=5, sticky='w')
            # to create the tab give row and column with pad lenght 5 in x axis and 5 in y axis

            Title = StringVar()

            ETitle = ttk.Entry(GUI, textvariable=Title, font=(None, 18))
            ETitle.grid(row=1, column=1, padx=5, pady=5, sticky='w')

            # Tab 3 (Expense)
            LExpense = ttk.Label(GUI, text='Expense', font=(None, 18))
            LExpense.grid(row=2, column=0, padx=5, pady=5, sticky='w')
            # to create the tab give row and column with pad lenght 5 in x axis and 5 in y axis

            Expense = StringVar()

            EExpense = ttk.Entry(GUI, textvariable=Expense, font=(None, 18))
            EExpense.grid(row=2, column=1, padx=5, pady=5, sticky='w')

            # to create table which saves the user data
            TVList = ['Date', 'Description', 'Expense']
            TVExpense = ttk.Treeview(GUI, column=TVList, show='headings', height=7)
            for i in TVList:
                TVExpense.heading(i, text=i.title())
            TVExpense.grid(row=4, column=0, padx=5, pady=5, sticky='w', columnspan=3)

            def AddExpense():
                a = EDate.get()
                b = Title.get()
                c = Expense.get()
                income = 0
                tracker(a, income, c, b)
                data = [a, b, c]
                TVExpense.insert('', 'end', values=data)

            # create add button
            BF1Add = Button(GUI, text='Add', command=AddExpense, bg="black", fg="white",font=("times new roman bold", 12))
            BF1Add.grid(row=3, column=1, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
            def checkIf(month):
                try:
                    df = pd.read_csv(f'{month}.csv')
                    return df.empty
                except:
                    return True

            def tracker(date1, income=0, expense=0, particular=" "):
                data = {
                    'Date': date1,
                    'Description': particular,
                    'Income': income,
                    'Expenses': expense
                }
                database = df.from_dict(data, orient='index')
                database = database.transpose()
                decide = 'a'
                check = False
                year, month, date = date1[5:7], date1[0], date1[2:4]
                month = int(month)
                curr_month = month_tracker(month)
                if checkIf(curr_month):
                    decide = 'w'
                    check = True
                database.to_csv(f'{curr_month}.csv', mode=decide, header=check, index=False)

            GUI.mainloop()

        def close():
            op.destroy()

        # op.iconbitmap("Price Bunny/icon.ico")
        Button(op, text="Add Income", width="25", height="3", font=("times new roman bold", 12), bg="black", fg="white",
               command=add_income).pack(pady=5)
        Button(op, text="Add Expense", width="25", height="3", font=("times new roman bold", 12), bg="black",
               fg="white", command=addexpense1).pack(pady=5)
        Button(op, text="Close", width="20", height="2", font=("times new roman bold", 12), bg="black", fg="white",
               relief=RAISED, command=close).pack(pady=20)

        op.mainloop()

    def options2():
        global bal
        op = Toplevel(dash)
        op.title("PriceBunny - Your Expenses")
        op.iconbitmap("icon.ico")
        # op.configure(bg="gold")
        op.geometry("350x300")

        bg = PhotoImage(file="goldBG.png")
        my_label = Label(op, image=bg)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)

        inc = 0
        exp = 0
        lab = 0
        bal = 0

        def total_balance_get():
            global bal
            global months
            global inc
            global exp
            global lab
            root = Toplevel(op)
            root.title('Balance')
            root.iconbitmap("icon.ico")
            root.geometry("510x300")

            bg = PhotoImage(file="goldBG.png")
            my_label = Label(root, image=bg)
            my_label.place(x=0, y=0, relwidth=1, relheight=1)

            def change():
                root.destroy()
                selected()

            def selected():
                global bal
                Bal = []
                curr_month = months
                # curr_month = month_tracker(month)
                get = pd.read_csv(f'{curr_month}.csv', index_col='Date')
                get.dropna(inplace=True)
                Balance = (get['Income'].sum() - get['Expenses'].sum())
                for month in months[0:months.index(curr_month) + 1]:
                    try:
                        got = pd.read_csv(f'{curr_month}.csv', index_col='Date')
                        got.dropna(inplace=True)
                        inc = got['Income'].sum()
                        exp = got['Expenses'].sum()
                        lab = inc - exp
                        Bal.append(lab)
                    except FileNotFoundError:
                        pass
                bal = sum(Bal)

                root1 = Toplevel(op)
                root1.title("Balance Report")
                root1.iconbitmap("icon.ico")
                bg = PhotoImage(file="goldBG.png")
                my_label = Label(root1, image=bg)
                my_label.place(x=0, y=0, relwidth=1, relheight=1)

                # root.state('zoomed')
                myLabel1 = Label(root1, text=f'      {curr_month.upper()}', font=("times new roman bold", 30),
                                 bg="black", fg="white", bd=1, relief="sunken")
                myLabel2 = Label(root1, text=f'Balance for {curr_month} : {lab}', font=("times new roman bold", 20),
                                 bg="gold")
                myLabel3 = Label(root1, text=f'Income for {curr_month} : {inc}', font=("times new roman bold", 20),
                                 bg="gold")
                myLabel4 = Label(root1, text=f'Expense for {curr_month} : {exp}', font=("times new roman bold", 20),
                                 bg="gold")
                myLabel5 = Label(root1, text=f'Total Balance as on {curr_month} : {bal}',
                                 font=("times new roman bold", 20), bg="gold")

                myLabel1.pack(pady=20)
                myLabel2.pack(pady=20)
                myLabel3.pack(pady=20)
                myLabel4.pack(pady=20)
                myLabel5.pack(pady=20)

                root1.mainloop()

            def comboclick(event):
                global months
                months = myCombo.get()

            Label(root, text="Get Your Balance Report Here", background="gold",
                      font=("times new roman bold", 15)).grid(row=0, column=2)
            #Label(root1, text=f'Balance for {curr_month} : {lab}', font=("times new roman bold", 20),
                           #      bg="gold")

            Label(root, text="Select The Month", background="gold", font=("times new roman bold", 15)).grid(
                column=0, row=5, padx=10, pady=25)

            options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                       "November", "December"]

            clicked = StringVar()

            myCombo = ttk.Combobox(root, value=options)
            myCombo.set("READONLY")
            myCombo.grid(column=2, row=5)
            myCombo.current(0)
            myCombo.bind("<<ComboboxSelected>>", comboclick)

            myButton = Button(root, text="Get Balance", bg="black", fg="white", font=("times new roman bold", 10),
                              command=change)
            myButton.grid(row=7, column=2)
            root.mainloop()

        def chart():
            root = Toplevel(op)
            root.title('Graph')
            root.iconbitmap("icon.ico")
            root.geometry("540x300")

            bg = PhotoImage(file="goldBG.png")
            my_label = Label(root, image=bg)
            my_label.place(x=0, y=0, relwidth=1, relheight=1)

            def comboclick(event):
                global months
                months = myCombo.get()

            ttk.Label(root, text="Get Your Expense Graph Here", background="gold",
                      font=("times new roman bold", 15)).grid(row=0, column=2)
            ttk.Label(root, text="Select The Month", background="gold", font=("times new roman bold", 15)).grid(
                column=0, row=5, padx=10, pady=25)

            def change():
                root.destroy()
                selected1()

            def selected1():
                curr_month = months
                data = pd.read_csv(f'{curr_month}.csv')

                data['Date'] = pd.to_datetime(data['Date'])
                data.sort_values('Date', inplace=True)
                price_date = data['Date']
                expense = data['Expenses']

                plt.bar(price_date, expense, color=['pink', 'blue'])
                plt.gcf().autofmt_xdate()
                date_format = mpl_dates.DateFormatter('%b,%d %Y')

                plt.title("2021 Expense graph")
                plt.xlabel('Date')
                plt.ylabel('Expenses')

                plt.show()

            options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                       "November", "December"]

            clicked = StringVar()

            myCombo = ttk.Combobox(root, value=options)
            myCombo.set("READONLY")
            myCombo.grid(column=2, row=5)
            myCombo.current(0)
            myCombo.bind("<<ComboboxSelected>>", comboclick)

            myButton = Button(root, text="Get Graph", bg="black", fg="white", font=("times new roman bold", 10),
                              command=change)
            myButton.grid(row=7, column=2)
            root.mainloop()

        def close():
            op.destroy()

        # op.iconbitmap("Price Bunny/icon.ico")
        Button(op, text="Your Monthly Expenses", width="25", height="3", font=("times new roman bold", 12), bg="black",
               fg="white", command=total_balance_get).pack(pady=5)
        Button(op, text="Your Expense Graph", width="25", height="3", font=("times new roman bold", 12), bg="black",
               fg="white", command=chart).pack(pady=5)
        Button(op, text="Close", width="20", height="2", font=("times new roman bold", 12), bg="black", fg="white",
               relief=RAISED, command=close).pack(pady=20)

        op.mainloop()

    def sign_out():
        so = Toplevel(dash)
        so.title("PriceBunny - Sign Out")
        so.iconbitmap("icon.ico")
        so.geometry("500x500")

        bg = PhotoImage(file="goldBG.png")
        my_label = Label(so, image=bg)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)

        def yes():
            root.destroy()

        def no():
            so.destroy()

        Label(so, text="Do you really want to sign out?", width="50", height="4", font=("times new roman bold", 16),
              bg="black", fg="white").pack()
        Button(so, text="Yes,sign out", width="25", height="3", font=("times new roman bold", 14), bg="black",
               fg="white", command=yes).pack(pady=45)
        Button(so, text="No,stay", width="25", height="3", font=("times new roman bold", 14), bg="black", fg="white",
               command=no).pack(pady=5)

        so.mainloop()

    def webcam():
        def no():
            cam.destroy()

        def camera():
            def capturing():
                videoCaptureObject = cv2.VideoCapture(0)
                result = True
                while (result):
                    ret, frame = videoCaptureObject.read()
                    cv2.imwrite("NewPicture.jpg", frame)
                    result = False
                videoCaptureObject.release()

                intro.destroy()
                popup()

            def popup():
                def destroy():
                    cv2.destroyAllWindows()
                    popup.destroy()
                    cam.destroy()

                popup = Toplevel(cam)
                popup.title("PriceBunny - Captured!")
                popup.iconbitmap("icon.ico")
                popup.geometry("500x500")
                bg = PhotoImage(file="goldBG.png")
                my_label = Label(popup, image=bg)
                my_label.place(x=0, y=0, relwidth=1, relheight=1)

                Label(popup, text="Captured! \nThe image is saved as 'NewPicture'. \nView the receipt in your gallery!",
                      width="50", height="4", font=("times new roman bold", 16), bg="white").pack()
                Button(popup, text="Okay", width="25", height="3", font=("times new roman bold", 14), bg="black",
                       fg="white", command=destroy).pack(pady=45)
                popup.mainloop()

            global intro
            intro = Toplevel(cam)
            intro.title("PriceBunny - Camera")
            intro.iconbitmap("icon.ico")
            intro.geometry("500x500")

            bg = PhotoImage(file="goldBG.png")
            my_label = Label(intro, image=bg)
            my_label.place(x=0, y=0, relwidth=1, relheight=1)

            Label(intro, text="Now place your receipt in front of the camera.\n Ready?", width="50", height="4",
                  font=("times new roman bold", 16), bg="white").pack()
            Button(intro, text="Yes", width="25", height="3", font=("times new roman bold", 14), bg="black", fg="white",
                   command=capturing).pack(pady=45)

            intro.mainloop()

        # cam code
        cam = Toplevel(dash)
        cam.title("PriceBunny - Camera permission")
        cam.iconbitmap("icon.ico")
        cam.geometry("500x500")

        bg = PhotoImage(file="goldBG.png")
        my_label = Label(cam, image=bg)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)

        Label(cam, text="Activate Camera?", width="50", height="4", font=("times new roman bold", 16),
              bg="white").pack()

        Button(cam, text="Yes", width="25", height="3", font=("times new roman bold", 14), bg="black", fg="white",
               command=camera).pack(pady=45)
        Button(cam, text="No", width="25", height="3", font=("times new roman bold", 14), bg="black", fg="white",
               command=no).pack(pady=45)

        cam.mainloop()

    def team():
        team = Toplevel(dash)
        team.title("PriceBunny - The Makers")
        team.iconbitmap("icon.ico")
        team.geometry("600x600")

        bg = PhotoImage(file="Bunny Ears Cake Topper, Easter Cake Topper(R).png")
        my_label = Label(team, image=bg)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)
        label = Label(team,
                      text="def Ramya_and_Hemavathi():\n\n while True: \n We hope this app provides you a comfortable environment \nto not only track expenses at ease,\nbut also find joy in saving!\n CHEERS!!\n\nwhile VERY True:\n Happy PriceBunny-ing!",
                      font=("Times New Roman", 14), bg="white")

        label.place(relx=0.5, rely=0.5, anchor='center')

        team.mainloop()

    dash = Toplevel(root)
    dash.title("PriceBunny - Dashboard")
    dash.configure(bg="pink")
    dash.iconbitmap("icon.ico")

    Button(dash, text="~For as long as money has existed, people have had thoughts and opinions about it~", width="75",
           height="2", font=("times new roman bold", 16), bg="gold", fg="black").pack()

    # Paned Window
    panedwindow = ttk.Panedwindow(dash, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)
    # Frame 1
    frame1 = ttk.Frame(panedwindow, width=200, height=500, relief=SUNKEN)

    frame2 = ttk.Frame(panedwindow, width=700, relief=SUNKEN)

    bg = PhotoImage(file="Web_Photo_Editor(2).png")
    my_label = Label(frame2, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)


    # LEFT BUTTONS
    Button(frame1, text="Profile", width="25", height="3", font=("times new roman bold", 10), bg="black", fg="white",
           command=profile).pack()
    Button(frame1, text="Your Expenses", width="25", height="3", font=("times new roman bold", 10), bg="black",
           fg="white", command=options1).pack()
    Button(frame1, text="Your Expense Report", width="25", height="3", font=("times new roman bold", 10), bg="black",
           fg="white", command=options2).pack()

    Button(frame1, text="Capture Receipts", width="25", height="3", font=("times new roman bold", 10), bg="black",
           fg="white", command=webcam).pack()

    Button(frame1, text="Sign Out", width="25", height="3", font=("times new roman bold", 10), bg="black", fg="white",
           command=sign_out).pack()

    Button(frame1, text="The Price Bunnies", width="25", height="3", font=("times new roman bold", 10), bg="black",
           fg="white", command=team).pack()

    # Frame 2

    panedwindow.add(frame1, weight=1)
    panedwindow.add(frame2, weight=4)

    dash.mainloop()


main_screen()





