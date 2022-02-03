
from re import S
import tkinter as tk

from form_output import login,signup

def open_gui():
    def create_entry(label):
        label = tk.Label(text=label, bg="#000", fg="#fff", font=('Silkscreen',14,'italic'))
        label.pack()

        entry = tk.Entry(bg="#4B4B4C", fg="#fff", width=50)
        entry.pack(pady=10)

        return entry
    
    def spacing(n:int):
        for i in range(0,n):
            top_spaing = tk.Label(text='', bg="#000")
            top_spaing.pack()
    
    def login_click():
        login(firstname.get(), surname.get())

    def signup_click():
        signup(firstname.get(), surname.get(), email.get(), dob.get())


    window = tk.Tk()
    window.title("Login")
    window.geometry("800x800")
    window.configure(background="#000")

    spacing(2)
    title = tk.Label(text="Login", bg="#000", fg="#fff", font=('Silkscreen',20,'bold','underline'))
    title.pack()
    spacing(2)

    firstname = create_entry("Firstname")
    surname = create_entry("Surname")
    email = create_entry("Email")
    dob = create_entry("Date Of Birth")

    spacing(2)
    login_button = tk.Button(master=window, text="Login", bg='#4B4B4C', fg='#fff', command=login_click, padx=20, pady=5) 
    login_button.pack()
    spacing(1)
    signup_button = tk.Button(master=window, text="Signup", bg='#4B4B4C', fg='#fff', command=signup_click, padx=20, pady=5)
    signup_button.pack()

    window.mainloop()
    
open_gui()