import tkinter as tk
from tkinter import *
from datetime import datetime
import time

mainwindow = tk.Tk()
screenX = mainwindow.winfo_screenwidth()
screenY = mainwindow.winfo_screenheight()
startgeometry = str(str(int(screenX / 2))+'x'+str(int(screenY / 2))+'+'+str(int(screenX / 4))+'+'+str(int(screenY / 4)))
mainwindow.title('Clock')
mainwindow.geometry(startgeometry)
mainwindow.minsize(320, 240)
try:
    mainwindow.iconbitmap('clock.ico')
except:
    print('CLOCK.ICO MISSING')
timeformat = '%I:%M:%S %p'
dateformat = '%x'

def setwin():
    screenX = mainwindow.winfo_width()
    screenY = mainwindow.winfo_height()
    settingswindow = Toplevel()
    startgeometry = str(str(int(screenX / 2))+'x'+str(int(screenY / 2))+'+'+str(int(screenX / 4 + mainwindow.winfo_rootx()))+'+'+str(int(screenY / 4 + mainwindow.winfo_rooty())))
    settingswindow.title('Settings')
    settingswindow.geometry(startgeometry)
    settingswindow.minsize(320, 240)
    try:
        settingswindow.iconbitmap('settings.ico')
    except:
        print('SETTINGS.ICO MISSING')

    closeb = Button(settingswindow, text = 'Close', command = settingswindow.destroy)
    labelstrf = Label(settingswindow, text = 'Format (strftime)')
    timefield = Entry(settingswindow, width = 15)
    timefield.insert(0, timeformat)
    datefield = Entry(settingswindow, width = 15)
    datefield.insert(0, dateformat)
    brokenformat = Label(settingswindow, text = 'IMPROPER FORMAT')

    def update():
        real_scale = settingswindow.winfo_width() / 640
        font_size2 = int(18 * real_scale)
        font_size3 = int(12 * real_scale)

        closeb.configure(font = ('Segoe Ui light', font_size3))
        closeb.place(x = 0, y = 0)
        timefield.configure(font = ('Segoe UI light', font_size3))
        timefield.place(x = 5 * real_scale, y = labelstrf.winfo_height() + closeb.winfo_height())
        datefield.configure(font = ('Segoe UI light', font_size3))
        datefield.place(x = 150 * real_scale, y = labelstrf.winfo_height() + closeb.winfo_height())
        global timeformat
        global dateformat
        timeformat = timefield.get()
        dateformat = datefield.get()
        labelstrf.configure(font = ('Segoe UI', font_size2))
        labelstrf.place(x = 0, y = closeb.winfo_height())
        try:
            n = datetime.now()
            n.strftime(timeformat)
            n.strftime(dateformat)
        except ValueError:
            brokenformat.configure(text = 'INVALID FORMAT', font = ('Segoe UI bold', font_size3), fg='red')
            brokenformat.place(x = 0, y = closeb.winfo_height() + 75 * real_scale)
        else:
            brokenformat.configure(text = 'VALID FORMAT', font = ('Segoe UI bold', font_size3), fg='green')
        settingswindow.after(10, update)

    if 'a' == 'a':
        update()
        

time = Label(mainwindow)
datetext = Label(mainwindow)
quitb = Button(mainwindow, text = 'Exit', command = mainwindow.destroy)
quitb.place(x = 0, y = 0)
setb = Button(mainwindow, text = 'Settings', command = setwin)

def update():
    n = datetime.now()
    try:
        t = n.strftime(timeformat)
    except:
        t = n.strftime('%I:%M:%S %p')
    try:
        d = n.strftime(dateformat)
    except:
        d = n.strftime('%x')
    real_scale = mainwindow.winfo_width() / 1280
    font_size1 = int(96 * real_scale)
    font_size2 = int(48 * real_scale)
    font_size3 = int(12 * real_scale)

    time.configure(text = t, font = ('Segoe UI Variable Display Semib', font_size1,))
    time.place(x = mainwindow.winfo_width() / 2 - time.winfo_width() / 2, y = mainwindow.winfo_height() / 2 - time.winfo_height() / 2)
    datetext.configure(text = d, font = ('Segoe UI Variable Display Semib', font_size2))
    datetext.place(x = mainwindow.winfo_width() / 2 - datetext.winfo_width() / 2, y = mainwindow.winfo_height() / 2 + time.winfo_height())
    quitb.configure(font = ('Segoe Ui light', font_size3))
    setb.configure(font = ('Segoe Ui light', font_size3))
    setb.place(x = quitb.winfo_width(), y = 0)
    mainwindow.after(10, update)
    
if 'a' == 'a':
    update()
mainloop()
