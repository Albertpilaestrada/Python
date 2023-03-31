from tkinter import *
from tkinter import messagebox
import sqlite3

#-------------------functions-------------------------------------

def bbdd_conect():
    my_conection=sqlite3.connect("Users")
    my_pointer=my_conection.cursor()
    
    try:
        my_pointer.execute('''
        CREATE TABLE USERDATA(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(20), 
        PASSWORD VARCHAR(25), 
        LASTNAME VARCHAR(20),
        ADDRESS VARCHAR(50),
        COMMENTS VARCHAR(250))
        ''')
        messagebox.showinfo("BBDD","BBDD successfully created")
    except:
        messagebox.showwarning("!Attention¡","The BBDD already exists")

def exitapi():
    value=messagebox.askquestion("Exit","Do you want to exit the application?")
    if value=="yes":
        root.destroy()

def fiel_delete():
    myid.set("")
    myname.set("")
    mypass.set("")
    mylastname.set("")
    mydirr.set("")
    commenttext.delete("1.0",END)

def create():#we must use parameterized queries to avoid sql injection, so this code is vulnerable
    my_conection=sqlite3.connect("Users")
    my_pointer=my_conection.cursor()
    #we must use parameterized queries to avoid sql injection, so this code is vulnerable
    """my_pointer.execute("INSERT INTO USERDATA VALUES( NULL , '"+myname.get()+
                       "','"+mypass.get()+
                       "','"+mylastname.get()+
                       "','"+mydirr.get()+
                       "','"+commenttext.get("1.0",END)+"')")"""
    data=myname.get(),mypass.get(),mylastname.get(),mydirr.get(),commenttext.get("1.0",END)
    my_pointer.execute("INSERT INTO USERDATA VALUES(NULL,?,?,?,?,?)",(data))
    my_conection.commit()
    messagebox.showinfo("BBDD","Register successfully inserted")
    

def read():
    my_conection=sqlite3.connect("Users")
    my_pointer=my_conection.cursor()

    my_pointer.execute("SELECT * FROM USERDATA WHERE ID="+myid.get())
    user=my_pointer.fetchall()
    for u in user:
        myid.set(u[0])
        myname.set(u[1])
        mypass.set(u[2])
        mylastname.set(u[3])
        mydirr.set(u[4])
        commenttext.insert(1.0,u[5])
    my_conection.commit()

def update():
    my_conection=sqlite3.connect("Users")
    my_pointer=my_conection.cursor()

    """my_pointer.execute("UPDATE USERDATA SET NAME='"+myname.get()+
                       "',PASSWORD='"+mypass.get()+
                       "',LASTNAME='"+mylastname.get()+
                       "',ADDRESS='"+mydirr.get()+
                       "',COMMENTS'"+commenttext.get("1.0",END)+
                       "' WHERE ID="+myid.get())"""
    data=myname.get(),mypass.get(),mylastname.get(),mydirr.get(),commenttext.get("1.0",END)
    my_pointer.execute("UPDATE USERDATA SET NAME=?, PASSWORD=?, LASTNAME=?, ADDRESS=?, COMMENTS=? "+
                       "WHERE ID="+myid.get(),(data))
    my_conection.commit()
    messagebox.showinfo("BBDD","Register successfully updated")

def delete():
    my_conection=sqlite3.connect("Users")
    my_pointer=my_conection.cursor()

    my_pointer.execute("DELETE FROM USERDATA WHERE ID="+myid.get())
    my_conection.commit()
    messagebox.showinfo("BBDD","Register successfully deleted")

#-------------------graphics interface----------------------------

root=Tk()

menu_bar=Menu(root)
root.config(menu=menu_bar,width=300,height=300)

bbdd_menu=Menu(menu_bar,tearoff=0)
bbdd_menu.add_command(label="Conect",command=bbdd_conect)
bbdd_menu.add_command(label="Exit",command=exitapi)

del_menu=Menu(menu_bar,tearoff=0)
del_menu.add_command(label="Delete",command=fiel_delete)

crud_menu=Menu(menu_bar,tearoff=0)
crud_menu.add_command(label="Create",command=create)
crud_menu.add_command(label="Read",command=read)
crud_menu.add_command(label="Update",command=update)
crud_menu.add_command(label="Delete",command=delete)

help_menu=Menu(menu_bar,tearoff=0)
help_menu.add_command(label="License")
help_menu.add_command(label="About...")

menu_bar.add_cascade(label="BBDD",menu=bbdd_menu)
menu_bar.add_cascade(label="Delete",menu=del_menu)
menu_bar.add_cascade(label="CRUD",menu=crud_menu)
menu_bar.add_cascade(label="Help",menu=help_menu)

#-------------------field strat----------------------------

myframe=Frame(root)
myframe.pack()

myid=StringVar()
myname=StringVar()
mypass=StringVar()
mylastname=StringVar()
mydirr=StringVar()

idfield=Entry(myframe,textvariable=myid)
idfield.grid(row=0,column=1,padx=10,pady=10)

namefield=Entry(myframe,textvariable=myname)
namefield.grid(row=1,column=1,padx=10,pady=10)

passfield=Entry(myframe,textvariable=mypass)
passfield.grid(row=2,column=1,padx=10,pady=10)
passfield.config(show="*")

lastnamefield=Entry(myframe,textvariable=mylastname)
lastnamefield.grid(row=3,column=1,padx=10,pady=10)

dirrfield=Entry(myframe,textvariable=mydirr)
dirrfield.grid(row=4,column=1,padx=10,pady=10)

commenttext=Text(myframe,width=16,height=5)
commenttext.grid(row=5,column=1,padx=10,pady=10)
scrollver=Scrollbar(myframe,command=commenttext.yview)
scrollver.grid(row=5,column=2,sticky="nsew")
commenttext.config(yscrollcommand=scrollver)

#-------------------------label strat------------------------

idlabel=Label(myframe,text="ID:")
idlabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

namelabel=Label(myframe,text="Name:")
namelabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passlabel=Label(myframe,text="Password:")
passlabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

lastnamelabel=Label(myframe,text="Last Name:")
lastnamelabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

dirrlabel=Label(myframe,text="Address:")
dirrlabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

commentlabel=Label(myframe,text="Comments:")
commentlabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#----------------------------------buttons here--------------------------------

myframe2=Frame(root)
myframe2.pack()

createbutton=Button(myframe2,text="Create",command=create)
createbutton.grid(row=1,column=0,sticky="e",padx=10,pady=10)

readbutton=Button(myframe2,text="Read",command=read)
readbutton.grid(row=1,column=1,sticky="e",padx=10,pady=10)

updatebutton=Button(myframe2,text="Update",command=update)
updatebutton.grid(row=1,column=2,sticky="e",padx=10,pady=10)

deletebutton=Button(myframe2,text="Delete",command=delete)
deletebutton.grid(row=1,column=3,sticky="e",padx=10,pady=10)

root.mainloop()