from tkinter import *
import random

parent=Tk()
parent.geometry("950x500")
parent.configure(bg="#B0E2FF")
array1=[]
array2=[]
label=Label(parent,text="",font=("Arial", 24))
label.pack(pady=200)
button_font = ("Arial", 10)

def print_number():
    random_number=random.randint(0,100)
    label.config(text=str(random_number))




def generate_buttons():
    
    for numb in range(3):
        button1=Button(parent,text=array1[numb],width=10,height=5,font=button_font)
        button1.place(x=50+(100*numb),y=100)

        button2=Button(parent,text=array2[numb],width=10,height=5,font=button_font)
        button2.place(x=600+(100*numb),y=100)
    space=0
    for numb in range(3,6):
        button1=Button(parent,text=array1[numb],width=10,height=5,font=button_font)
        button1.place(x=50+(100*space),y=200)

        button2=Button(parent,text=array2[numb],width=10,height=5,font=button_font)
        button2.place(x=600+(100*space),y=200)
        space=space+1
    
    space=0
    for numb in range(6,9):
        button1=Button(parent,text=array1[numb],width=10,height=5,font=button_font)
        button1.place(x=50+(100*space),y=300)

        button2=Button(parent,text=array2[numb],width=10,height=5,font=button_font)
        button2.place(x=600+(100*space),y=300)
        space=space+1

    number_button=Button(parent,text="CLICK TO GENERATE A NUMBER",command=print_number,width=35,height=4)
    number_button.place(x=337,y=260)
    # button1=Button(parent,text=array1[1],width=10,height=5)
    # button1.place(x=150,y=100)
    


def generate_number():
    for x in range(9):
        number= random.randint(0,100)
        array1.append(number)
    for y in range(9):
        number1=random.randint(0,100)
        array2.append(number1)
    generate_buttons()

    return 1

button_start=Button(parent,text="START GAME",command=generate_number,fg="green",)
button_start.pack(side=TOP)
button_end=Button(parent,text="END GAME",fg="red",command=parent.destroy)
button_end.pack(side=BOTTOM)


parent.mainloop()

print(array1)
print(array2)