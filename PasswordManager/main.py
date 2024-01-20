from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
emailEntry = Entry(width=35)
emailEntry.grid(columnspan=2, column=1, row=2)
passwordEntry = Entry(width=21)
passwordEntry.grid(column=1, row=3)
# Buttons
generatePassButton = Button(text="Generate Password")
generatePassButton.grid(column=2, row=3)
addButton = Button(text="Add", width=36)
addButton.grid(columnspan=2, column=1, row=4)

window.mainloop()
