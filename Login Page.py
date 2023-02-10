from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root=Tk()
root.title("Login")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=userbox.get()
    password=passbox.get()

    if username=="admin" and password=="1234":
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        Label(screen,text="Josh Welcomes You", bg="#fff", font=("Century Gothic", 32, "bold")).pack(expand=True)
        
        screen.mainloop()
    elif username!="admin" and password!="1234":
        messagebox.showerror("Error", "Check username or password")

    elif password!="1234":
        messagebox.showerror("Error", "Incorrect password")

    elif username!= "admin":
        messagebox.showerror("Error", "Check username or password")
# Open Image
Login_img = Image.open("Login_Image.png")

#Resize Image
resized = Login_img.resize((350, 425), Image.ANTIALIAS)

#Define Image (Original Size: 6000x4000)
new_login_img=ImageTk.PhotoImage(resized)
Login_label=Label(root,image=new_login_img).place(x=50,y=50)

#Login frame
frame=Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

#Header
heading=Label(frame, text= "User Login", fg="#57a1f8", bg="white", font=("Century Gothic", 24))
heading.place(x=90, y=0)

#Function to delete "Enter Username" prompt from field when clicked in.
def on_enter(e):
    userbox.delete(0, "end")

#Function to restore "Enter Username" prompt from field when clicked out.
def on_exit(x):
    name=userbox.get()
    if name=="":
        userbox.insert(0, "Enter Username")

userbox = Entry(frame,width=25,fg="black", border=0, bg="white", font=("Century Gothic", 11))
userbox.place(x=70, y=120)
userbox.insert(0, "Enter Username")
userbox.bind("<FocusIn>", on_enter)
userbox.bind("<FocusOut>", on_exit)

Frame(frame, width=202,height=2,bg="black").place(x=70,y=140)

#Function to delete "Enter Password" prompt from field when clicked in.
def on_enter(e):
    passbox.delete(0, "end")

#Function to restore "Enter Password" prompt from field when clicked out.
def on_exit(x):
    name=passbox.get()
    if name=="":
        passbox.insert(0, "Enter Password")

passbox = Entry(frame,width=25,fg="black", border=0, bg="white", font=("Century Gothic", 11))
passbox.place(x=70, y=200)
passbox.insert(0, "Enter Password")
passbox.bind("<FocusIn>", on_enter)
passbox.bind("<FocusOut>", on_exit)

Frame(frame, width=202,height=2,bg="black").place(x=70,y=220)


signin_button=Button(frame,width=25,pady=7,text="Sign In", bg="#57a1f8", fg="white", cursor="hand2",  command=signin, font=("Century Gothic", 14), border=0)
signin_button.place(x=30,y=250)
signup_label=Label(frame,text="Don't have an account?", fg="black",bg="white",font=("Century Gothic", 8))
signup_label.place(x=70,y=300)

signup_button=Button(frame,width=6, text="Sign Up",border=0, bg="white",cursor="hand2", fg="#57a1f8")
signup_button.place(x=220, y=300)
root.mainloop()
