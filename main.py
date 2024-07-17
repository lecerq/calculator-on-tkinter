from tkinter import *

bumbum=""

root=Tk()
root.title('Basicly calculator')
root.geometry('600x200')

def press(num):
    global bumbum
    bumbum = bumbum+(str(num))
    uran.set(bumbum)
def clear():
    global bumbum
    bumbum=""
    uran.set("")
def sum():
    global bumbum
    summa = str(eval(bumbum))
    uran.set(summa)
    bumbum=""
uran=StringVar()

uran_field = Entry(root, textvariable=uran)
uran_field.grid(columnspan=4, ipadx=90)
button=Button(text='1',command=lambda: press(1),height=1, width=7)
button.grid(row=2,column=0)
button2=Button(text='2',command=lambda: press(2),height=1, width=7)
button2.grid(row=2,column=1)
button3=Button(text='3',command=lambda: press(3),height=1, width=7)
button3.grid(row=2,column=2)
button4=Button(text='4',command=lambda: press(4),height=1, width=7)
button4.grid(row=3,column=0)
button5=Button(text='5',command=lambda: press(5),height=1, width=7)
button5.grid(row=3,column=1)
button6=Button(text='6',command=lambda: press(6),height=1, width=7)
button6.grid(row=3,column=2)
button7=Button(text='7',command=lambda: press(7),height=1, width=7)
button7.grid(row=4,column=0)
button8=Button(text='8',command=lambda: press(8),height=1, width=7)
button8.grid(row=4,column=1)
button9=Button(text='9',command=lambda: press(9),height=1, width=7)
button9.grid(row=4,column=2)
button0=Button(text='0',command=lambda: press(0),height=1, width=7)
button0.grid(row=5,column=0)
btnclear=Button(text='del',command=clear,height=1, width=7)
btnclear.grid(row=5,column=1)
btnp=Button(text='+',command=lambda: press('+'),height=1,width=7)
btnp.grid(row=2,column=3)
btnm=Button(text='-',command=lambda: press('-'),height=1,width=7)
btnm.grid(row=3,column=3)
btnu=Button(text='*',command=lambda: press('*'),height=1,width=7)
btnu.grid(row=4,column=3)
btnd=Button(text='/',command=lambda: press('/'),height=1,width=7)
btnd.grid(row=5,column=3)
summma=Button(text='sum',command=sum,height=1,width=7)
summma.grid(row=5,column=2)
root.mainloop()
