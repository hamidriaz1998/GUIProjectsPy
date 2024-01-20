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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    checkMarks.config(text="")
    label.config(text="Timer", bg=YELLOW, fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global reps
    reps += 1
    if reps == 8:
        countDown(SHORT_BREAK_MIN * 60)
        label.config(fg=RED, text="Break")
    elif reps % 2 == 0:
        countDown(LONG_BREAK_MIN * 60)
        label.config(fg=PINK, text="Break")
    elif reps % 2 == 1:
        countDown(WORK_MIN * 60)
        label.config(fg=GREEN, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    global timer
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
        timer = window.after(1000, countDown, count - 1)
    else:
        startTimer()
        marks = ""
        workSessions = floor(reps / 2)
        for _ in range(workSessions):
            marks += "✓"
        checkMarks.config(text=marks)


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

resetButton = Button(text="reset", command=reset)
resetButton.grid(column=2, row=2)

checkMarks = Label(text="✓", fg=GREEN, bg=YELLOW)
checkMarks.grid(columns=3, row=3)

window.mainloop()
