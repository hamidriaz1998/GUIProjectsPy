from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

# Logo
logo = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
websiteLabel = Label(text="Website:")
websiteLabel.grid(column=0, row=1)
emailLabel = Label(text="Email/Username:")
emailLabel.grid(column=0, row=2)
passwordLabel = Label(text="Password:")
passwordLabel.grid(column=0, row=3)

# Entries
websiteEntry = Entry(width=35)
websiteEntry.grid(columnspan=2, column=1, row=1)
websiteEntry.focus()
emailEntry = Entry(width=35)
emailEntry.grid(columnspan=2, column=1, row=2)
emailEntry.insert(0, "example@ex.com")
passwordEntry = Entry(width=21)
passwordEntry.grid(column=1, row=3)
# Buttons
generatePassButton = Button(text="Generate Password")
generatePassButton.grid(column=2, row=3)
addButton = Button(text="Add", width=36)
addButton.grid(columnspan=2, column=1, row=4)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    passwordEntry.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password = ''
    password += ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=nr_letters))
    password += ''.join(random.choices('!@#$%^&*()', k=nr_symbols))
    password += ''.join(random.choices('0123456789', k=nr_numbers))
    passwordEntry.insert(0, password)
    pyperclip.copy(password)
generatePassButton.config(command=generate_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(websiteEntry.get()) == 0 or len(passwordEntry.get()) == 0 or len(emailEntry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    is_ok = messagebox.askokcancel(title=websiteEntry.get(), message=f"These are the details entered: \nEmail: {emailEntry.get()}\nPassword: {passwordEntry.get()}\nIs it ok to save?")
    if not is_ok:
        return
    with open("data.txt", "a") as file:
        file.write(f"{websiteEntry.get()}\t{emailEntry.get()}\t{passwordEntry.get()}\n")
    websiteEntry.delete(0, END)
    passwordEntry.delete(0, END)
addButton.config(command=save)
# ---------------------------- MAIN LOOP ------------------------------- #
window.mainloop()