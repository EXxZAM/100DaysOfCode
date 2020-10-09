from tkinter import *
import pygame
import os
from tkinter import StringVar
from tkinter import filedialog
root = Tk()
root.geometry('600x420')
root.resizable(0,0)
root.title('Music Player')
# Initiating Pygame
pygame.init()
# Initiating Pygame Mixer
pygame.mixer.init()

# Declaring track Variable
track = StringVar()
# Declaring Status Variable
status = StringVar()


# Defining Play Song Function
def playsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0',END)
    # Displaying Selected Song title
    
    songtrack.insert('1.0',playlist.get(ACTIVE))
    songtrack.config(state=DISABLED)
    # Displaying Status
    status.set("-Playing")
    # Loading Selected Song
    pygame.mixer.music.load(playlist.get(ACTIVE))
    # Playing Selected Song
    pygame.mixer.music.play()

def stopsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0',END)
    songtrack.config(state=DISABLED)
    # Displaying Status
    status.set("-Stopped")
    # Stopped Song
    pygame.mixer.music.stop()

def pausesong():
    # Displaying Status
    status.set("-Paused")
    # Paused Song
    pygame.mixer.music.pause()

def unpausesong():
    # Displaying Status
    status.set("-Playing")
    # Playing back Song
    pygame.mixer.music.unpause()

# Changing Directory for fetching Songs
def change_dir():
    global address
    
    address = filedialog.askdirectory()
    os.chdir(address)

    # Fetching Songs
    songtracks = os.listdir()
    # Inserting Songs into Playlist
    for track in songtracks:
        playlist.insert(END,track)

trackframe = LabelFrame(root,text="Song Track",font=("Arial",15,"bold"),bg="#a887e0",fg="white",bd=5,relief=GROOVE)
trackframe.place(x=0,y=200,width=600,height=120)


# Inserting Song Track Label
songtrack = Text(trackframe,width=40,height=2,font=("Arial",15,),bg="#8a1553",fg="white",state=DISABLED)
songtrack.grid(row=0,column=0,padx=10,pady=5)
# Inserting Status Label
trackstatus = Label(trackframe,textvariable=status,font=("Sans-serif",12,),bg="#8a1553",fg="white").grid(row=0,column=1,padx=10,pady=5)

# Creating Button Frame
buttonframe = LabelFrame(root,text="Control Panel",font=("Arial",15,"bold"),bg="#a887e0",fg="white",bd=5,relief=GROOVE, pady=10,)
buttonframe.place(x=0,y=320,width=600,height=100)
# Inserting Play Button
playbtn = Button(buttonframe,text="Play",command=playsong,width=6,height=1,font=("Arial",16,),fg="white",bg="#8a1553").grid(row=0,column=0,padx=10,pady=5)
# Inserting Pause Button
playbtn = Button(buttonframe,text="Pause",command=pausesong,width=8,height=1,font=("Arial",16,),fg="white",bg="#8a1553").grid(row=0,column=1,padx=10,pady=5)
# Inserting Unpause Button
playbtn = Button(buttonframe,text="Unpause",command=unpausesong,width=10,height=1,font=("Arial",16,),fg="white",bg="#8a1553").grid(row=0,column=2,padx=10,pady=5)
# Inserting Stop Button
playbtn = Button(buttonframe,text="Stop",command=stopsong,width=6,height=1,font=("Arial",16,),fg="white",bg="#8a1553").grid(row=0,column=3,padx=10,pady=5)
# Inserting Stop Button


# Creating Playlist Frame
songsframe = LabelFrame(root,text="Song Playlist",font=("Arial",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
songsframe.place(x=0,y=0,width=600,height=200)

# Inserting scrollbar
scrol_y = Scrollbar(songsframe,orient=VERTICAL)
# Inserting Playlist listbox
playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("Arial",12,),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
# Applying Scrollbar to listbox
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)


change_dir()
root.mainloop()