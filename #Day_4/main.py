# Password Gen


# Importing packages
from tkinter import *
import random
import time
import os
import pyperclip

# Defining the main window
root = Tk()
root.title('Password Generator')
root.geometry('400x200')
root.config(bg='#121212')
root.resizable(0,0)
password = ''
# Functions
def set_difi():
    global difi
    
    difi = difficulity.get()

def generate():
    """ Generates a random password """
    global password
    output_entry.config(state=NORMAL)
    output_entry.delete(0,END)
    output_entry.config(state=DISABLED)
    # Defining the lists of characters used in password
    symbols = ['@','#','$','%']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    chars = ['a','b','c','d','f','g','h','i','j','k','n','m','p','q','r','s','t','u,','v','w','x','y','z']
    chars2=[]
    for item in chars:
        chars2.append(item.upper())
    similar = ['i','l','I','L','0','o','O']
    random_list = [symbols, numbers, chars, similar,chars2]
    password = ''

    if difi == 'Easy':
        password = password + random.choice(chars)
        password = password + random.choice(numbers)
        password = password + random.choice(symbols)
        password = password + random.choice(similar)

    elif difi == 'Medium':
    
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
       
    elif difi == 'Hard':
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        password = password + random.choice(random.choice(random_list))
        

    output_entry.config(state=NORMAL)
    output_entry.insert(0,password)
    output_entry.config(state=DISABLED)
    
    
    


def copy(passw):
    try:
        pyperclip.copy(passw)
    except:
        pass

# Defining the layout
output_entry = Entry(root, state=DISABLED,width=30)

difficulity = StringVar()
b1 = Radiobutton(root, text='Simple', variable=difficulity, value='Easy',selectcolor='black',fg='white',  bg='#121212', command=set_difi)
b2 = Radiobutton(root, text='Medium', variable=difficulity, value='Medium',selectcolor='black',fg='white',  bg='#121212', command=set_difi)
b3 = Radiobutton(root, text='Hard', variable=difficulity, value='Hard',selectcolor='black', fg='white', bg='#121212', command=set_difi)
difficulity.set('Medium')
difi = difficulity.get()

button = Button(root, text=' Generate ', padx=10, bg='black', fg='white',pady=2, command=generate)
button2 = Button(root, text=' Copy ', padx=10, bg='black', fg='white',pady=2, command=lambda: copy(password))
 
# tkvar = StringVar(root)
# choices = { '4','5','Fries','Fish','Potatoe'}
# tkvar.set('Pizza') # set the default option
# popupMenu = OptionMenu(root, tkvar, *choices)


# Putting the widgets on the screen
output_entry.place(relx=0.5, rely=0.2, anchor=CENTER)
b1.place(relx=0.3, rely=0.35, anchor=CENTER)
b2.place(relx=0.5, rely=0.35, anchor=CENTER)
b3.place(relx=0.7, rely=0.35, anchor=CENTER)
button.place(relx=0.5, rely=0.5, anchor=CENTER)
button2.place(relx=0.5, rely=0.7, anchor=CENTER)




# Calling the main window's mainloop
root.mainloop()