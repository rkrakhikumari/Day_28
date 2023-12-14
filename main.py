from tkinter import *
import math
from PIL import Image, ImageTk

# Constants
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#03AC13'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Timer reset
def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# Timer mechanism
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work Time", fg=GREEN)

# Countdown
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# UI Setup
window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW)
window.geometry("300x300") # Adjust the size as needed

image = Image.open("tomato.jpg")
# image = image.resize((100, 100), Image.Resampling.LANCZOS)
tomato_img = ImageTk.PhotoImage(image)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)  # Adjust the position as needed
timer_text = canvas.create_text(100, 130, text="00:00", fill="#E97451", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", fg="#954535", font=(FONT_NAME, 50), bg=YELLOW)
label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
