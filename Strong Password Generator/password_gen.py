from tkinter import *
import random
import string
global p_save

root = Tk()
root.title("Strong Password Generator")
root.geometry("500x500")
root.configure(background='#ffae7B')

def password_generator():
    symbols = "!\"#$%&\'()*+,-./:;<=>?@\\]^_`{|}~"
    password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + symbols) for _ in range(20))
    entry1.delete(0, END)
    entry1.insert(0, password)

def password_saver():
    password = entry1.get()
    global p_save
    p_save = password

    with open('strong_passwords.txt', 'a+') as f:
        f.write(p_save + "\n")

#Buttons
Button1 = Button(root, text="Click to generate a strong password", command=password_generator, width=30)
Button1.place(x=133, y=100)

Button2 = Button(root, text="Save password to .txt file", command=password_saver, width=30)
Button2.place(x=133, y=333)

#Entries
entry1 = Entry(root, width=30)
entry1.place(x=150, y=200)

root.mainloop()