from tkinter import *


# defining the root window
root = Tk()
root.title('IP finder')
root.geometry('400x150')
root.resizable(0,0)
root.config(bg='#121212')


# Functions

def ipInfo(addr=''):
    global result
    from urllib.request import urlopen
    from json import load
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    
    try:
        res = urlopen(url)
        #response from url(if res==None then check connection)
        data = load(res)
        #will load the json response into data
        for attr in data.keys():
            result ='Ip = ' + data['ip'] + ' , \n' +'Country = ' + data['country'] + ' , \n' + 'City = ' + data['city'] + ' , \n'+ 'Location = ' + data['loc'] 
    except:
        result=' IP Address not found'
    
    

def get_ip():

    ipInfo(ip_entry.get())
    text = Text(root, height=5, width=30,bg='#121212',fg='white')
    text.config(state=NORMAL)
    text.insert(INSERT,result)
    text.place(relx=0.65, rely=0.65, anchor='c',)
    text.config(state=DISABLED)



# Defining the layout 

ip_entry = Entry(root,)
ip_entry.insert(0,'Enter the IP Address')

confirm = Button(root, text='Search IP', command=get_ip)

ip_entry.grid(row=0, column=0, padx=10, pady=10)
confirm.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()