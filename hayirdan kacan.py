from tkinter import *
from tkinter import messagebox
import random

def hayir():
    messagebox.showinfo('', 'Saol kardes')
    quit()

def fare(event):
    btnevet.place(x=random.randint(0, 250), y=random.randint(0, 250))  
root = Tk()
root.geometry('300x300')
root.title('Kasim bileti aliniyor mu?')
root.resizable(width=False, height=False)  
root['bg'] = 'white'

label = Label(root, text='Kasim bileti aliniyor mu?', font='Arial 20 bold', bg='white')
label.pack()

btnevet = Button(root, text='hayir', font='Arial 20 bold')
btnevet.place(x=85, y=50)
btnevet.bind('<Enter>', fare)

btnhayir = Button(root, text='Evet', font='Arial 20 bold', command=hayir)
btnhayir.place(x=175, y=50)

root.mainloop()