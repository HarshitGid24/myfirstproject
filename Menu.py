import tkinter
import tkinter as tk
from tkinter import *
import mysql.connector
from PIL import Image,ImageTk
import os
root=tk.Tk()
root.title("Menu")

root.geometry("400x350")

connection=mysql.connector.connect(host="localhost",user="root",password="harshit123",port="3306",database="rbs")
c=connection.cursor()

bkg="#9c6f44"


im = Image.open("food.jpg")
image_resize = im.resize((400,100))
photo = ImageTk.PhotoImage(image_resize)
label1 = Label(image=photo)
label1.image=photo
label1.pack()
frame= tk.Frame(root, width=1000, height=2000, background="bisque",borderwidth=2)
l1=tk.Label(root,text="MENU",font=("Algerian",25),fg="black",bg="white").place(x=160,y=10)

l2=tk.Label(root,text="Continetal Food",font=("Algerian",18),fg="white",bg="black").place(x=120,y=60)

d1=tk.Label(frame,text="Pizza",font=("Algerian",18),fg="white",bg=bkg)
p1=Label(frame,text="Rs.489",font=("Algerian",18),fg="black",bg=bkg)
e_i1=tk.Entry(frame,font=("Verdana",12))

d2=tk.Label(frame,text="Burger",font=("Algerian",18),fg="white",bg=bkg)
p2=Label(frame,text="Rs.150",font=("Algerian",18),fg="black",bg=bkg)
e_i2=tk.Entry(frame,font=("Verdana",12))

d3=tk.Label(frame,text="Pasta",font=("Algerian",18),fg="white",bg=bkg)
p3=Label(frame,text="Rs.300",font=("Algerian",18),fg="black",bg=bkg)
e_i3=tk.Entry(frame,font=("Verdana",12))

d4=tk.Label(frame,text="Sushi",font=("Algerian",18),fg="white",bg=bkg)
p4=Label(frame,text="Rs.350",font=("Algerian",18),fg="black",bg=bkg)
e_i4=tk.Entry(frame,font=("Verdana",12))

d5=tk.Label(frame,text="Dimsums",font=("Algerian",18),fg="white",bg=bkg)
p5=Label(frame,text="Rs.400",font=("Algerian",18),fg="black",bg=bkg)
e_i5=tk.Entry(frame,font=("Verdana",12))


d1.grid(row=1,column=0)
p1.grid(row=1,column=1)
e_i1.grid(row=1,column=2,padx=5,pady=5)

d2.grid(row=2,column=0)
p2.grid(row=2,column=1)
e_i2.grid(row=2,column=2,padx=10,pady=10)

d3.grid(row=3,column=0)
p3.grid(row=3,column=1)
e_i3.grid(row=3,column=2,padx=10,pady=10)

d4.grid(row=4,column=0)
p4.grid(row=4,column=1)
e_i4.grid(row=4,column=2,padx=10,pady=10)

d5.grid(row=5,column=0)
p5.grid(row=5,column=1)
e_i5.grid(row=5,column=2,padx=10,pady=10)


def insert_D():
    i1 = e_i1.get()
    i2 = e_i2.get()
    i3 = e_i3.get()
    i4 = e_i4.get()
    i5 = e_i5.get()
    insert_query="INSERT INTO menu(i1,i2,i3,i4,i5) VALUES(%s,%s,%s,%s,%s)"
    vals=(i1,i2,i3,i4,i5)
    c.execute(insert_query,vals)
    connection.commit()
    root.destroy()
    os.system("bill.py")

b=tk.Button(frame,text="Generate Bill",font=("Elephant",16),command=insert_D)

b.grid(row=6,column=1)

frame.pack(side=tk.BOTTOM)


root.mainloop()