# importing the needed packages
import pyqrcode
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox
import os
import time
# big_code = pyqrcode.create('https://exxzamtutorials.ir', error='L', version=5, mode='binary')
# big_code.png(r'F:\#100DaysOfCode\#Day_7\images\code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
# big_code.show()

# Defining Functions
def make_qr_code():
    global big_code
    global thumb, img, thumb
    
    if url_entry.get() == "":
        messagebox.showinfo('error','Enter something in the entry box')
        return
    else:
        big_code = pyqrcode.create(url_entry.get(), error='L', version=5, mode='binary')
        # big_code.show()  
        save_btn.config(state=NORMAL)
        big_code.png('prev.png', scale=5, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
        img = Image.open(r'F:\#100DaysOfCode\prev.png')
        
        top = Toplevel()
        top.geometry('300x300')
        top.config(bg='#121212')
        thumb = ImageTk.PhotoImage(img)
        
        image_label = Label(top, )
        image_label.place(relx=0.5, rely=0.5, anchor='c')
        image_label.config(image=thumb)
    

def save_qr_code():
    save_name = filedialog.asksaveasfilename(initialdir=r'C:\Users\Public\Pictures', filetypes=(('png', '.png'), ("All Files", "*.*")))
    big_code.png(save_name, scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    
# Making the main window 
root = Tk()
root.title("QR Maker")
root.geometry("500x100")
root.resizable(0,0)
root.config(bg='#121212')

# Definig the layout
url_entry = Entry(root, width=30, borderwidth=3)
save_btn = Button(root, text='Save QR', padx=15, bg='#121212', fg='white', pady=5, state=DISABLED, command=save_qr_code)  
make_btn = Button(root, text='Create QRcode', padx=15, bg='#121212', fg='white', pady=5, command=make_qr_code)
quit_btn = Button(root, text='Quit App', padx=15, command=root.destroy, bg='#121212', fg='white', pady=5 )

# placing widgets on screen
url_entry.place(relx=0.5, rely=0.2, anchor='c')
save_btn.place(relx=0.25, rely=0.55, anchor='c')
make_btn.place(relx=0.5, rely=0.55, anchor='c')
quit_btn.place(relx=0.75, rely=0.55, anchor='c')

# Calling the root window's main loop


root.mainloop()