from tkinter import *
from tkinter import messagebox
import webbrowser

windo = Tk()
windo.geometry('800x450+500+50')
windo.resizable(False, False)
windo.title('SUPER MARKET')
windo.config(background='#FEFEFE')


def openyoutube():
    webbrowser.open_new('https://www.youtube.com/channel/UCuCATueQMoLDeGtJIupIW6Q')


def openfacebook():
    webbrowser.open_new('https://web.facebook.com/profile.php?id=100070408725323')


def messagebox():
    messagebox.showinfo('SHEF SHOP', 'This is a app For Testing my App Developing')


def program():
    a = entry.get()
    b = entry1.get()
    id = '123456789'
    password = '123456789'

    if a == id and b == password:
        windo.destroy()
        root = Tk()
        root.geometry('400x600+400+20')
        root.resizable(False, False)
        
        # ----------variables---------#
        q1 = IntVar()
        q2 = IntVar()
        q3 = IntVar()
        q4 = IntVar()
        q5 = IntVar()
        q6 = IntVar()
        q7 = IntVar()
        q8 = IntVar()
        q9 = IntVar()
        q10 = IntVar()
        q11 = IntVar()
        q12 = StringVar()

        def total():
            water = q1.get() * 6
            yaghourt = q2.get() * 2
            raibi = q3.get() * 2
            soda = q4.get() * 3
            chips = q5.get() * 5
            bimo = q6.get() * 1
            milk = q7.get() * 3.5
            raib = q8.get() * 3
            choclat = q9.get() * 8
            zit = q10.get() * 16
            roz = q11.get() * 15
            totaloat = float(
                water +
                yaghourt +
                raibi +
                soda +
                chips +
                bimo +
                milk +
                raib +
                choclat +
                zit +
                roz)
            zaka = str(totaloat)
            l99 = Label(root, text=zaka + ' DH', font=('tajawal', 15, 'bold'))
            l99.place(x=180, y=520)

        l1 = Label(root, text='SUPER MARKET', bg='black', fg='#F4B525', font=('tajawal', 15, 'bold')).pack(fill=X)

        f1 = Frame(root,width=230, height=400, bg='#0B2F3A').place(x=90, y=50)

        l2 = Label(f1, text='WATER', bg='#0B2F3A', fg='white').place(x=100, y=90)
        l3 = Label(f1, text='YAGHOURT', bg='#0B2F3A', fg='white').place(x=100, y=120)
        l4 = Label(f1, text='RAIBi', bg='#0B2F3A', fg='white').place(x=100, y=150)
        l5 = Label(f1, text='SODA', bg='#0B2F3A', fg='white').place(x=100, y=180)
        l6 = Label(f1, text='CHIPS', bg='#0B2F3A', fg='white').place(x=100, y=210)
        l7 = Label(f1, text='BIMO', bg='#0B2F3A', fg='white').place(x=100, y=240)
        l8 = Label(f1, text='MILK', bg='#0B2F3A', fg='white').place(x=100, y=270)
        l9 = Label(f1, text='RAIB', bg='#0B2F3A', fg='white').place(x=100, y=300)
        l0 = Label(f1, text='SHOCLAT', bg='#0B2F3A', fg='white').place(x=100, y=330)
        l11 = Label(f1, text='ZIT', bg='#0B2F3A', fg='white').place(x=100, y=360)
        l11 = Label(f1, text='ROZ', bg='#0B2F3A', fg='white').place(x=100, y=390)

        E1 = Entry(f1, width=10, textvariable=q1)
        E1.place(x=200, y=90)
        E2 = Entry(f1, width=10, textvariable=q2)
        E2.place(x=200, y=120)
        E3 = Entry(f1, width=10, textvariable=q3)
        E3.place(x=200, y=150)
        E4 = Entry(f1, width=10, textvariable=q4)
        E4.place(x=200, y=180)
        E5 = Entry(f1, width=10, textvariable=q5)
        E5.place(x=200, y=210)
        E6 = Entry(f1, width=10, textvariable=q6)
        E6.place(x=200, y=240)
        E7 = Entry(f1, width=10, textvariable=q7)
        E7.place(x=200, y=270)
        E8 = Entry(f1, width=10, textvariable=q8)
        E8.place(x=200, y=300)
        E9 = Entry(f1, width=10, textvariable=q9)
        E9.place(x=200, y=330)
        E10 = Entry(f1, width=10, textvariable=q10)
        E10.place(x=200, y=360)
        E11 = Entry(f1, width=10, textvariable=q11)
        E11.place(x=200, y=390)

        b1 = Button(f1, text='GET TOTAL', width=20, height=1, bg='#0B2F3A', fg='gold', font=('tajawal', 11, 'bold'),
                    command=total).place(x=115, y=470)

        water = q1.get() * 6
        yaghourt = q1.get() * 2
        raibi = q1.get() * 2
        soda = q1.get() * 3
        chips = q1.get() * 5
        bimo = q1.get() * 1
        milk = q1.get() * 3.5
        raib = q1.get() * 3
        choclat = q1.get() * 8
        zit = q1.get() * 16
        roz = q1.get() * 15

        windo.mainloop()


    else:
        messagebox.showerror('INCORRESCT MODE PASS', 'INCORRECT MOD PASS')


l1 = Label(windo, text='SUPER MARKET', bg='black', fg='#F4B525', font=('tajawal', 15, 'bold')).pack(fill=X)
f2 = Frame(windo, width=662, height=160, bg='#0B2F3A').place(y=350)

f1 = Frame(windo, width=150, height=500, bg='#0B2F3A').place(x=650, y=30)
l2 = Label(f1, text='This Project it From', bg='#0B2F3A', fg='white', font=('tajawal', 10, 'bold')).place(x=665, y=60)
l3 = Label(f1, text='zakaria salhi', bg='#0B2F3A', fg='white', font=('tajawal', 10, 'bold')).place(x=685, y=80)
photo = PhotoImage(file=('z.PNG'))
l4 = Label(image=photo).place(x=200, y=35)
l5 = Label(f2, text='ID', bg='#0B2F3A', fg='#F4B525', font=('tajawal', 15, 'bold')).place(x=150, y=364)
l6 = Label(f2, text='PASSWORD', bg='#0B2F3A', fg='#F4B525', font=('tajawal', 15, 'bold')).place(x=70, y=405)

b1 = Button(f1, text='My youtube', bg='#F4B525', fg='black', font=('tajawal', 10, 'bold'), width=20, height=1,
            command=openyoutube).place(x=650, y=120)
b2 = Button(f1, text='My facebook', bg='#F4B525', fg='black', font=('tajawal', 10, 'bold'), width=20, height=1,
            command=openfacebook).place(x=650, y=150)
b3 = Button(f1, text='app info', bg='#F4B525', fg='black', font=('tajawal', 10, 'bold'), width=20, height=1,
            command=messagebox).place(x=650, y=180)
b4 = Button(f1, text='Exite', bg='#F4B525', fg='black', font=('tajawal', 10, 'bold'), width=20, height=1,
            command=quit).place(x=650, y=210)

entry = Entry(f2, width=30)
entry.place(x=200, y=370)
entry1 = Entry(f2, width=30)
entry1.place(x=200, y=410)
b5 = Button(f1, text='ENTER', bg='#F4B525', fg='black', font=('tajawal', 10, 'bold'), width=10, height=4,
            command=program).place(x=430, y=360)

windo.mainloop()