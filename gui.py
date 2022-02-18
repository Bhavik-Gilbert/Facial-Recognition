import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
import tkcalendar as calendar

from functions import empty

from form_output import login, signup, retake_image, confirm_image, cancel_images

def create_entry(text:str, frame, type:int=0):
        label = tk.Label(frame, text=text, bg="#000", fg="#fff", font=('Silkscreen',14,'italic'))
        label.pack()

        if(type == 0):
            entry = tk.Entry(frame, bg="#4B4B4C", fg="#fff", width=50)
        if(type == 1):
            entry = calendar.DateEntry(frame, width=50, bg="#4B4B4C", fg="#fff")

        entry.pack(pady=10) 

        return entry

def spacing(n:int, frame):
        for i in range(0,n):
            top_spaing = tk.Label(frame, text='', bg="#000")
            top_spaing.pack()

def create_frame(window,title:str):
    window.title(title)
    frame = tk.Frame(window, background="#000")
    frame.pack()

    return frame

def open_gui():
    window = tk.Tk()
    window.geometry("800x800")
    window.configure(background="#000")
    
    login_gui(window)

    window.mainloop()

def login_gui(window):
    def login_click():
        message, compare = login(username.get())
        if(compare):
            frame.destroy()
            logged_in_gui(window)

        if not empty(message):
            messagebox.showerror('Input Error', message)

    def signup_click():
        frame.destroy()
        signup_gui(window)

    frame = create_frame(window, "Login")

    spacing(2, frame)
    title = tk.Label(frame, text="Login", bg="#000", fg="#fff", font=('Silkscreen',20,'bold','underline'))
    title.pack()
    
    spacing(2, frame)

    username = create_entry("Username", frame)

    spacing(2, frame)
    login_button = tk.Button(master=frame, text="Login", bg='#4B4B4C', fg='#fff', command=login_click, padx=20, pady=5) 
    login_button.pack()
    spacing(1, frame)
    signup_button = tk.Button(master=frame, text="Signup", bg='#2f374a', fg='#fff', command=signup_click, padx=20, pady=5)
    signup_button.pack()


def signup_gui(window):
    def login_click():
        frame.destroy()
        login_gui(window)

    def signup_click():
        message, valid = signup(username.get(),firstname.get(), surname.get(), email.get(), dob.get())

        global invalid
        invalid = False

        if not(empty(message)):
            invalid = True

        if valid:
            frame.destroy()
            image_gui(window)
        
        if not(empty(message)):
            messagebox.showerror('Input Error', message)

    frame = create_frame(window, "Signup")

    spacing(2, frame)
    title = tk.Label(frame, text="Signup", bg="#000", fg="#fff", font=('Silkscreen',20,'bold','underline'))
    title.pack()

    spacing(2, frame)

    username = create_entry("Username", frame)
    firstname = create_entry("Firstname", frame)
    surname = create_entry("Surname", frame)
    email = create_entry("Email", frame)
    dob = create_entry("Date of Birth", frame, 1)


    spacing(2, frame)
    signup_button = tk.Button(master=frame, text="Signup", bg='#4B4B4C', fg='#fff', command=signup_click, padx=20, pady=5)
    signup_button.pack()
    spacing(1, frame)
    login_button = tk.Button(master=frame, text="Login", bg='#2f374a', fg='#fff', command=login_click, padx=20, pady=5) 
    login_button.pack()

def image_gui(window):
    def confirm_click():
        upload = confirm_image()
        if(upload):
            messagebox.showerror('Complete', "Signup Successful")
            frame.destroy()
            login_gui(window)
        else:
            messagebox.showerror('Error', "Couldn't upload image to database")

    def retake_click():
        message = retake_image()

        global invalid
        invalid = False

        if not(empty(message)):
            invalid = True

        frame.destroy()
        image_gui(window)

        if not(empty(message)):
            messagebox.showerror('Input Error', message)
    
    def cancel_click():
        cancel_images()
        
        frame.destroy()
        login_gui(window)

        messagebox.showerror('Cancel', "Signup Cancelled Successfully")
        

    frame = create_frame(window, "Picture")

    spacing(2, frame)

    img = tk.PhotoImage(file='person.png')
    panel = tk.Label(frame,image=img)
    panel.photo = img
    panel.pack()

    spacing(2, frame)

    if not(invalid):
        confirm_button = tk.Button(master=frame, text="Confirm", bg='#4B4B4C', fg='#fff', command=confirm_click, padx=20, pady=5)
        confirm_button.pack()
        spacing(1, frame)

    retake_button = tk.Button(master=frame, text="Retake", bg='#2f374a', fg='#fff', command=retake_click, padx=20, pady=5) 
    retake_button.pack()

    spacing(1, frame)
    cancel_button = tk.Button(master=frame, text="Cancel", bg='#73081a', fg='#fff', command=cancel_click, padx=20, pady=5) 
    cancel_button.pack()

def logged_in_gui(window):
    def logout_click():
        frame.destroy()

        login_gui(window)
        messagebox.showerror('Logout', "Logged out Successfully")

    frame = create_frame(window, "Logged In")

    spacing(1, frame)

    label = tk.Label(frame, text="Welcome", bg="#000", fg="#fff", font=('Silkscreen',20,'italic'))
    label.pack()

    spacing(2, frame)

    cancel_button = tk.Button(master=frame, text="Logout", bg='#73081a', fg='#fff', command=logout_click, padx=20, pady=5) 
    cancel_button.pack()




open_gui()