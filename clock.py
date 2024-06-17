version = '1.1'
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
scale = 0

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
    global version
    v = Label(settingswindow, text = version)
    closeb = Button(settingswindow, text = 'Close', command = settingswindow.destroy)
    labelstrf = Label(settingswindow, text = 'Format (strftime)')
    timefield = Entry(settingswindow, width = 15)
    timefield.insert(0, timeformat)
    datefield = Entry(settingswindow, width = 15)
    datefield.insert(0, dateformat)
    brokenformat = Label(settingswindow, text = 'IMPROPER FORMAT')

    def scalef(scalev):
        global scale
        scale = scalev

    scale_025 = Button(settingswindow, text =  '0.25x', command = lambda: scalef(0.25))
    scale_05 = Button(settingswindow, text =  '0.5x', command = lambda: scalef(0.5))
    scale_075 = Button(settingswindow, text =  '0.75x', command = lambda: scalef(0.75))
    scale_1 = Button(settingswindow, text =  '1x', command = lambda: scalef(1))
    scale_125 = Button(settingswindow, text = '1.25x', command = lambda: scalef(1.25))
    scale_15 = Button(settingswindow, text =  '1.5x', command = lambda: scalef(1.5))
    scale_175 = Button(settingswindow, text = '1.75x', command = lambda: scalef(1.75))
    scale_2 = Button(settingswindow, text = '2x', command = lambda: scalef(2))
    scale_win = Button(settingswindow, text = 'Window', command = lambda: scalef(0))
    scalel = Label(settingswindow, text = 'Scale Multiple')

    def update():
        global scale
        if scale == 0:
            real_scale = settingswindow.winfo_width() / 640
        else:
            real_scale = scale
        font_size1 = int(8 * real_scale)
        font_size2 = int(18 * real_scale)
        font_size3 = int(12 * real_scale)

        v.configure(font = ('Segoe Variable Display Semib', font_size1))
        v.place(x = settingswindow.winfo_width() - v.winfo_width() - 5 * real_scale, y = settingswindow.winfo_height() - v.winfo_height() - 5 * real_scale)

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
        labelstrf.place(x = 5 * real_scale, y = closeb.winfo_height())

        try:
            n = datetime.now()
            n.strftime(timeformat)
            n.strftime(dateformat)
        except ValueError:
            brokenformat.configure(text = 'INVALID FORMAT', font = ('Segoe UI bold', font_size3), fg='red')
            brokenformat.place(x = 5 * real_scale, y = closeb.winfo_height() + 70 * real_scale)
        else:
            brokenformat.configure(text = 'VALID FORMAT', font = ('Segoe UI bold', font_size3), fg='green')
            brokenformat.place(x = 5 * real_scale, y = closeb.winfo_height() + 70 * real_scale)

        #scalel.configure(font = ('Segoe UI', font_size2))
        #scalel.place(x = settingswindow.winfo_width() - scalel.winfo_width() - 5 * real_scale)
        scale_025.place(x = settingswindow.winfo_width() - scale_025.winfo_width() - 5 * real_scale, y = 10 * real_scale)
        scale_05.place(x = settingswindow.winfo_width() - scale_025.winfo_width() - scale_05.winfo_width() - 10 * real_scale, y = 5 * real_scale)
        scale_075.place(x = settingswindow.winfo_width() - scale_025.winfo_width() - scale_05.winfo_width() - scale_075.winfo_width() - 15 * real_scale, y = 5 * real_scale)
        scale_1.place(x = settingswindow.winfo_width() - scale_025.winfo_width() - scale_05.winfo_width() - scale_075.winfo_width() - scale_1.winfo_width() - 20 * real_scale, y = 5 * real_scale)
        scale_025.place(x = settingswindow.winfo_width() - scale_025.winfo_width() - 5 * real_scale, y = 5 * real_scale)
        scale_125.place(x = settingswindow.winfo_width() - scale_125.winfo_width() - 5 * real_scale, y = scale_025.winfo_height() + 10 * real_scale)
        scale_15.place(x = settingswindow.winfo_width() - scale_125.winfo_width() - scale_15.winfo_width() - 10 * real_scale, y = scale_025.winfo_height() + 10 * real_scale)
        scale_175.place(x = settingswindow.winfo_width() - scale_125.winfo_width() - scale_15.winfo_width() - scale_175.winfo_width() - 15 * real_scale, y = scale_025.winfo_height() + 10 * real_scale)
        scale_2.place(x = settingswindow.winfo_width() - scale_125.winfo_width() - scale_15.winfo_width() - scale_175.winfo_width() - scale_2.winfo_width() - 20 * real_scale, y = scale_025.winfo_height() + 10 * real_scale)
        scale_win.place(x = settingswindow.winfo_width() - scale_win.winfo_width() - 5 * real_scale , y = scale_025.winfo_height() + scale_175.winfo_height() + 15 * real_scale)

        scale_025.configure(font = ('Segoe Ui light', font_size3))
        scale_05.configure(font = ('Segoe Ui light', font_size3))
        scale_075.configure(font = ('Segoe Ui light', font_size3))
        scale_1.configure(font = ('Segoe Ui light', font_size3))
        scale_125.configure(font = ('Segoe Ui light', font_size3))
        scale_15.configure(font = ('Segoe Ui light', font_size3))
        scale_175.configure(font = ('Segoe Ui light', font_size3))
        scale_2.configure(font = ('Segoe Ui light', font_size3))
        scale_win.configure(font = ('Segoe Ui light', font_size3))

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

    global scale
    if scale == 0:
        real_scale = mainwindow.winfo_width() / 1280 
    else:
        real_scale = scale

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
