from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#537D5D"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
DAILY_GOAL = 12 # 12 work sessions (which equals around 6 hours of focused work)
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # If t's the 8th rep:
        timer_label.config(text="20 min break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        # If it's 2nd/4th/6th rep:
        timer_label.config(text="5 min break", fg=PINK)
        count_down(short_break_sec)
    else:
        # If it's the 1st/3rd/5th/7th rep:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))

        # Recommended Daily Goal
        if work_sessions >= DAILY_GOAL:
            reset_timer()
            check_mark.config(
                text=f"{marks}\n🎯 Daily goal achieved!\nTime to rest – you’ve earned it!",
                fg=GREEN,
                bg=YELLOW,
                font=(FONT_NAME, 20, "bold")
            )

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", background=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)

start_btn = Button(text="Start", background="white", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", background="white", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="images/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
