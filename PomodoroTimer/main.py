from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    countDown(60 * 5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    countMinutes = floor(count / 60)
    countSeconds = count % 60
    text = f"{countMinutes}:"
    if countSeconds == 0:
        text += "00"
    elif countSeconds < 10:
        text += f"0{countSeconds}"
    else:
        text += str(countSeconds)

    canvas.itemconfig(timerText, text=text)
    if count > 0:
        window.after(1000, countDown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(
    text="Timer",
    fg=GREEN,
    font=(FONT_NAME, 35, "bold"),
    bg=YELLOW,
    highlightthickness=0,
)
label.grid(column=1, row=0)

image = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(101, 112, image=image)
timerText = canvas.create_text(
    103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

startButton = Button(text="Start", highlightthickness=0, command=startTimer)
startButton.grid(column=0, row=2)

resetButton = Button(text="reset")
resetButton.grid(column=2, row=2)

window.mainloop()
