from tkinter import *

window = Tk()
window.minsize(width=500, height=500)
window.title("Mile to Km Converter")

entry = Entry()
entry.grid(column=1, row=0)

milesLabel = Label(text="Miles")
milesLabel.grid(column=2, row=0)

equalToLabel = Label(text="is equal to: ")
equalToLabel.grid(column=0, row=1)

kmLabel = Label(text="Km")
kmLabel.grid(column=2, row=1)

convertedValue = Label(text="0")
convertedValue.grid(column=1, row=1)


def calculate():
    miles = float(entry.get())
    km = round(miles * 1.609, 3)
    convertedValue.config(text=str(km))


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)
window.mainloop()
