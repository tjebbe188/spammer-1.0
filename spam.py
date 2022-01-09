import keyboard
from pyautogui import *
from keyboard import *
from time import sleep
from tkinter import *
import pyautogui
window=Tk()


def clicker():
    global click_var 
    #if click_var = 0: clicker is off
    #if click_var = 1: clicker is on
    if click_var == 0:
        click_var = 1 
        print('opopo')
        sleep(0.2)
    elif click_var == 1:
        print('11111111')
        click_var = 0
        sleep(0.2)
    elif click_var < 0:
        print('error1: clickvar input not 0')
    elif click_var > 1:
        print('error2: clickvar input not 1')
    else:
        print('wait what')

def everyone_spam():
    global everyone_var
    #if click_var = 0: clicker is off
    #if click_var = 1: clicker is on
    if everyone_var == 0:
        everyone_var = 1 
        print('popo')
        sleep(0.2)
    elif everyone_var == 1:
        print('pepe')
        everyone_var = 0
        sleep(0.2)
    elif everyone_var < 0:
        print('error5: everyonevar input not 0')
    elif everyone_var > 1:
        print('error6: everyonevar input not 1')
    else:
        print('wait what what')

def nerd_spam():
    global nerd_var
    #if click_var = 0: clicker is off
    #if click_var = 1: clicker is on
    if nerd_var == 0:
        nerd_var = 1 
        print('popo')
        sleep(0.2)
    elif nerd_var == 1:
        print('pepe')
        nerd_var = 0
        sleep(0.2)
    elif nerd_var < 0:
        print('error9: nerd_var input not 0')
    elif nerd_var > 1:
        print('error10: nerd_var input not 1')
    else:
        print('wait wait what what')

def gg_spam():
    global gg_var
    #if click_var = 0: clicker is off
    #if click_var = 1: clicker is on
    if gg_var == 0:
        gg_var = 1 
        print('popo')
        sleep(0.2)
    elif gg_var == 1:
        print('pepe')
        gg_var = 0
        sleep(0.2)
    elif gg_var < 0:
        print('error13: gg_var input not 0')
    elif gg_var > 1:
        print('error14: gg_var input not 1')
    else:
        print('wait wait what what')

looper = True

def stop():
    global looper
    looper = False

name=Label(window, text="THE spammer 1.0", fg='black', font=("Helvetica", 30))
name.place(x=10, y=10)


clickerbtn=Button(window, text="clicker", bg='grey', width='16' , height='2' ,command=clicker)
clickerbtn.place(x=10, y=100)

clickername=Label(window, text="auto clicker. its not my fault if you get banned somewhere.\npress 9 or the button to turn on/off", fg='black', font=("Helvetica", 10))
clickername.place(x=150, y=105)


everyonebtn=Button(window, text="@everyone spammer", bg='grey', width='16', height='2' ,command=everyone_spam)
everyonebtn.place(x=10, y=150)

clickername=Label(window, text="@everyone spammer. great for annoying people on discord.\npress 8 or the button to turn on/off", fg='black', font=("Helvetica", 10))
clickername.place(x=150, y=155)


nerdbtn=Button(window, text="nerd spammer", bg='grey', width='16', height='2' ,command=nerd_spam)
nerdbtn.place(x=10, y=200)

clickername=Label(window, text="nerd spammer. in case someone is being really annoying.\npress 7 or the button to turn on/off", fg='black', font=("Helvetica", 10))
clickername.place(x=150, y=205)


ggbtn=Button(window, text="gg spammer", bg='grey', width='16', height='2' ,command=gg_spam)
ggbtn.place(x=10, y=250)

clickername=Label(window, text="gg spammer. we all gotta stay positive in these times :D\npress 6 or the button to turn on/off", fg='black', font=("Helvetica", 10))
clickername.place(x=150, y=255)


breakbtn=Button(window, text='stop it', bg='grey', width='16', height='2' ,command=stop)
breakbtn.place(x=10, y=300)

clickername=Label(window, text="button to close the spammer. in case you almost get banned.\npress 5 or the button to turn close the spammer", fg='black', font=("Helvetica", 10))
clickername.place(x=150, y=305)


window.title('THE spammer 1.0')
window.geometry("600x400+10+20")

click_var = 0
everyone_var = 0
nerd_var = 0
gg_var = 0
something = 0

print('starting program')

while looper == True: 
    clickerbtn.pack  
    everyonebtn.pack
    nerdbtn.pack
    ggbtn.pack
    breakbtn.pack
    if keyboard.is_pressed("9"):
        clicker()
    if keyboard.is_pressed("8"):
        everyone_spam()
    if keyboard.is_pressed("7"):
        nerd_spam()
    if keyboard.is_pressed("6"):
        gg_spam()
    if keyboard.is_pressed("5"):
        stop()

    if click_var == 1:  
        pyautogui.tripleClick()
    if click_var == 0:
        something =+ 1
    if click_var < 0:
        print('error3: clickvar output not 0')
    if click_var > 1:
        print('error4: clickvar output not 1')
    

    if everyone_var == 1:
        pyautogui.typewrite('@everyone')
        pyautogui.press('enter')  
    if everyone_var == 0:
        something =+ 1
    if everyone_var < 0:
        print('error7: everyonevar output not 0')
    if everyone_var > 1:
        print('error8: everyonevar output not 1')
    
    if nerd_var == 1:
        pyautogui.typewrite('nerd')
        pyautogui.press('enter')  
    if nerd_var == 0:
        something =+ 1
    if nerd_var < 0:
        print('error11: nerd_var output not 0')
    if nerd_var > 1:
        print('error12: nerd_var output not 1')
    
    if gg_var == 1:
        pyautogui.typewrite('gg')
        pyautogui.press('enter')  
    if gg_var == 0:
        something =+ 1
    if gg_var < 0:
        print('error15: gg_var output not 0')
    if gg_var > 1:
        print('error15: gg_var output not 1')

    window.update()
    window.update_idletasks()