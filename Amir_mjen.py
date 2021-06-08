from tkinter.ttk import *
from time import strftime
import os, sys
from tkinter import *
import tkinter.messagebox
import pygame
from pygame import *
import pyglet


gui = Tk()
gui.title('Mjenjačnica')
gui.iconbitmap('C:/Users/enes/PycharmProjects/Amir_mjen/exc2.ico')
gui.geometry('280x455')
gui.configure(borderwidth="5")
gui.configure(relief="sunken")
gui.configure(background="#2c2c2c")
gui.configure(cursor="arrow")
gui.configure(highlightbackground="#d9d9d9")
gui.configure(highlightcolor="black")

frame1 = Frame(gui).grid(row=0, column=0)
frame2 = Frame(gui).grid(row=1, column=0)
frame3 = Frame(gui).grid(row=2, column=0)
frame4 = Frame(gui).grid(row=3, column=0)
frame5 = Frame(gui).grid(row=4, column=0)
frame6 = Frame(gui).grid(row=5, column=0)
frame7 = Frame(gui).grid(row=8, column=0)
frame8 = Frame(gui).grid(row=9, column=0)
frame9 = Frame(gui).grid(row=10, column=0)

tkinter.messagebox.showinfo('Dobro Došli', 'Samo da znate ovo je moja aplikacija tj, Ammar Bašić Mjenjačnica')

wellbl = Label(frame1, relief='ridge', text='Zamjena novca --> €URO | USD | BAM | HRK')
wellbl.configure(width=36, fg="SpringGreen2", bg='black', font='MathJax_caligraphic 9')
wellbl.grid(row=0, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky='w')

optionList = ["Izaberite valutu", "EUR", "USD", "BAM", "HRK"]
optvar = StringVar(gui)
optvar.set(optionList[0])

opt = OptionMenu(frame2, optvar, *optionList)
opt.config(width=10, font='MathJax_caligraphic 9', fg='black', bg='purple1')
opt.grid(row=1, column=0, sticky='w')

val = DoubleVar(gui, 0.0)
i = IntVar()
i.set(2)

r1 = Radiobutton(frame3, width=5, text='-> EUR', value=1, variable=i, indicator=1,
                 background="NavajoWhite2").grid(row=2, column=0, padx=0, sticky='w')
r2 = Radiobutton(frame3, width=5, text='-> USD', value=2, variable=i, indicator=2,
                 background="AntiqueWhite4").grid(row=2, column=0, padx=64, sticky='w')
r3 = Radiobutton(frame3, width=5, text='-> BAM', value=3, variable=i, indicator=3,
                 background="NavajoWhite2").grid(row=2, column=0, padx=128, sticky='w')
r4 = Radiobutton(frame3, width=5, text='-> HRK', value=4, variable=i, indicator=4,
                 background="LemonChiffon4").grid(row=2, column=0, padx=192, sticky='w')

e1 = Entry(frame4, textvariable=val, bg='dodger blue', relief='sunken', width=10, font='ubuntu 13 bold')
e1.configure(cursor='arrow', justify='right', highlightcolor='black')
e1.grid(row=3, column=0, pady=15, ipady=1, ipadx=1, sticky='w', padx=0)


def callback(*args):
    optlbl = Label(frame2, bg='blue', fg='PaleGreen1',
    font='Ubuntu 10 italic', width=16, relief='groove', text="mijenjate  iz  {}  --->".format(optvar.get()))
    optlbl.grid(row=1, column=0, sticky='w', padx=120)


def izracun():
    if i.get() == 2 and optvar.get() == "EUR":
        usd1 = float(val.get())
        usd2 = usd1 * 1.18
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % usd2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame6, bg='Green3', font=8, text='$$$', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 3 and optvar.get() == "EUR":
        bam1 = float(val.get())
        bam2 = bam1 * 1.95
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % bam2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame5, bg='SpringGreen', font=8, text='KM ', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 4 and optvar.get() == "EUR":
        kuna1 = float(val.get())
        kuna2 = kuna1 * 7.57
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % kuna2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame5, bg='SpringGreen', font=8, text='kuna ', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 1 and optvar.get() == "USD":
        eur1 = float(val.get())
        eur2 = eur1 * 0.85
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % eur2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame5, bg='SpringGreen', font=8, text='€€€ ', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 3 and optvar.get() == "USD":
        bam1 = float(val.get())
        bam2 = bam1 * 1.66
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % bam2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame5, bg='SpringGreen', font=8, text='KM ', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 4 and optvar.get() == "USD":
        kuna1 = float(val.get())
        kuna2 = kuna1 * 6.43
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % kuna2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame5, bg='SpringGreen', font=8, text='kuna', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 1 and optvar.get() == "BAM":
        eur1 = float(val.get())
        eur2 = eur1 * 0.51
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % eur2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame5, bg='SpringGreen', font=8, text='€€€', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 2 and optvar.get() == "BAM":
        usd1 = float(val.get())
        usd2 = usd1 * 0.60
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % usd2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame5, bg='SpringGreen', font=8, text='$$$', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 4 and optvar.get() == "BAM":
        kuna1 = float(val.get())
        kuna2 = kuna1 * 3.87
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % kuna2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame5, bg='SpringGreen', font=8, text='kuna', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 1 and optvar.get() == "HRK":
        eur1 = float(val.get())
        eur2 = eur1 * 0.13
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % eur2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame5, bg='SpringGreen', font=8, text='€€€', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 2 and optvar.get() == "HRK":
        usd1 = float(val.get())
        usd2 = usd1 * 0.16
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % usd2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame6, bg='SpringGreen', font=8, text='$$$', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

    if i.get() == 3 and optvar.get() == "HRK":
        bam1 = float(val.get())
        bam2 = bam1 * 0.26
        rezlbl = Label(text='Vaša konverzija iznosi %.2f' % bam2)
        rezlbl.configure(bg='DeepSkyBlue2', font='ubuntu 10 bold')
        rezlbl.grid(row=5, column=0, padx=7, pady=15, ipady=2, ipadx=0, sticky='w')
        rezlbl = Label(frame6, bg='SpringGreen', font=8, text='KM ', textvariable=i.get())
        rezlbl.grid(row=5, column=0, padx=215)

def play():
    pygame.mixer.init()
    mixer.music.load("indila.mp3")
    mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def ispravka():
    e1.delete(0, END)
    e1.insert(0, "")

#def restart():
#   python = sys.executable
#   os.execl(python, python, *sys.argv)

def zavrsi():
    tkinter.messagebox.showinfo('Doviđenja', 'Hvala na korištenju Ammarove mjenjačnice')
    gui.quit()

def none():
    text = strftime('%H:%M:%S %p')
    dan = strftime('%A')
    lbl.config(text=text)
    lbl.after(1000, none)
    danlbl.config(text=dan)


mslika = PhotoImage(file='money_bag2.png')
label = Label(frame9, image=mslika)
label.image = mslika
label.grid(row=10, column=0, padx=0, pady=0, ipady=0, ipadx=0, sticky='w')


ispravkabtn = Button(frame4, relief='sunken', width=8, text='Ispravka', font='DejaVu 9', command=ispravka,
                bg="AntiqueWhite2", fg='black').grid(row=3, column=0, padx=107, sticky='w')

izvrsibtn = Button(frame4, relief='sunken', width=8, text='Konvertuj', font='DejaVu 9', borderwidth=3, command=izracun,
                bg="Green3", fg='black').grid(row=3, column=0, padx=187, sticky='w')

playbtn = Button(frame5, relief='sunken', borderwidth=2, width=5,
                 text='play', font='DejaVu 9', command=play,
                 fg='black', bg='bisque4',).grid(row=4, column=0, padx=0, sticky='w')

stopbtn = Button(frame5, relief='sunken', borderwidth=2, width=5,
                 text='stop', font='DejaVu 9', command=stop,
                 fg='black', bg='bisque4',).grid(row=4, column=0, padx=50, sticky='w')

#restartbtn = Button(frame5, relief='sunken', borderwidth=2, width=8, text='Restart',
#                    font='DejaVu 9', command=restart, fg='black', bg='yellow',).grid(row=4, column=0, padx=107, sticky='w')

zavrsibtn = Button(frame5, relief='raised', text='Izađi -->', font='DejaVu 9', borderwidth=3, width=9, command=zavrsi,
                fg='black', bg='brown').grid(row=4, column=0, padx=183, sticky='w')


danlbl = Label(frame7, text='',font=('Digital dream Fat Skew', 20 ,'bold'),background='black', foreground='green')
danlbl.grid(row=9, column=0, padx=50, pady=0, ipadx=0, ipady=5, sticky='w')

lbl = Label(frame6, font=('Digital dream Fat Skew', 20 ,'bold'),background='black', foreground='red')
lbl.grid(row=8, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky='w')
none()

optvar.trace("w", callback)
gui.mainloop()
