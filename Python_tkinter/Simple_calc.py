from tkinter import *

root = Tk()
# root.geometry("400x400")
root.title("Simple Calculator")
# root.iconbitmap(r"C:\Users\window10\Downloads\calc_icon.ico")
f1 = Frame(root)
f1.grid(row=0,column=0)

f2 = Frame(root)
f2.grid(row=1,column=0)



def update(o):
    la_var = label.cget('text')
    e_var = e.get()
    up = la_var + e_var + o
    label.config(text= up)

def onClick(number):
    current = e.get()
    update(" ")
    e.delete(0,END)
    e.insert(0,str(current) + str(number))


def Clear():
    e.delete(0,END)
    label.config(text="")


def Add(o):
    n1 = e.get()
    global num1
    num1 = n1
    update(" "+o+" ")
    e.delete(0, END)
    global op
    op = o



def Sub(o):
    n1 = e.get()
    global num1
    num1 = n1
    update(" "+o+" ")
    e.delete(0, END)
    global op
    op = o


def Mul(o):
    n1 = e.get()
    global num1
    num1 = n1
    update(" "+o+" ")
    e.delete(0, END)
    global op
    op = o


def Div(o):
    n1 = e.get()
    global num1
    num1 = n1
    update(" "+o+" ")
    e.delete(0, END)
    global op
    op = o


def Pow(o):
    n1 = e.get()
    global num1
    num1 = n1
    update(" "+o+" ")
    e.delete(0, END)
    global op
    op = o


def Eq(num1,op):
    num2 = e.get()
    if op == "+":
        result = int(num1) + int(num2)
    elif op == "-":
        result = int(num1) - int(num2)
    elif op == "*":
        result = int(num1) * int(num2)
    elif op == "/":
        result = int(num1) / int(num2)
    else:
        result = int(num1) ** int(num2)
    update(" = ")
    e.delete(0, END)
    e.insert(0,result)






e = Entry(f1,width=30,borderwidth=2,font=("Times New Roman",14,"normal"))
e.grid(row=1,column=0,columnspan=3,pady=2,padx=2,ipady=16)

label =Label(font=("Times New Roman",8,"normal"),fg="grey",bg="white")
label.place(x=5,y=5)



l7 = Button(f2,text=7,font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:onClick(7))
l8 = Button(f2,text=8,font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:onClick(8))
l9 = Button(f2,text=9,font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:onClick(9))
l4 = Button(f2,text=4,font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:onClick(4))
l5 = Button(f2,text=5,font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:onClick(5))
l6 = Button(f2,text=6,font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:onClick(6))
l1 = Button(f2,text=1,font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:onClick(1))
l2 = Button(f2,text=2,font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:onClick(2))
l3 = Button(f2,text=3,font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:onClick(3))
l0 = Button(f2,text=0,font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:onClick(0))
l_eq = Button(f2,text="=",font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda :Eq(num1,op))
l_clear = Button(f2,text="Clear",font=("Times New Roman",12,"bold"),height=2,width=8,command=Clear)
l_add = Button(f2,text="+",font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:Add("+"))
l_sub = Button(f2,text="-",font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:Sub("-"))
l_mul = Button(f2,text="*",font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:Mul("*"))
l_div = Button(f2,text="/",font=("Times New Roman",12,"bold"),height=2,width=8,command=lambda:Div("/"))
l_pow = Button(f2,text="**",font=("Times New Roman",12,"bold"),height=2,width=16,command=lambda:Pow("**"))



l7.grid(row=1,column=0,padx=2,pady=2)
l8.grid(row=1,column=1,pady=2)
l9.grid(row=1,column=2,padx=2,pady=2)
l4.grid(row=2,column=0,padx=2,pady=2)
l5.grid(row=2,column=1,pady=2)
l6.grid(row=2,column=2,padx=2,pady=2)
l1.grid(row=3,column=0,padx=2,pady=2)
l2.grid(row=3,column=1,pady=2)
l3.grid(row=3,column=2,padx=2,pady=2)
l0.grid(row=4,column=0,pady=2)
l_eq.grid(row=4,column=1,pady=2,)
l_clear.grid(row=4,column=2,pady=2,padx=2)
l_add.grid(row=5,column=0,padx=2,pady=2)
l_sub.grid(row=5,column=1,pady=2)
l_mul.grid(row=5,column=2,pady=2,padx=2)
l_div.grid(row=6,column=2,padx=2,pady=2)
l_pow.grid(row=6,column=0,pady=2,columnspan=2)


root.mainloop()