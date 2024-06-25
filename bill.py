import json
import tkinter
from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
from tkinter import filedialog as fd



connection=mysql.connector.connect(host="localhost",user="root",password="harshit123",port="3306",database="rbs")
c=connection.cursor()

root = Tk()
root.geometry('500x850')
root.title("BILL")
im=Image.open("restaurant.jpeg")
image_resize = im.resize((500,150))
photo = ImageTk.PhotoImage(image_resize)
label1 = Label(image=photo)
label1.image=photo
label1.pack()

text_box = Text(root)

im=Image.open("yellow.jpg")
image_resize = im.resize((500,700))
photo = ImageTk.PhotoImage(image_resize)
label2= Label(image=photo)
label2.image=photo
label2.pack()



c.execute("Select * from continentalperk")
l=[]
for x in c:
    l.append(x)

c.execute("Select * from login")
l2=[]
for x in c:
    l2.append(x)
l2=l2[-1]

uname=l2[0]
for i in l:
    if(i[4]==uname):
        r=i

bl= Label(root,text="BILL",font=("Elephant",20)).place(x=200,y=90)
l1=Label(root,text="---------------------------------------------------------------------------------------------------",font=("Helvetica",12),fg="red",bg="black").place(x=0,y=150)
b2=Label(root,text="Invoice From:",font=("Helvetica",12)).place(x=20,y=180)
r1=Label(root,text="Continental Perk Inc.",font=("Calibri",14),bg="grey").place(x=15,y=210)
r2=Label(root,text="cp123@gmail.com",font=("Calibri",14),bg="grey").place(x=15,y=240)
r3=Label(root,text="+91 9810909952",font=("Calibri",14),bg="grey").place(x=15,y=270)
b3=Label(root,text="Invoice To:",font=("Helvetica",12)).place(x=350,y=180)
c1=Label(root,text=r[0]+' '+r[1],font=("Helvetica",12),bg="grey").place(x=350,y=210)
c2=Label(root,text=r[3],font=("Helvetica",12),bg="grey").place(x=350,y=240)
c3=Label(root,text=r[2],font=("Helvetica",12),bg="grey").place(x=350,y=270)

l2=Label(root,text="---------------------------------------------------------------------------------------------------",font=("Helvetica",12),fg="pink",bg="black").place(x=0,y=310)

c.execute("SELECT * FROM menu")
a=[]
for x in c:
    a.append(x)
a=a[-1]
h="hello"
d=Label(root,text="DESCRIPTION",font=("Helvetica",15),bg="white",fg="red").place(x=10,y=350)
l3=Label(root,text="---------------------------------------------------------------------------------------------------",font=("Helvetica",12),fg="pink",bg="black").place(x=0,y=390)
q=Label(root,text="QTY",font=("Helvetica",15),bg="white",fg="red").place(x=280,y=350)

q2=Label(root,text="PRICE",font=("Helvetica",15),bg="white",fg="red").place(x=340,y=350)
q3=Label(root,text="TOTAL",font=("Helvetica",15),bg="white",fg="red").place(x=420,y=350)

pizza= Label(root, text = "1.Pizza",font=("Elephant",15),fg="Black").place(x=10,y=425)
y1=Label(root,text=a[0],font=("Elephant",15),bg="white",fg="black").place(x=290,y=425)
p1=Label(root,text="Rs.489",font=("Algerian",18),bg="brown",fg="white").place(x=325,y=425)
t1=Label(root,text=int(a[0])*200,font=("Algerian",18),bg="white",fg="brown").place(x=430,y=425)

bg= Label(root, text = "2.Burger",font=("Elephant",15),fg="Black").place(x=10,y=475)
y2=Label(root,text=a[1],font=("Elephant",15),bg="white",fg="black").place(x=290,y=475)
p2=Label(root,text="Rs.150",font=("Algerian",18),bg="brown",fg="white").place(x=325,y=475)
t2=Label(root,text=int(a[1])*100,font=("Algerian",18),bg="white",fg="brown").place(x=430,y=475)

pasta= Label(root, text = "3.Pasta",font=("Elephant",15),fg="Black").place(x=10,y=525)
y3=Label(root,text=a[2],font=("Elephant",15),bg="white",fg="black").place(x=290,y=525)
p3=Label(root,text="Rs.300",font=("Algerian",18),bg="brown",fg="white").place(x=325,y=525)
t3=Label(root,text=int(a[2])*300,font=("Algerian",18),bg="white",fg="brown").place(x=430,y=525)

sushi=Label(root, text = "4.Sushi",font=("Elephant",15),fg="Black").place(x=10,y=575)
y4=Label(root,text=a[3],font=("Elephant",15),bg="white",fg="black").place(x=290,y=575)
p4=Label(root,text="Rs.350",font=("Algerian",18),bg="brown",fg="white").place(x=325,y=575)
t4=Label(root,text=int(a[3])*250,font=("Algerian",18),bg="white",fg="brown").place(x=430,y=575)

momos= Label(root, text = "5.Dimsums",font=("Elephant",15),fg="Black").place(x=10,y=625)
y5=Label(root,text=a[4],font=("Elephant",15),bg="white",fg="black").place(x=290,y=625)
p5=Label(root,text="Rs.400",font=("Algerian",18),bg="brown",fg="white").place(x=325,y=625)
t5=Label(root,text=int(a[4])*100,font=("Algerian",18),bg="white",fg="brown").place(x=430,y=625)

ll=Label(root,text="TOTAL BILL ~",font=("Elephant",18),bg="black",fg="white").place(x=90,y=660)
tot=int(a[0])*200+int(a[1])*100+int(a[2])*300+int(a[3])*250+int(a[4])*100
t6=Label(root,text=str(tot),font=("Elephant",18),bg="black",fg="white").place(x=300,y=660)
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)


root.mainloop()