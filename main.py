from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from datetime import datetime
import os
import tkinterdnd2

root = Tk()
root.title("Insta Viewer")
canvas = tk.Canvas(root, height=900, width=1440)
canvas.pack()

#
#Creating the overall design / colors of the base program
#

frame1 = tk.Frame(root, width=20, height=100, bg="#e5e5e5")
frame1.place(relx=0.28, rely=0, relwidth=0.425, relheight=1)


captionTitle = Label(root, text="Select desired caption", font =("Arial", 20), fg="Black")
captionTitle.place(relx=0.03, rely=0.13, relwidth=0.2, relheight=0.1)


#
#Caption selecter
#

def caption1ex():
    caption1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, state=DISABLED, fg="Black")
    caption1.place(relx=0.02, rely=0.22)

    caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, fg="Black")
    caption2.place(relx=0.1, rely=0.22)

    caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, fg="Black")
    caption3.place(relx=0.18, rely=0.22)

    caption_box1 = tk.Text(width= 55, height=45)
    caption_box1.place(relx=0.005, rely=0.28, relwidth= 0.27, relheight=0.7)
    caption_box1.insert("1.0", "Insert caption here (Deals, flavors in photo, ect)\n\n Orignal 25k\n Oreo 30k\n Toblorone 30k\n Salted Caramel 30k\n Strawberry 30k\n Mango 20k\n\n\n WhatsApp: 081703764815")


def caption2ex():
    caption1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, fg="Black")
    caption1.place(relx=0.02, rely=0.22)

    caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, state=DISABLED, fg="Black")
    caption2.place(relx=0.1, rely=0.22)

    caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, fg="Black")
    caption3.place(relx=0.18, rely=0.22)

    caption_box2 = tk.Text(width= 55, height=45)
    caption_box2.place(relx=0.005, rely=0.28, relwidth= 0.27, relheight=0.7)
    caption_box2.insert("1.0", "Hi Ima, if your using this hello from Tetahi <3")


def caption3ex():
    caption1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, fg="Black")
    caption1.place(relx=0.02, rely=0.22)

    caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, fg="Black")
    caption2.place(relx=0.1, rely=0.22)

    caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, state=DISABLED, fg="Black")
    caption3.place(relx=0.18, rely=0.22)

    caption_box3 = tk.Text(width= 55, height=45)
    caption_box3.place(relx=0.005, rely=0.28, relwidth= 0.27, relheight=0.7)
    caption_box3.insert("1.0", "Insert main caption for post (Location, Deals ect)\n\n\n\n\n\n\n\n\n\nFor further inquireies message us directly through Instagram, Facebook, Email (gil@brh23.com) or through our website brh23.com")

#Starting with selectable caption groups
caption1 = Button(root, text="Eat me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, fg="Black")
caption1.place(relx=0.02, rely=0.22)

caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, fg="Black")
caption2.place(relx=0.1, rely=0.22)

caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, fg="Black")
caption3.place(relx=0.18, rely=0.22)

#need to work on getting the text to be consistantly saved when selecting caption groups
caption_box = tk.Text()
caption_box.place(relx=0.005, rely=0.28, relwidth= 0.27, relheight=0.7)

#
#Date selecter
#

# TODO: set to current date

#Day
clicked = StringVar()
clicked.set(datetime.now().strftime("%d"))

drop = tk.OptionMenu(root, clicked, "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
drop.place(relx=0.73, rely=0.22)

#Month
clicked2 = StringVar()
clicked2.set(datetime.now().strftime("%B"))

drop2 = tk.OptionMenu(root, clicked2, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
drop2.config(width=6)
drop2.place(relx=0.771, rely=0.22)

#Year
clicked3 = StringVar()
clicked3.set(datetime.now().strftime("%Y"))

drop3 = tk.OptionMenu(root, clicked3, "2021", "2022", "2023", "2024", "2025", "2026")
drop3.place(relx=0.84, rely=0.22)

#
#Time of post imput
#
myLable1 = Label(root, text="Time of post (24 hour time):", font =("Arial", 15), fg="Black")
myLable1.place(relx=0.73, rely=0.28)

myLable2 = Label(root, text=":", font =("Arial", 15), fg="Black")
myLable2.place(relx=0.7552, rely=0.31)

postTimeH = Entry(root, width=3)
postTimeH.place(relx=0.73, rely=0.31)
_hr = (int(datetime.now().strftime("%H"))+1) % 24
if _hr>9 :
    _hr = str(_hr)
else :
    _hr = "0"+str(_hr)

postTimeH.insert(0, _hr)

postTimeM = Entry(root, width=3)
postTimeM.place(relx=0.76, rely=0.31)
postTimeM.insert(0, "00")


#
#hashtag group switcher
#

#functions changing which button is selected and unselecting the other
#Need to add more functionality - learn lists
def hashtag1ex():
    hashtag1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=hashtag1ex, state=DISABLED, fg="Black")
    hashtag1.place(relx=0.73, rely=0.5)

    hashtag2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=hashtag2ex, fg="Black")
    hashtag2.place(relx=0.82, rely=0.5)

    hashtag3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=hashtag3ex, fg="Black")
    hashtag3.place(relx=0.91, rely=0.5)

def hashtag2ex():
    hashtag1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=hashtag1ex, fg="Black")
    hashtag1.place(relx=0.73, rely=0.5)

    hashtag2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=hashtag2ex, state=DISABLED, fg="Black")
    hashtag2.place(relx=0.82, rely=0.5)

    hashtag3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=hashtag3ex, fg="Black")
    hashtag3.place(relx=0.91, rely=0.5)

def hashtag3ex():
    hashtag1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=hashtag1ex, fg="Black")
    hashtag1.place(relx=0.73, rely=0.5)

    hashtag2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=hashtag2ex, fg="Black")
    hashtag2.place(relx=0.82, rely=0.5)

    hashtag3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=hashtag3ex, state=DISABLED, fg="Black")
    hashtag3.place(relx=0.91, rely=0.5)

#Starting with selectable caption groups
hashtag1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=hashtag1ex, fg="Black")
hashtag1.place(relx=0.73, rely=0.5)

hashtag2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=hashtag2ex, fg="Black")
hashtag2.place(relx=0.82, rely=0.5)

hashtag3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=hashtag3ex, fg="Black")
hashtag3.place(relx=0.91, rely=0.5)



#Title "Select hashtag group"
myLable1 = Label(root, text="Select hashtag group", font =("Arial", 15), fg="Black")
myLable1.place(relx=0.799, rely=0.45)


def myClick():
    myLabel = Label(root, text="hello", fg = "Black")
    myLabel.place(x=0, y=0)

#Confirm post button
myButton = Button(root, text="Confirm", font =("Arial Bold", 25), command=myClick, fg="green", bg='blue')
myButton.place(relx=0.705, rely=0.9, relheight=0.1, relwidth=0.288)

# DONE: make size of window scalable
# TODO: drag and drop
# TODO: Overriding drag and drop
# TODO: Drang and drop oly for pictures
# TODO: Account switcher (object oriented?)
# TODO: Instagram functionality
# TODO: Hashtag editor
# TODO: Encryption for passwords



root.mainloop()

#Questions:
#Why can I not see a background color for my buttons?
#Is there a way where all of the buttons and inputs are relative to each other?
#How can I do drag and drop files to the middle?
