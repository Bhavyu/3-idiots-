from tkinter import *
import tkinter as tk
from datetime import *




def sec_frame():
    global f2
    f2=Frame()
    f2.pack()
    f2.place(width=1700,height=500,x=0,y=500)
    f2.config(bg="yellow")

def new_cust():
    global f2
    global name_text
    global n
    
    sec_frame()
    
    name_text=Entry(bd=8,font=(14))
    Label(f2,text="Name",bg="cyan",font=(8)).place(x=30,y=55)
    name_text.place(x=95,y=550)
    

    name_text=Entry(bd=8,font=(14),textvariable=n)
    Label(f2,text="Company Name",bg="cyan",font=(8)).place(x=30,y=105)
    name_text.place(x=185,y=600)
    

    name_text=Entry(bd=8,font=(14))
    Label(f2,text="Mobile",bg="cyan",font=(8)).place(x=30,y=155)
    name_text.place(x=105,y=650)

    name_text=Entry(bd=8,font=(14))
    Label(f2,text="Email",bg="cyan",font=(8)).place(x=30,y=200)
    name_text.place(x=100,y=700)

    add=Button(f2,text="Add",width=5,height=1,bg='pink',bd=8,command=lambda:add_new_entry(n))
    add.place(x=200,y=250)

def add_new_entry(num1):
    global c
    global name_text
    global n
    global w
    global tkvar
    print(num1)  #PY_var
    no=(num1.get())
    c.insert(2,no)
    print(no)  #input
    print(c)  #list
    w=OptionMenu(mf,tkvar,*c)
    Label(mf,text="Select any account",font=(10),bg="yellow").place(x=35,y=130)
    w.place(x=210,y=120)
    w.config(bd=10,bg="white",fg="blue",font=(14))
    tkvar.set(no)


    

def remove_cust():
    global f2
    sec_frame()
    name_text=Entry(bd=8,font=(14))
    Label(f2,text="Name",bg="cyan",font=(8)).place(x=30,y=55)
    name_text.place(x=95,y=550)

    name2_text=Entry(bd=8,font=(14))
    Label(f2,text="Company Name",bg="cyan",font=(8)).place(x=30,y=105)
    name2_text.place(x=185,y=600)

    remove=Button(f2,text="Delete",width=5,height=1,bg='pink',bd=8,command=lambda:delete_entry())
    remove.place(x=175,y=155)

def delete_entry():
    global x
    global c
    global w
    global tkvar
    c.remove(x)
    w=OptionMenu(mf,tkvar,*c)
    Label(mf,text="Select any account",font=(10),bg="yellow").place(x=35,y=130)
    w.place(x=210,y=120)
    w.config(bd=10,bg="white",fg="blue",font=(14))
    tkvar.set("Select account")

def new_entry():
    sec_frame()
    """h=15
    w=5

    for i in range(h):     #rows
        for j in range(w):    #column
            b=Entry(f2, text="",width=30)
            b.grid(row=i,column=j)
        b.place(x=0,y=0)    
    l=Label(f2,text="option",font=(2),width=8,bg="white",height=0)
    l.grid(row=1,column=0)
    l.place(x=0,y=0)"""

    #dte=Entry(bd=8,font=(14))
    d=Label(f2,text="Date",bg="cyan",font=(8)).place(x=30,y=30)
    #dte.place(x=90,y=525)

    m=date.today()
    d2=m.strftime("%d.%B.%Y")
    #dte.insert(eval(d2))
    dte=Label(f2,text=d2,bg="red",font=(8)).place(x=90,y=30)


    E=datetime.strftime(datetime.now() - timedelta(1),"%d.%B.%Y")
    counter=0
    if E == m:
        counter=0
    else:
        counter=counter+1
        
    #entry_no=Entry(bd=8,font=(14))
    e1=Label(f2,text="Entry No",bg="cyan",font=(8)).place(x=405,y=30)
    #entry_no.place(x=600,y=525)
    e2=Label(f2,text=d2+"||"+str(counter),bg="red",font=(8)).place(x=510,y=30)

    global tkvar
    global n
    #tkvar=StringVar(root)

    t={'Black & white':"2",'Colour':"10",'Printout':"5",'Lamination (A5)':"20",'Lamination (A4)':"40",'Photocopy':"25",'Binding (Thread)':"50",'Binding (Sprial)':"40"}
    
    

    #tkvar.set("one")
    global p

    types=OptionMenu(f2,n,*t)
    Label(f2,text="Select Type",font=(10),bg="cyan").place(x=25,y=85)
    types.place(x=140,y=75)
    types.config(bd=10,bg="cyan",fg="red",font=(14))

    rate=Entry(f2,bd=8,font=(14))
    Label(f2,text="Rate",bg="cyan",font=(8)).place(x=405,y=85)
    rate.place(x=470,y=80)

    pg=Entry(f2,bd=8,font=(14),textvariable=h)
    Label(f2,text="Quantity",bg="cyan",font=(8)).place(x=25,y=138)
    pg.place(x=110,y=135)
    
    
    
    global v
    #v.set("L")
   
    b1=Radiobutton(f2,text="Single",variable=v,value=1,bg="cyan",font=(8),bd=3).place(x=405,y=135)
    #b1.pack(anchor=W)
    #sb.place(x=50,y=59)

    b1=Radiobutton(f2,text="B2B",variable=v,value=2,bg="cyan",font=(8),bd=3).place(x=500,y=135)
    #b1.pack(anchor=W)

    
    dis=Entry(bd=8,font=(14))
    Label(f2,text="Discount",bg="cyan",font=(8)).place(x=25,y=195)
    dis.place(x=115,y=690)

    
    total_amt=Entry(bd=8,font=(14))
    Label(f2,text="Total",bg="cyan",font=(8)).place(x=405,y=195)
    total_amt.place(x=470,y=690)
    
    
    
    """fr=eval(rs)
    tat=f*fr
    total_amt.delete(0,END)
    total_amt.insert(0,eval(tat))"""

    final_total=Entry(f2,bd=8,font=(14))
    Label(f2,text="Final Amount",bg="cyan",font=(8)).place(x=25,y=255)
    final_total.place(x=150,y=250)

    
    submit=Button(f2,text="Submit!",width=8,height=1,bg='pink',bd=10,command=lambda:payment())
    submit.place(x=430,y=250)
    

    
    def change_dropdown2(*args):
        print(n.get())
        global n2
        n2=n.get()
        #f=n2
        #print(f)
        global rs
        rs=eval(t[n2])
        print(rs)
        rate.delete(0,END)
        rate.insert(0,rs)

    n.trace('w',change_dropdown2)

    def callback1(*x):
        
        f=eval(h.get())
        print(f)
        global tat
        global rs
        global bal
        #global f
        
        tat=f*rs
        print(tat)
        #global tat
        total_amt.delete(0,END)
        total_amt.insert(0,tat)

        bal=bal+tat
        final_total.delete(0,END)
        final_total.insert(0,bal)
        
        
        
    h.trace("w",callback1)
    




def payment():
    global f2
    sec_frame()
    
    cust_name=Entry(bd=8,font=(14))
    Label(f2,text="customer",bg="cyan",font=(8)).place(x=30,y=55)
    cust_name.place(x=130,y=600)

    Balance=Entry(bd=8,font=(14))
    Label(f2,text="Balance",bg="cyan",font=(8)).place(x=30,y=105)
    Balance.place(x=130,y=550)

    amt=Entry(bd=8,font=(14))
    Label(f2,text="Amount paid",bg="cyan",font=(8)).place(x=30,y=155)
    amt.place(x=155,y=650)

    r_bal=Entry(bd=8,font=(14))
    Label(f2,text="Remaining balance",bg="cyan",font=(8)).place(x=30,y=205)
    r_bal.place(x=225,y=700)

    submit=Button(f2,text="Submit",width=8,height=1,bg='pink',bd=8)
    submit.place(x=200,y=250)
    
def about():
    cust_name1=Entry(bd=8,font=(14))
    Label(mf,text="Customer",bg="cyan",font=(8)).place(x=1080,y=223)
    cust_name1.place(x=1175,y=215)

    mbl=Entry(bd=8,font=(14))
    Label(mf,text="Mobile",bg="cyan",font=(8)).place(x=1100,y=282)
    mbl.place(x=1175,y=277)

    eml=Entry(bd=8,font=(14))
    Label(mf,text="Email",bg="cyan",font=(8)).place(x=1100,y=335)
    eml.place(x=1175,y=335)


    
    

root=Tk()
root.title("XEROX MANAGEMENT ")
root.geometry("2000x1000")


mf=Frame(root)
mf.pack()
mf.place(width=1600,height=800,x=0,y=0)

mf.config(bg="light blue")

f2=Frame(root)


name_text=Entry()
tkvar=StringVar(root)
h=tk.StringVar(root)
n=tk.StringVar(root)
p=StringVar(root)
v=IntVar(root)
bal=0.0
rs=0
f=0
tat=0
c=['Suchit Academy','Programmatix','Garud','Phoenix','Vartak','Thakur']


#mf.grid(row=0,column=0)
#mf.grid(column=0,row=0,sticky=NSEW)

#mf.columnconfigure(0,weight=1)
#mf.rowconfigure(0,weight=1)
#mf.pack(pady=100,padx=100,fill="red")
#C:\Users\ADMIN\Desktop\python programs\GUI PYTHON

logo=tk.PhotoImage(file="final.gif")

pic=Label(mf,image=logo,height=120,width=500,bg="orange")#.place(x=0,y=0)
pic.pack()





#tkvar.set("one")

w=OptionMenu(mf,tkvar,*c)
Label(mf,text="Select any account",font=(10),bg="yellow").place(x=35,y=130)
w.place(x=210,y=120)
w.config(bd=10,bg="yellow",fg="red",font=(14))
tkvar.set("select any account")

bal_text=Entry(bd=8,font=(14))
Label(mf,text="Balance",bg="yellow",font=(14)).place(x=750,y=135)
bal_text.place(x=850,y=130)
#bal_text.set(eval(bal))
bal_text.delete(0,END)
bal_text.insert(0,bal)

abt=Button(mf,text="!About",width=8,height=1,bg='yellow',bd=8,command=lambda:about())
abt.place(x=1100,y=135)
##################################################
add_cust=Button(mf,text="+++ Add customer +++",font=(1),width=18,height=1,bg='light green',bd=15,command=lambda:new_cust())
add_cust.place(x=45,y=255)
#b1.config(bd=10)

del_cust=Button(mf,text="--- Delete customer ---",font=(1),width=18,height=1,bg='light green',bd=15,command=lambda:remove_cust())
del_cust.place(x=45,y=330)
#b2.config(bd=10)

add_entry=Button(mf,text="--> Add Entry <--",width=15,height=2,bg='red',bd=15,command=lambda:new_entry())
add_entry.place(x=400,y=255)
#b1.config(bd=10)

edit_entry=Button(mf,text="--> Edit Entry <--",width=15,height=2,bg='red',bd=15,command=lambda:new_entry())
edit_entry.place(x=400,y=330)
#b2.config(bd=10)


gen_bill=Button(mf,text="--> Generate Bill <--",width=15,height=2,bg='red',bd=15)
gen_bill.place(x=555,y=255)
#b1.config(bd=10)

pay=Button(mf,text="--> Make payment <-- ",width=18,height=2,bg='red',bd=15,command=lambda:payment())
pay.place(x=555,y=330)
#b2.config(bd=10)


x=''         







def change_dropdown(*args):
    print(tkvar.get())
    global x
    x=tkvar.get()
    

tkvar.trace('w',change_dropdown)


mainloop()
