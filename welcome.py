from tkinter import *
import os
from PIL import Image,ImageTk
root = Tk()
def register():
    root.destroy()
    os.system("Register.py")
def login():
    root.destroy()
    os.system("Login.py")

root.geometry('400x250')
root.title("Welcome")

im = Image.open("restaurant.jpeg")
image_resize = im.resize((400,250))
photo = ImageTk.PhotoImage(image_resize)
label1 = Label(image=photo)
label1.image=photo
label1.pack()
#new_size = im.resize((new_width, new_height))



namel = Label(root, text = "Welcome to Continental Perk !",font=("Algerian",20),fg="white",bg='red').place(x = 45,y = 10)
registerbutton=Button(root,text="Register",command=register,height=2, width=10,font=("Arial",15),fg='white',bg='black').place(x=35,y=100)
loginbuton=Button(root,text="Login",command=login,height=2, width=10,font=("Arial",15),bg='green',fg='white').place(x=210,y=100)



root.mainloop()