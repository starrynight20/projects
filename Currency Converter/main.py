from tkinter import *

global f_num

root = Tk()
root.title("Currency converter")
root.geometry("500x500")
root.configure(background='#ffae7B')

currencies = [
    "Euro",
    "Dollar",
    "Yen",
    "Pound sterling"
]

def conversion():
    first_number = entry1.get()
    global f_num
    f_num = float(first_number)

    if clicked1.get() == "Dollar" and clicked2.get() == "Euro":
        display.delete(0, END)
        display.insert(0, f_num * 0.82)

    elif clicked1.get() == "Dollar" and clicked2.get() == "Yen":
        display.delete(0, END)
        display.insert(0, f_num * 103.32)

    elif clicked1.get() == "Dollar" and clicked2.get() == "Pound sterling":
        display.delete(0, END)
        display.insert(0, f_num * 0.74)

    elif clicked1.get() == "Dollar" and clicked2.get() == "Dollar":
        display.delete(0, END)

    elif clicked1.get() == "Euro" and clicked2.get() == "Dollar":
        display.delete(0, END)
        display.insert(0, f_num * 1.22)

    elif clicked1.get() == "Euro" and clicked2.get() == "Yen":
        display.delete(0, END)
        display.insert(0, f_num * 126.43)

    elif clicked1.get() == "Euro" and clicked2.get() == "Pound sterling":
        display.delete(0, END)
        display.insert(0, f_num * 0.91)

    elif clicked1.get() == "Euro" and clicked2.get() == "Euro":
        display.delete(0, END)

    elif clicked1.get() == "Yen" and clicked2.get() == "Euro":
        display.delete(0, END)
        display.insert(0, f_num * 0.0079)

    elif clicked1.get() == "Yen" and clicked2.get() == "Dollar":
        display.delete(0, END)
        display.insert(0, f_num * 0.0097)

    elif clicked1.get() == "Yen" and clicked2.get() == "Pound sterling":
        display.delete(0, END)
        display.insert(0, f_num * 0.0072)

    elif clicked1.get() == "Yen" and clicked2.get() == "Yen":
        display.delete(0, END)

    elif clicked1.get() == "Pound sterling" and clicked2.get() == "Dollar":
        display.delete(0, END)
        display.insert(0, f_num * 1.35)

    elif clicked1.get() == "Pound sterling" and clicked2.get() == "Euro":
        display.delete(0, END)
        display.insert(0, f_num * 1.10)

    elif clicked1.get() == "Pound sterling" and clicked2.get() == "Yen":
        display.delete(0, END)
        display.insert(0, f_num * 139.56)

    elif clicked1.get() == "Pound sterling" and clicked2.get() == "Pound sterling":
        display.delete(0, END)


clicked1 = StringVar()
clicked2 = StringVar()
clicked1.set(currencies[0])
clicked2.set(currencies[0])

# Dropdown menus
drop_down1 = OptionMenu(root, clicked1, *currencies)
drop_down2 = OptionMenu(root, clicked2, *currencies)
drop_down1.place(x=100, y=150)
drop_down2.place(x=300, y=150)

# Buttons
myButton = Button(root, text="Go", command=conversion)
myButton.place(x=220, y=220)

# Entries
entry1 = Entry(root, width=10)
display = Entry(root, width=10)
entry1.place(x=103, y=200)
display.place(x=202, y=250)

root.mainloop()
