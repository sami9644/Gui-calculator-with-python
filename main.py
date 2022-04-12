from tkinter import *

c = Tk()
c.geometry('200x250')
screen = Entry(c,width = 60)
screen.place(x=0,y=0)

def disp(numb):
    cur = screen.get()
    screen.delete(0, END)
    screen.insert(0,str(cur)+str(numb))

def equals ():
    temp = str(screen.get())
    screen.delete(0,END)
    screen.insert(0,eval(temp))

btn7 = Button(c,text = "7",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("7"))
btn8 = Button(c,text = "8",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("8"))
btn9 = Button(c,text = "9",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("9"))
btndel = Button(c,text = "DEL",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : screen.delete(0,END))

btn7.place(x=0,y=20)
btn8.place(x=50,y=20)
btn9.place(x=100,y=20)
btndel.place(x=150,y=20)

btn4 = Button(c,text = "4",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("4"))
btn5 = Button(c,text = "5",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("5"))
btn6 = Button(c,text = "6",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("6"))
btndiv = Button(c,text = "/",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("/"))

btn4.place(x=0,y= 60)
btn5.place(x=50,y= 60)
btn6.place(x=100,y=60)
btndiv.place(x=150,y= 60)

btn1 = Button(c,text = "1",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("1"))
btn2 = Button(c,text = "2",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("2"))
btn3 = Button(c,text = "3",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("3"))
btnmul = Button(c,text = "*",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("*"))

btn1.place(x =0,y=100)
btn2.place(x =50,y=100)
btn3.place(x =100,y=100)
btnmul.place(x =150,y=100)

btn0 = Button(c,text = "0",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("0"))
btndot = Button(c,text = ".",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("."))
btneq = Button(c,text = "=",padx=20,pady=10,bg = "black",fg="white",bd = 0,command = equals)
btnmin = Button(c,text = "-",padx=25,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("-"))

btn0.place(x=0,y=140)
btndot.place(x=50,y=140)
btneq.place(x=95,y=140)
btnmin.place(x=145,y=140)

btnadd = Button(c,text = "+",padx=25,pady=10,bg = "black",fg="white",bd = 0,command = lambda : disp("+"))
btnadd.place(x=0,y=180)

c.mainloop()