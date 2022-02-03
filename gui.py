
import tkinter as tk

from form_output import login,signup

def create_entry(label, frame):
        label = tk.Label(frame, text=label, bg="#000", fg="#fff", font=('Silkscreen',14,'italic'))
        label.pack()

        entry = tk.Entry(frame, bg="#4B4B4C", fg="#fff", width=50)
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
        login(firstname.get(), surname.get())

    def signup_click():
        frame.destroy()
        signup_gui(window)

    frame = create_frame(window, "Login")

    spacing(2, frame)
    title = tk.Label(frame, text="Login", bg="#000", fg="#fff", font=('Silkscreen',20,'bold','underline'))
    title.pack()
    spacing(2, frame)

    firstname = create_entry("Firstname", frame)
    surname = create_entry("Surname", frame)

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
        signup(firstname.get(), surname.get(), email.get(), dob.get())

    frame = create_frame(window, "Signup")

    spacing(2, frame)
    title = tk.Label(frame, text="Signup", bg="#000", fg="#fff", font=('Silkscreen',20,'bold','underline'))
    title.pack()
    spacing(2, frame)

    firstname = create_entry("Firstname", frame)
    surname = create_entry("Surname", frame)
    email = create_entry("Email", frame)
    dob = create_entry("Date of Birth", frame)


    spacing(2, frame)
    signup_button = tk.Button(master=frame, text="Signup", bg='#4B4B4C', fg='#fff', command=signup_click, padx=20, pady=5)
    signup_button.pack()
    spacing(1, frame)
    login_button = tk.Button(master=frame, text="Login", bg='#2f374a', fg='#fff', command=login_click, padx=20, pady=5) 
    login_button.pack()

    
open_gui()