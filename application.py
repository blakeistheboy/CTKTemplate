from customtkinter import *
from random import randint
#functions
def slider(value):
    print(value) #if you want the number to basically be rounded up replace this with print(int(value))

def button():
    r = randint(1, 50)
    print("successfully used button | hashed number: ", r)



def switch():
    D = False
    if Switch.get() == True:
        D = True
        print(D)
    else:
        D = False
        print(D)

def checkbox():
    F = False
    if CheckBox.get() == True:
        F = True
        print(f"[] {F}")
    else:
        F = False
        print(f"[] {F}")

def DropDown(x):
    print('selected: ', x)



app = CTk()
app.geometry("400x400")
app.title("Template | https://discord.gg/GjRt2YtJkV")

Slider = CTkSlider(app, state='normal', from_=0, to=100, command=slider)
Slider.set(0)
Slider.pack(anchor='center', pady=10)

Button = CTkButton(app, text='Click Me!', command=button)
Button.pack(anchor='center', pady=10)

Switch = CTkSwitch(app, text='Enable/Disable Me!', command=switch)
Switch.pack(anchor='center', pady=10)

CheckBox = CTkCheckBox(app, command=checkbox, text='Click Me To Change A Value!')
CheckBox.pack(anchor='center', )

Entry = CTkEntry(app, width=50, height=20, placeholder_text='Entry')
Entry.pack(anchor='center', pady=10)

TextBox = CTkTextbox(app, width=100, height=100)
TextBox.pack(anchor='center', pady=10)

OptionMenu = CTkOptionMenu(app, width=50, height=20, values=['option 1', 'option 2'], command=DropDown)
OptionMenu.pack(anchor='center', pady=10)
app.mainloop()

