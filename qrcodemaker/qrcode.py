from tkinter import *
import qrcodemaker.qrcode as qrcode

windo = Tk()
windo.geometry('500x400+300+50')
windo.resizable(False,False)
windo.title('MAKE QRCODE')

def qr():
    a = e1.get()
    b = e2.get()
    img = qrcode.make(a)
    img.save(b+'.png')

l1=Label(windo,text='MAKE YOUR OWN QRCODE FOR FREE',font='Courier 15 bold',bg='black',fg='white')
l1.pack(fill=X)

f1=Frame(width=400,height=300,bg='black')
f1.place(x=50,y=80)

l2=Label(f1,text='MAKE QRCODE',font='Courier 15 bold',bg='black',fg='white')
l2.place(x=150,y=20)

l3=Label(f1,text='INSIDE QR',font='Courier 12 bold',bg='black',fg='white')
l3.place(x=45,y=100)
l4=Label(f1,text='THE NAME',font='Courier 12 bold',bg='black',fg='white')
l4.place(x=45,y=150)

b1=Button(f1,text='SAVE',bg='black',fg='white',font='tajawal 13',width=20,command=qr)
b1.place(x=150,y=200)

e1=Entry(f1,width=30)
e1.place(x=150,y=100)
e2=Entry(f1,width=30)
e2.place(x=150,y=150)

windo.mainloop()
