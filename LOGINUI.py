from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()
root.title('LIBRARY')
root.geometry('480x320')
root.iconbitmap(r"E:\ajayKarthik\Py\Projects\images\library2.ico")

# for storing string datatype
emailVariable = StringVar()
passVariable = StringVar()

# connecting to DB and adding record of new user
def connectAndAdd():
    nameVar, newEmailVar, newPassVar = nameEntry.get(),newEmailIdEntry.get(),newPasswordEntry.get()
    values=(nameVar,newEmailVar,newPassVar)

    conn = sqlite3.connect('usersDB')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES (?,?,?)",values)
    print(values)
    print('Added')
    
    conn.commit()
    conn.close()

    messagebox.showinfo('SUCESS',message='Account created successfully!')
    
    top.destroy()


# new window for new user registration
def createNewAccount():
    global top
    top = Toplevel()
    top.title('REGISTRATION')
    top.geometry('480x320')

    nameLabel = Label(top, text="Name", fg='green', font='Courier 10 bold')
    newEmailIdLabel = Label(top, text='Email-ID', fg='green', font='Courier 10 bold')
    newPasswordLabel = Label(top, text='Password', fg='green', font='Courier 10 bold')

    global nameEntry
    global newEmailIdEntry
    global newPasswordEntry
    nameEntry=Entry(top, width=35, bd=5)
    newEmailIdEntry=Entry(top, width=35, bd=5)
    newPasswordEntry=Entry(top, width=35, bd=5)
    
    createButton = Button(top, text='CREATE', command=connectAndAdd, padx=35, activebackground='green')

    nameLabel.place(x=60,y=40)
    newEmailIdLabel.place(x=60,y=80)
    newPasswordLabel.place(x=60,y=120)
    nameEntry.place(x=135, y=40)
    newEmailIdEntry.place(x=135,y=80)
    newPasswordEntry.place(x=135,y=120)
    createButton.place(x=150,y=165)


# user log out function
def logOut():
    messagebox.showinfo(title='LOGGED-OUT',message='Successfully logged out!')
    top2.destroy()
    print("Log-In session over")


# logging in user
def loggingIn():
    emailVariable=emailIdEntry.get()
    passVariable=passwordEntry.get()
    

    connection=sqlite3.connect('usersDB')
    c=connection.cursor()

    c.execute("SELECT name, password FROM users WHERE email=(?)",[emailVariable])
    result=c.fetchone()
    try:
        if result[1]==passVariable:
            details=True
            messagebox.showinfo('SUCCESS',message=f"Welcome {result[0]}!")
            print('Log-In session started')
        else:
            details=False
            messagebox.showinfo('RE-TRY',message="Wrong Credentials! (OR) No account. Please Try Again ")
    except TypeError:
        details=False
        messagebox.showinfo('RE-TRY',message="Wrong Credentials! (OR) No account. Please Try Again")
    
    # displaying user data
    global top2
    if details==True:
        top2 = Toplevel()
        top2.title('REGISTRATION')
        top2.geometry('480x320')

        l1=Label(top2,text='Your details are:')
            
        c.execute('SELECT * FROM users WHERE email=(?) AND password=(?)',[emailVariable,passVariable])
        data = c.fetchone()
            
        l2=Label(top2,text=data[0])
        l3=Label(top2,text=data[1])
        l4=Label(top2,text=data[2])

        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()

        connection.commit()

        logoutButton=Button(top2,text='LOGOUT',command=logOut)
        logoutButton.pack()
        
        connection.close()
        

# global scope from here

# Labels
titleLabel=Label(root,text="WELCOME TO LIBRARY",font='Stencil', fg='red')
emailIdLabel = Label(root, text='Email-ID',font='Courier 10 bold', fg='blue')
passwordLabel = Label(root, text='Password',font='Courier 10 bold', fg='blue')
newUserCheckLabel = Label(root, text='ARE YOU NEW? CLICK YES TO CREATE A NEW ACCOUNT.',font='TimesNewRoman 10 bold')

# Entry boxes
emailIdEntry = Entry(root, textvariable=emailVariable, width=35, bd=5)
passwordEntry = Entry(root, textvariable=passVariable, show='*', width=35, bd=5)

# Buttons
submit = Button(root, text='SUBMIT', command=loggingIn, fg='green', activebackground='green',padx=40)
c = Button(root, text='YES', command=createNewAccount, fg='green', activebackground='green', padx=30)


titleLabel.place(x=150,y=15)
emailIdLabel.place(x=60,y=80)
passwordLabel.place(x=60,y=120)
newUserCheckLabel.place(x=0,y=220)
c.place(x=135,y=250)
emailIdEntry.place(x=135,y=80)
passwordEntry.place(x=135,y=120)
submit.place(x=150,y=165)

root.mainloop()
