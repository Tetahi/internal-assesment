from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from datetime import datetime
import os
import tkinterdnd2
from instabot import Bot
import sqlite3, hashlib
from functools import partial


global caption_box


#
#Overall design
#

#Instaviewer main window
root = tkinterdnd2.Tk()
root.title("Insta Viewer")
canvas = tk.Canvas(root, height=900, width=1440)
canvas.pack()

frame1 = tk.Frame(root, width=20, height=100, bg="#e5e5e5")
frame1.place(relx=0.28, rely=0, relwidth=0.425, relheight=1)

#CaptionTitle
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
    caption_box = tk.Text(width= 55, height=45)
    caption_box.place(relx=0.005, rely=0.28, relwidth= 0.27, relheight=0.7)
    caption_box.insert("1.0", "Insert caption here (Deals, flavors in photo, ect)\n\n Orignal 25k\n Oreo 30k\n Toblorone 30k\n Salted Caramel 30k\n Strawberry 30k\n Mango 20k\n\n\n WhatsApp: 081703764815")


def caption2ex():
    caption1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, fg="Black")
    caption1.place(relx=0.02, rely=0.22)
    caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, state=DISABLED, fg="Black")
    caption2.place(relx=0.1, rely=0.22)
    caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, fg="Black")
    caption3.place(relx=0.18, rely=0.22)
    caption_box = tk.Text(width= 55, height=45)
    caption_box.place(relx=0.005, rely=0.28, relwidth= 0.27, relheight=0.7)
    caption_box.insert("1.0", "Hi Ima, if your using this hello from Tetahi <3")

def caption3ex():
    caption1 = Button(root, text="Eat Me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, fg="Black")
    caption1.place(relx=0.02, rely=0.22)
    caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, fg="Black")
    caption2.place(relx=0.1, rely=0.22)
    caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, state=DISABLED, fg="Black")
    caption3.place(relx=0.18, rely=0.22)
    caption_box = tk.Text(width= 55, height=45)
    caption_box.place(relx=0.005, rely=0.28, relwidth= 0.27, relheight=0.7)
    caption_box.insert("1.0", "Insert main caption for post (Location, Deals ect)\n\n\n\n\n\n\n\n\n\nFor further inquireies message us directly through Instagram, Facebook, Email (gil@brh23.com) or through our website brh23.com")

#selectable caption groups main page
caption1 = Button(root, text="Eat me", font =("Arial Bold", 12), width=8, height= 2, command=caption1ex, fg="Black")
caption1.place(relx=0.02, rely=0.22)
caption2 = Button(root, text="Custom", font =("Arial Bold", 12), width=8, height= 2, command=caption2ex, fg="Black")
caption2.place(relx=0.1, rely=0.22)
caption3 = Button(root, text="BRH", font =("Arial Bold", 12), width=8, height= 2, command=caption3ex, fg="Black")
caption3.place(relx=0.18, rely=0.22)
caption_box = tk.Text()
caption_box.place(relx=0.005, rely=0.28, relwidth= 0.27, relheight=0.7)

#
#Account database
#
with sqlite3.connect("accountinfo.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accountDetails(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")

def LogInAccount():

    global username
    global password
    global usernameEntry
    global passwordEntry
    username = StringVar()
    password = StringVar()

    def LogInDetails():

        username = usernameEntry.get()
        password = passwordEntry.get()

        insert_fields = """INSERT INTO accountDetails(username, password)
        VALUES(?, ?)"""
        cursor.execute(insert_fields, (username, password))
        db.commit()
        logInPop.destroy()
        LogInAccount()

    def removeEntry(input):
        cursor.execute("DELETE FROM accountDetails WHERE id = ?", (input,))
        db.commit()
        logInPop.destroy()
        LogInAccount()

    def selectEntry(input):
        global postUser
        global postPass
        postUser = (array[input-1][1])
        postPass = (array[input-1][2])
        logInPop.destroy()
        Label7 = Label(root, text=("You are posting to: " + postUser), font=("Arial Bold", 15))
        Label7.place(relx=0.73, rely=0.1)

#Login window
    logInPop = tkinterdnd2.Tk()
    logInPop.title("Log in")
    canvas2 = tk.Canvas(logInPop, height = 400, width = 300)
    canvas2.pack()
    usernameLabel = Label(logInPop, text="Username: ")
    usernameLabel.place(relx=0, rely=0)
    usernameEntry = Entry(logInPop, textvariable=username)
    usernameEntry.place(relx=0.3, rely=0)
    usernameEntry.focus()
    passwordLabel = Label(logInPop, text="Password: ")
    passwordLabel.place(relx=0, rely=0.08)
    passwordEntry = Entry(logInPop, textvariable=password)
    passwordEntry.place(relx=0.3, rely=0.08)
    label6 = Label(logInPop, text="Saved Accounts:", font=("Arial Bold", 20))
    label6.place(relx=0, rely=0.23)
    logInButton = Button(logInPop, text="Save details", bg="Blue", command = LogInDetails)
    logInButton.place(relx=0.63, rely=0.15, relwidth = 0.3, relheight = 0.06)
    logInPop.mainloop

    usernamelbl = Label(logInPop, text="Username", font=("Arial Bold", 15))
    usernamelbl.place(relx= 0.03, rely=0.3)
    passwordlbl = Label(logInPop, text="Password", font=("Arial Bold", 15))
    passwordlbl.place(relx= 0.35, rely=0.3)

    cursor.execute("SELECT * FROM accountDetails")
    if(cursor.fetchall() != None):
        i = 0
        while True:
            cursor.execute("SELECT * FROM accountDetails")
            array = cursor.fetchall()

            if (len(array) == 0):
                break

            rowsize = i*0.07 + 0.39

            label4 = Label(logInPop, text=(array[i][1]), font=("Airal Bold", 12))
            label4.place(relx = 0.03, rely=rowsize)
            label5 = Label(logInPop, text=(array[i][2]), font=("Airal Bold", 12))
            label5.place(relx = 0.35, rely=rowsize)

            delButton = Button(logInPop, text="Delete", command = partial(removeEntry, array[i][0]))
            delButton.place(relx = 0.8, rely=rowsize, relwidth = 0.2)

            selButton = Button(logInPop, text="Select", command = partial(selectEntry, array[i][0]))
            selButton.place(relx = 0.6, rely=rowsize, relwidth = 0.2)

            i = i+1

            cursor.execute("SELECT * FROM accountDetails")
            if (len(cursor.fetchall()) <= i):
                break


logIn = tk.Button(root, text="Account editor / selector", font = ("Arial Bold", 15), command = LogInAccount)
logIn.place(relx=0.705, rely=0, relwidth=0.285, relheight=0.07)

#
#Date selecter
#


#Day
clicked = StringVar(root)
clicked.set(datetime.now().strftime("%d"))

drop = tk.OptionMenu(root, clicked, "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
drop.place(relx=0.73, rely=0.22)

#Month
clicked = StringVar(root)
clicked.set(datetime.now().strftime("%B"))

drop2 = tk.OptionMenu(root, clicked, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
drop2.config(width=6)
drop2.place(relx=0.771, rely=0.22)

#Year
clicked = StringVar(root)
clicked.set(datetime.now().strftime("%Y"))

drop3 = tk.OptionMenu(root, clicked, "2021", "2022", "2023", "2024", "2025", "2026")
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
#Need to add more functionality - learn arrays
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

# TODO: what time will it post, what day will it post, how long will it be until it post,

def getTime():
    global postTimeH
    global postTimeM
    global postMinute
    global postHour
    global drop
    global drop2
    global drop3
    global postDay
    global postMonth
    global postYear

    postMinute = postTimeM.get()
    postHour = postTimeH.get()
    postDay = clicked.get()
    postMonth = clicked.get()
    postYear = clicked.get()

def getFile():
    global postFile
    global lb

    postFile = lb.get(ACTIVE)
    print(postFile)

def confirmPost():
    confirm = tkinterdnd2.Tk()
    confirm.title("Are you sure you want to post this?")

    label10 = Label(confirm, text="Account:")
    label10.grid(row=0, column=0)
    try :
        label11 = Label(confirm, text=(postUser))
        label11.grid(row=0, column=1)
    except :
        error = tkinterdnd2.Tk()
        error.title("Error")
        label001 = Label(error, text=("Please select an account"))
        label001.pack()

    global caption_box
    postCaption = caption_box.get("1.0","end-1c")
    print(postCaption)
    label12 = Label(confirm, text="Caption:")
    label12.grid(row=1, column=0)
    label13 = Label(confirm, text=(postCaption))
    label13.grid(row=1, column=1)

    getTime()
    if int(postHour) > 24:
        error2 = tkinterdnd2.Tk()
        error2.title("Error")
        label002 = Label(error, text=("Invalid time to post"))
        label002.pack()

    getFile()

#Confirm post button
myButton = Button(root, text="Confirm", font =("Arial Bold", 25), command=confirmPost, fg="green", bg='blue')
myButton.place(relx=0.705, rely=0.9, relheight=0.1, relwidth=0.288)

#Drag and drop
myLable3 = Label(root, text = "Drag & Drop files here", font = ("Arial Bold", 24))
myLable3.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.288)

def addto_listbox(event):
    lb.insert("end", event.data)

ws = tk.Frame(root, width=20, height=100, bg="#e5e5e5")
ws.place(relx=0.28, rely=0.3, relwidth=0.425, relheight=1)

frame = Frame(ws)
frame.pack()

lb = Listbox(
    frame,
    width=60,
    height=15,
    selectmode=SINGLE,
    )
lb.pack(fill=X, side=LEFT)
lb.drop_target_register(tkinterdnd2.DND_FILES)
lb.dnd_bind('<<Drop>>', addto_listbox)

myLable3 = Label(root, text = "Drag & Drop file to post below", font = ("Arial Bold", 20))
myLable3.place(relx=0.39, rely=0.24, relheight=0.05, relwidth=0.2)

# TODO: Overriding drag and drop
# TODO: Instagram functionality
# TODO: Hashtag editor
# TODO: Encryption for passwords

# CREDIT: password saver : https://www.youtube.com/watch?v=UrH2WCoYEVo
# CREDIT: password saver : https://www.simplifiedpython.net/python-gui-login/
# CREDIT: TKinter tutorial : https://www.youtube.com/watch?v=YXPyB4XeYLA&t=1205s
# CREDIT: drag and drop : https://pythonguides.com/python-tkinter-drag-and-drop/

root.mainloop()
