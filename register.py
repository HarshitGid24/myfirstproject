import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
root = Tk()
root.title("Registration")

connection = mysql.connector.connect(host='localhost', user='root', password='harshit123',
                                     port='3306', database='rbs')
c = connection.cursor()

bkg = "#636e72"


frame = tk.Frame(root, bg=bkg)

label_firstname = tk.Label(frame, text="First Name: ", font=('verdana',12), bg=bkg)
entry_firstname = tk.Entry(frame, font=('verdana',12))

label_lastname = tk.Label(frame, text="Last Name: ", font=('verdana',12), bg=bkg)
entry_lastname = tk.Entry(frame, font=('verdana',12))

label_mobile= tk.Label(frame, text="Mobile: ", font=('verdana',12), bg=bkg)
entry_mobile = tk.Entry(frame, font=('verdana',12))

label_email = tk.Label(frame, text="Email: ", font=('verdana',12), bg=bkg)
entry_email = tk.Entry(frame, font=('verdana',12))

label_uname = tk.Label(frame, text="Username: ", font=('verdana',12), bg=bkg)
entry_uname = tk.Entry(frame, font=('verdana',12))

label_pwd = tk.Label(frame, text="Password: ", font=('verdana',12), bg=bkg)
entry_pwd = tk.Entry(frame, font=('verdana',12))


def insertData():
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    mobile = entry_mobile.get()
    email = entry_email.get()
    uname = entry_uname.get()
    pwd = entry_pwd.get()
    insert_query = "INSERT INTO continentalperk(firstname,lastname,mobile,email,uname,pwd)VALUES (%s,%s,%s,%s,%s,%s)"
    vals = (firstname,lastname,mobile,email,uname,pwd)
    c.execute(insert_query,vals)
    connection.commit()
    messagebox.showinfo("Success", "Registration Successfully")


button_insert = tk.Button(frame, text="Register", font=('verdana',14), bg='orange',
                          command = insertData)

label_firstname.grid(row=0, column=0)
entry_firstname.grid(row=0, column=1, pady=10, padx=10)

label_lastname.grid(row=1, column=0)
entry_lastname.grid(row=1, column=1, pady=10, padx=10)

label_mobile.grid(row=2, column=0, sticky='e')
entry_mobile.grid(row=2, column=1, pady=10, padx=10)

label_email.grid(row=3, column=0, sticky='e')
entry_email.grid(row=3, column=1, pady=10, padx=10)

label_uname.grid(row=4, column=0, sticky='e')
entry_uname.grid(row=4, column=1, pady=10, padx=10)

label_pwd.grid(row=5, column=0, sticky='e')
entry_pwd.grid(row=5, column=1, pady=10, padx=10)

button_insert.grid(row=7,column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

frame.grid(row=0, column=0)


root.mainloop()