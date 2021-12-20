from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

root = Tk()
root.title("Insta Viewer")
root.geometry("1440x900")


#
#Creating the overall design / colors of the base program
#

frame1 = tk.Frame(master=root, width=20, height=100, bg="#e5e5e5")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=root, width=200, bg="#eaeaea")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=root, width=20, bg="#e5e5e5")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


captionTitle = Label(root, text="Select desired caption", font =("Arial", 25), fg="Black")
captionTitle.place(x=20, y=130)


#
#Caption selecter
#

def caption1ex():
    caption1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, state=DISABLED, fg="Black")
    caption1.place(x=20, y=180)

    caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, fg="Black")
    caption2.place(x=150, y=180)

    caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, fg="Black")
    caption3.place(x=280, y=180)

    caption_box1 = tk.Text(width= 55, height=45)
    caption_box1.place(x=10, y=230)
    caption_box1.insert("1.0", "Insert caption here (Deals, flavors in photo, ect)\n\n Orignal 25k\n Oreo 30k\n Toblorone 30k\n Salted Caramel 30k\n Strawberry 30k\n Mango 20k\n\n\n WhatsApp: 081703764815")


def caption2ex():
    caption1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, fg="Black")
    caption1.place(x=20, y=180)

    caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, state=DISABLED, fg="Black")
    caption2.place(x=150, y=180)

    caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, fg="Black")
    caption3.place(x=280, y=180)

    caption_box2 = tk.Text(width= 55, height=45)
    caption_box2.place(x=10, y=230)
    caption_box2.insert("1.0", "Hi Ima, if your using this hello from Tetahi <3")


def caption3ex():
    caption1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, fg="Black")
    caption1.place(x=20, y=180)

    caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, fg="Black")
    caption2.place(x=150, y=180)

    caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, state=DISABLED, fg="Black")
    caption3.place(x=280, y=180)

    caption_box3 = tk.Text(width= 55, height=45)
    caption_box3.place(x=10, y=230)
    caption_box3.insert("1.0", "Insert main caption for post (Location, Deals ect)\n\n\n\n\n\n\n\n\n\nFor further inquireies message us directly through Instagram, Facebook, Email (gil@brh23.com) or through our website brh23.com")

#Starting with selectable caption groups
caption1 = Button(root, text="Eat me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, fg="Black")
caption1.place(x=20, y=180)

caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, fg="Black")
caption2.place(x=150, y=180)

caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, fg="Black")
caption3.place(x=280, y=180)

#need to work on getting the text to be consistantly saved when selecting caption groups
caption_box = tk.Text(width= 55, height=45)
caption_box.place(x=10, y=230)

#
#Date selecter
#

#Day
clicked = StringVar()
clicked.set("01")

drop = OptionMenu(root, clicked, "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
drop.place(x=1060, y=180)

#Month
clicked2 = StringVar()
clicked2.set("January")

#????How do I lock the size of the dropbox????
drop2 = OptionMenu(root, clicked2, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
drop2.place(x=1120, y=180)

#Year
clicked3 = StringVar()
clicked3.set("2021")

drop3 = OptionMenu(root, clicked3, "2021", "2022", "2023", "2024", "2025", "2026")
drop3.place(x=1215, y=180)

#
#Time of post imput
#
myLable1 = Label(root, text="Time of post (24 hour time):", font =("Arial", 15), fg="Black")
myLable1.place(x=1060, y=240)

postTimeH = Entry(root, width=3)
postTimeH.place(x=1060, y=270)
postTimeH.insert(0, "00")

postTimeM = Entry(root, width=3)
postTimeM.place(x=1100, y=270)
postTimeM.insert(0, "00")


#
#hashtag group switcher
#

#functions changing which button is selected and unselecting the other
#Need to add more functionality - learn lists
def hashtag1ex():
    hashtag1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=hashtag1ex, state=DISABLED, fg="Black")
    hashtag1.place(x=1050, y=450)

    hashtag2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=hashtag2ex, fg="Black")
    hashtag2.place(x=1180, y=450)

    hashtag3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=hashtag3ex, fg="Black")
    hashtag3.place(x=1310, y=450)

def hashtag2ex():
    hashtag1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=hashtag1ex, fg="Black")
    hashtag1.place(x=1050, y=450)

    hashtag2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=hashtag2ex, state=DISABLED, fg="Black")
    hashtag2.place(x=1180, y=450)

    hashtag3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=hashtag3ex, fg="Black")
    hashtag3.place(x=1310, y=450)

def hashtag3ex():
    hashtag1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=hashtag1ex, fg="Black")
    hashtag1.place(x=1050, y=450)

    hashtag2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=hashtag2ex, fg="Black")
    hashtag2.place(x=1180, y=450)

    hashtag3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=hashtag3ex, state=DISABLED, fg="Black")
    hashtag3.place(x=1310, y=450)

#Starting with selectable caption groups
hashtag1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=hashtag1ex, fg="Black")
hashtag1.place(x=1050, y=450)

hashtag2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=hashtag2ex, fg="Black")
hashtag2.place(x=1180, y=450)

hashtag3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=hashtag3ex, fg="Black")
hashtag3.place(x=1310, y=450)



#Title "Select hashtag group"
myLable1 = Label(root, text="Select hashtag group", font =("Arial", 15), fg="Black")
myLable1.place(x=1160, y=400)


def myClick():
    myLabel = Label(root, text="hello", fg = "Black")
    myLabel .place(x=0, y=0)

#Confirm post button
myButton = Button(root, text="Confirm", font =("Arial Bold", 25), width=28, height=2, command=myClick, fg="green", bg='blue')
myButton.place(x=1020, y=780)



root.mainloop()

#Questions:
#Why can I not see a background color for my buttons?
#Is there a way where all of the buttons and inputs are relative to each other?
#How can I do drag and drop files to the middle?
