from tkinter import *
import time


root = Tk()

timer = Label(root, font=('Tahoma', 80), width=6, heigh=2)
timer.pack()
counter = 0


def start():
    global counter
    if counter < 100:
        counter += 1
        name = str(counter)
        time.sleep(1)
        timer.config(text=name)
    timer.after(50, start)


def reset():
    global counter
    counter = 0
    name = str(counter)
    timer.config(text=name)


button1 = Button(root, text="start timer", command=start)
button1.place(x=0, y=0)

button2 = Button(root, text="reset timer", command=reset)
button2.place(x=150, y=0)

root.mainloop()
