import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import os
from tkinter import messagebox

root = Tk()
root.title("Login")

connection = mysql.connector.connect(host='localhost', user='root', password='harshit123',
                                     port='3306', database='rbs')
c = connection.cursor()

bkg = "#636e72"

frame = tk.Frame(root, bg=bkg)

label_uname = tk.Label(frame, text="Username: ", font=('verdana', 12), bg=bkg)
entry_uname = tk.Entry(frame, font=('verdana', 12))

label_pwd = tk.Label(frame, text="Password: ", font=('verdana', 12), bg=bkg)
entry_pwd = tk.Entry(frame, font=('verdana', 12), show="*")


def selectData():
    c.execute("select uname,pwd from continentalperk")
    result = c.fetchall()
    check = 0
    for i in result:
        u = i[0]
        p = i[1]
        if entry_uname.get() != u or entry_pwd.get() != p:
            check = 0
        else:
            check = 1
            break

    if check == 1:
        messagebox.showinfo("Success", "Login Successfull")
        uname = entry_uname.get()
        pwd = entry_pwd.get()
        insert_query = "INSERT INTO login(uname,pwd) VALUES(%s,%s)"
        vals = (uname, pwd)
        c.execute(insert_query, vals)
        connection.commit()
        root.destroy()
        os.system("Menu.py")
    else:
        messagebox.showinfo("Sorry", "Invalid Username or Password")



button_insert = tk.Button(frame, text="Login", font=('verdana', 14), bg='orange',
                          command=selectData)

label_uname.grid(row=0, column=0, sticky='e')
entry_uname.grid(row=0, column=1, pady=10, padx=10)

label_pwd.grid(row=1, column=0, sticky='e')
entry_pwd.grid(row=1, column=1, pady=10, padx=10)

button_insert.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

frame.grid(row=0, column=0)

root.mainloop()