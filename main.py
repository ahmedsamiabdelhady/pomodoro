from tkinter import *
import math
import winsound
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
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps= 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER", fg=GREEN)
    check_label.config(text= " ")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    #Make a Beeb sound before each session.
    freq = 440 # Hz
    if reps in [1, 3, 5, 7]:
        duration = math.floor(WORK_MIN * 60)
        winsound.Beep(freq, duration)
    elif reps == 8:
        duration = math.floor(LONG_BREAK_MIN * 60)
        winsound.Beep(freq, duration)
    elif reps in [2, 4, 6]:
        duration = math.floor(SHORT_BREAK_MIN * 60)
        winsound.Beep(freq, duration)
    #countdown for each session.
    reps += 1
    work_sec= WORK_MIN * 60
    long_break_sec= LONG_BREAK_MIN * 60
    short_break_sec= SHORT_BREAK_MIN * 60
    if reps in [1, 3, 5, 7]:
        title_label.config(text= "WORK", fg= RED)
        count_down(work_sec)
    elif reps == 8:
        title_label.config(text= "BREAK", fg= GREEN)
        count_down(long_break_sec)
    elif reps in [2, 4, 6]:
        title_label.config(text= "BREAK", fg= PINK)
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(n):
    count_min = math.floor(n / 60)
    count_sec = n % 60
    if count_sec < 10:
        count_sec= f"0{count_sec}"
    if count_min < 10:
        count_min= f"0{count_min}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if n > 0:
        global timer
        timer = window.after(1000, count_down, n-1)
    else:
        start_timer()
        check = " "
        work_sessions= math.floor(reps/2)
        for _ in range(work_sessions):
            check += "✔"
        check_label.config(text= check)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady=50, bg= YELLOW)
canvas = Canvas(width=300, height=300, highlightthickness=0, bg=YELLOW)
brain_img = PhotoImage(file="brain.png")
canvas.create_image(150, 120, image=brain_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(146, 250, text="00:00", fill=PINK, font=(FONT_NAME, 45, "bold"))
canvas.grid(column=1, row=1)

title_label= Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)

check_label= Label(text=" ", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 13, "normal"))
check_label.grid(column=1, row=3)

reset = PhotoImage(file="stop-button.png")
reset_button= Button(highlightthickness=0, bg= YELLOW, bd=0, image=reset, command= reset_timer)
reset_button.grid(column=2, row=2)

start = PhotoImage(file= "play-button.png")
start_button= Button(highlightthickness=0, bg= YELLOW, bd=0, image=start, command=start_timer)
start_button.grid(column=0, row=2)





window.mainloop()