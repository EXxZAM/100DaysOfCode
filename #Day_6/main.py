import random
from tkinter import *
import pyttsx3
import winsound 
import persian
# Defining the root window
root = Tk()
root.title('Alexa')
root.geometry('300x400')

# Defining functions 
def send_msg():
    message = question_entry.get()
    message = persian.arToPersianChar(message)
    check_awnsers(message)

def check_awnsers(msg):
    
    greet = ['سلام',]
    conv = ['چطوری', 'خوبی']
    convo_awnsers_pos = ['خوبم','حالم خوبه','بد نیستم' ]
    convo_awnsers_neg = ["حالم خوش نیست", "حالم خوب نیست", "حالم بده", "ناراحتم",]
    awnser = ''
    audio_file = ''
    for item in greet:
        if item in msg:
            awnser = 'سلام! من آرمان هستم'
            audio_file = r'F:\#100DaysOfCode\#Day_6\1.wav'
    
    for item in conv:
        if item in msg:
            awnser = "من عالیم! شما چطورید"
            audio_file = r'F:\#100DaysOfCode\#Day_6\2.wav'
    
    for item in convo_awnsers_pos:
        if item in msg:
            awnser = 'از خوشحالیتون خوشحالم'
            audio_file = r'F:\#100DaysOfCode\#Day_6\3.wav'
    
    for item in convo_awnsers_neg:
        if item in msg:
            awnser = "ای بابا! خدا کنه به زودی حالت بهتر شه"
            audio_file = r'F:\#100DaysOfCode\#Day_6\4.wav'
    
    if awnser == '':
        awnser = "متاسفم! ولی متوجه نشدم چی گفتی"
        audio_file = r'F:\#100DaysOfCode\#Day_6\5.wav'
        
    if 'اسمت چیه' in msg:
        awnser = 'من آرمان هستم'
        audio_file = r'F:\#100DaysOfCode\#Day_6\6.wav'
    if 'چیکار بلدی انجام بدی' in msg:
        awnser = 'من میتونم براتون نوشته ذخیره کنم! یا براتون توی اینترنت سرچ کنم! خوبه نه؟'
        audio_file = r'F:\#100DaysOfCode\#Day_6\7.wav'
    awnser_to_user(awnser,audio_file)

def awnser_to_user(return_msg,audio):

    out_label.config(text=return_msg)
    question_entry.delete(0,END)
    winsound.PlaySound(audio,winsound.SND_ASYNC)
    
# Defining the layout
# Defining the two frames (input,output)
output_frame = LabelFrame(root,height=250,width=50, bg='#121211')
input_frame = LabelFrame(root,height=20,width=50, bg='#121211')

output_frame.pack(fill=BOTH, expand=True)
input_frame.pack(fill=BOTH, expand=True)

# Defining the input frame
question_entry = Entry(input_frame, bg='#ffffff', width=45, borderwidth=3)
send_button = Button(input_frame, text='Send Message', borderwidth=4, bg='#121212', fg='white', command=send_msg)
quit_button = Button(input_frame, text='Quit', borderwidth=4, bg='#121212', fg='white', command=root.destroy)

question_entry.grid(row=0,column=0,padx=10,pady=10)
send_button.grid(row=1,column=0,padx=10,pady=10,sticky='we')
quit_button.grid(row=3,column=0,padx=10,pady=10,sticky='we')

# Defining the output frame 
out_label = Label(output_frame, text='چطور میتونم کمکتون کنم', bg='#121212', fg='white',wraplength=200,)

out_label.place(relx=0.5, rely=0.5, anchor='c')
# Calling the main window's main loop 
root.mainloop()