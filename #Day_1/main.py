# I wanted to make a simple terminal based calculator for the first day of the 100 days of code challange

# Packages =>
import os
# Functions
def show_list():
    input('Enter any key to continue \n')
    os.system('cls')
    user_choice=''
    print(list_of_operations)
    while True:
        try:
            user_choice = int(input('Enter the number of your operation \n'))
            break
        except:
            os.system('cls')
            print(list_of_operations)
            print('Only Enter A number that exist in the list')
    print(user_choice)
    check_awnser(user_choice)

def check_awnser(choice):
    if choice == 1:
        a = int(input('Enter the first number \n'))
        b = int(input('Enter the second number \n'))
        add(a,b)
    elif choice == 2:
        a = int(input('Enter the first number \n'))
        b = int(input('Enter the second number \n'))
        print(sub(a,b))
    elif choice == 3:
        a = int(input('Enter the first number \n'))
        b = int(input('Enter the second number \n'))
        print(div(a,b))
    elif choice == 4:
        
        a = int(input('Enter the first number \n'))
        b = int(input('Enter the second number \n'))
        print(mult(a,b))
    else:
        print('Only Enter A Number in the list')
        show_list()

def add(a,b):
    
    print('the awnser is '+str(a+b))
    

def sub(a,b):
    if a<b:
        return 'the awnser is '+str(b-a)
    else:
        return 'the awnser is '+str(a-b)

def div(a,b):
    return 'the awnser is '+str(a/b)

def mult(a,b):
    return 'the awnser is '+str(a*b)
# Making the menu to show a list of operations
list_of_operations = """
Choose by entering the number of the opration
1- Addition
2- Subtract
3- Divide
4- Multiply
"""

continue_loop=True
while continue_loop==True:

    show_list()
    
    
