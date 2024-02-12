from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser

windo =Tk()
windo.geometry('700x500+300+50')
windo.resizable(False,False)
windo.title('Time Organization')
windo.config(background='white')

def zaka():
    messagebox.showinfo('Welcome' , 'This project for Time Organisation' )

def zaka1():
    webbrowser.open_new('https://www.youtube.com/channel/UCuCATueQMoLDeGtJIupIW6Q')

def zaka2():
    webbrowser.open_new('https://web.facebook.com/profile.php?id=100070408725323')

def zaka3():
    b = e1.get()
    c =e2.get()
    id ='123456789'
    password ='123456789'
    if b == id and c == password:
        windo.destroy()
        root = Tk()
        root.geometry('400x600+400+50')
        root.resizable(False,False)
        root.title('Time Organisation')

        l6=Label(root,text='Time Organization',bg='#4CB3A2',fg='white',font="Courier 15 bold",height=1).pack(fill=X)

        f3=Frame(root,width=300 , height=500, bg='#5B277C').place(x=50,y=50)

        l7=Label(f3,text='Organize your time',bg='#5B277C',fg='white',font="Courier 15 bold",height=1).place(x=90,y=80)
        l8=Label(f3, text='Studying',font='Courier',bg='#5B277C',fg='white').place(x=60 ,y=150)
        l9=Label(f3, text='Playing',font='Courier',bg='#5B277C',fg='white').place(x=60 ,y=180)
        l10=Label(f3, text='Bathing',font='Courier',bg='#5B277C',fg='white').place(x=60 ,y=210)
        l11=Label(f3, text='eating',font='Courier',bg='#5B277C',fg='white').place(x=60 ,y=240)
        l12=Label(f3, text='Sleeping',font='Courier',bg='#5B277C',fg='white').place(x=60 ,y=270)
        l13=Label(f3, text='Break',font='Courier',bg='#5B277C',fg='white').place(x=60 ,y=300)
        l14=Label(f3, text='Praying',font='Courier',bg='#5B277C',fg='white').place(x=60 ,y=330)
        l15=Label(f3, text='sport',font='Courier',bg='#5B277C',fg='white').place(x=60 ,y=360)
        l16=Label(f3, text='Working',font='Courier',bg='#5B277C',fg='white').place(x=60 ,y=390)
        l17=Label(f3, text='Else',font='Courier',bg='#5B277C',fg='white').place(x=60 ,y=420)
        def total():
            x1 =q1.get()*1
            x2 =q2.get()*1
            x3 =q3.get()*1
            x4 =q4.get()*1
            x5 =q5.get()*1
            x6 =q6.get()*1
            x7 =q7.get()*1
            x8 =q8.get()*1
            x9 =q9.get()*1
            x10 =q10.get()*1
            totalito =float(
                x1+
                x2+
                x3+
                x4+
                x5+
                x6+
                x7+
                x8+
                x9+
                x10
            )
            nino = str(totalito)
            l99=Label(root , text=nino+' Hour',font='tajawal 15')
            l99.place(x=150,y=550)



        q1 =IntVar()
        q2 =IntVar()
        q3 =IntVar()
        q4 =IntVar()
        q5 =IntVar()
        q6 =IntVar()
        q7 =IntVar()
        q8 =IntVar()
        q9 =IntVar()
        q10 =IntVar()


        e3=Entry(f3,width=20,textvariable=q1)
        e3.place(x=160,y=155)
        e4=Entry(f3,width=20,textvariable=q2)
        e4.place(x=160,y=185)
        e5=Entry(f3,width=20,textvariable=q3)
        e5.place(x=160,y=215)
        e6=Entry(f3,width=20,textvariable=q4)
        e6.place(x=160,y=245)
        e7=Entry(f3,width=20,textvariable=q5)
        e7.place(x=160,y=275)
        e8=Entry(f3,width=20,textvariable=q6)
        e8.place(x=160,y=305)
        e9=Entry(f3,width=20,textvariable=q7)
        e9.place(x=160,y=335)
        e10=Entry(f3,width=20,textvariable=q8)
        e10.place(x=160,y=365)
        e11=Entry(f3,width=20,textvariable=q9)
        e11.place(x=160,y=395)
        e12=Entry(f3,width=20,textvariable=q10)
        e12.place(x=160,y=425)

        b5=Button(f3,text='The account',bg='#4CB3A2',fg='white',width=12,height=1,font="Courier 15",command=total)
        b5.place(x=120,y=480)

        root.mainloop()

    else:
        messagebox.showerror('INCORRESCT MODE PASS', 'INCORRECT MOD PASS')


f1=Frame(windo,width=200,height=500,bg='#5B277C')
f1.place(x=500,y=29)
f2=Frame(windo,width=500,height=300,bg='#5B277C')
f2.place(x=0,y=350)

l1=Label(windo,text='Time Organization',bg='#4CB3A2',fg='white',font="Courier 15 bold",height=1)
l1.pack(fill=X)
photo = PhotoImage(file=('x.png'))
l2=Label(windo,image=photo).place(x=100,y=50)
l3=Label(f1,text='THIS PROJECT \nFROM ZAKARIA SALHI',bg='#5B277C',fg='white',font="Courier 12 bold")
l3.place(x=10,y=20)
l4=Label(f2,text='ID',bg='#5B277C',fg='white',font="Courier 15 bold")
l4.place(x=120,y=30)
l5=Label(f2,text='PASSWORD',bg='#5B277C',fg='white',font="Courier 15 bold")
l5.place(x=50,y=80)

b1=Button(f1,text='ABOUT PROJECT',bg='#4CB3A2',fg='white',width=15,height=2,font="Courier 15",command=zaka)
b1.place(x=6,y=100)
b2=Button(f1,text='youtube',bg='red',fg='white',width=8,height=1,font="Courier 8",command=zaka1)
b2.place(x=70,y=445)
b3=Button(f1,text='facebook',bg='blue',fg='white',width=8,height=1,font="Courier 8",command=zaka2)
b3.place(x=136,y=445)
b4=Button(f1,text='QUIT',bg='#4CB3A2',fg='white',width=15,height=2,font="Courier 15",command=quit)
b4.place(x=6,y=170)
b5=Button(f2,text='ENTER',bg='#4CB3A2',fg='white',width=10,height=4,font="Courier 10",command=zaka3)
b5.place(x=380,y=35)

e1=Entry(f2,width=30)
e1.place(x=180,y=35)
e2=Entry(f2,width=30)
e2.place(x=180,y=85)

windo.mainloop()
