from datetime import datetime
from itertools import dropwhile, takewhile
from tkinter import *
import instaloader
import os
from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
from tkinter import filedialog
import webbrowser
from tkinter import messagebox
import glob


# Define the window
root = Tk()
root.title('Insta Downloader')
root.geometry('500x500')
root.config(bg='#121212')

file_path = ''


# Define Functions 
def select_dir():
    global file_path
    file_path = filedialog.askdirectory()
    print(file_path)

def open_dir():
    if file_path == '':
        messagebox.showerror('Error', 'Select A directory first')
    else:
        webbrowser.open(file_path)


def download_post():
    if file_path == '':
        messagebox.showerror('Error', 'Select A directory first')
    else:
        i = int(number_of_posts_entry.get())
        os.chdir(file_path)
        L = instaloader.Instaloader()
        posts = instaloader.Profile.from_username(L.context, username_entry.get()).get_posts()
        x=0
        for post in posts:
            if x > i:
                messagebox.showinfo('Info', 'Download Successful')
                break
            elif post.is_video == True:
                pass
            else:
                L.download_post(post,  username_entry.get())
                x=x+1
                


# Define the layout
# Username entry, the path selector, the confirm button, the open dir button
username_label = Label(root, text='User Name: ', bg='#121212', fg='white')
username_entry = Entry(root, width=30, borderwidth=5 )

number_of_posts_label = Label(root, text='posts to download: ', bg='#121212', fg='white')
number_of_posts_entry = Entry(root, width=30, borderwidth=5 )

dir_select_btn = Button(root, text='Select Directory', bg='#121212', borderwidth=3, fg='white', command=select_dir)
download_post_btn = Button(root, text='Download Posts', bg='#121212', borderwidth=3, fg='white', command=download_post)
open_dir_btn = Button(root, text='Open The last Directory', bg='#121212', borderwidth=3, fg='white', command=open_dir)


username_label.grid(row=0, column=0,padx=10, pady=10)
username_entry.grid(row=0, column=1,padx=10, pady=10)

number_of_posts_label.grid(row=1, column=0,padx=10, pady=10)
number_of_posts_entry.grid(row=1, column=1,padx=10, pady=10)


dir_select_btn.grid(row=2, column=1,columnspan=2,padx=10, pady=10, sticky='we')
open_dir_btn.grid(row=3, column=1,columnspan=2,padx=10, pady=10, sticky='we')
download_post_btn.grid(row=4, column=1,columnspan=2,padx=10, pady=10, sticky='we')
# Calling the root main loop
root.mainloop()





