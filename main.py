from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
REPS = 0
Timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global REPS, Timer
    REPS = 0
    window.after_cancel(Timer)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    heading.config(text="Timer", fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        heading.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        heading.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        heading.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global Timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    new_count = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=new_count)
    if count > 0:
        Timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
heading = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
heading.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_button = Button(text="Start", cursor="hand2", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", cursor="hand2", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)
check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
check_marks.grid(column=1, row=3)
window.resizable(False, False)
window.mainloop()
