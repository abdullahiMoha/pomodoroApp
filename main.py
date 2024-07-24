from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# FONT = (FONT_NAME, 35, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text = "00:00")
	lbl_header.config(text = "Timer")
	lbl_check.config(text = "")
	global reps
	reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
	global reps
	reps += 1
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60

	if reps % 8 == 0:  # or reps / 5 == 1 or reps / 5 == 2 or reps / 5 == 3:
		lbl_header.config(text = "Break", fg = RED)
		count_down(long_break_sec)
	elif reps % 2 == 0:
		lbl_header.config(text = "Break", fg = PINK)
		count_down(short_break_sec)
	else:
		lbl_header.config(text = "Work", fg = GREEN)
		count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
	count_min = math.floor(count / 60)
	count_sec = math.floor(count % 60)

	# Correcting the format
	if count_sec < 10:
		count_sec = f"0{count_sec}"
	if count_min < 10:
		count_min = f"0{count_min}"

	canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
	# Looping through timer function
	if count > 0:
		global timer
		timer = window.after(1000, count_down, count - 1)
	else:
		start_timer()
		mark = ""
		work_sessions = math.floor(reps / 2)
		for _ in range(work_sessions):
			mark += "✔"
		lbl_check.config(text = mark)


# ---------------------------- UI SETUP ------------------------------- #

# creating the main window
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

# making the screen canvas as tomato image background and other UI elements

lbl_header = Label(text = "Timer", font = (FONT_NAME, 35, "bold"), fg = GREEN, bg = YELLOW)  # header label
lbl_header.grid(row = 0, column = 1)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_bg = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_bg)
timer_text = canvas.create_text(110, 130, text = "00:00", font = (FONT_NAME, 30, "bold"), fill = "white")  # timer label
canvas.grid(row = 1, column = 1)

# count_down(5)

btn_start = Button(text = "Start", bg = "white", highlightthickness = 0, bd = 0,
				   command = start_timer)  # button on the left side
btn_start.grid(row = 2, column = 0)

btn_reset = Button(text = "Reset", bg = "white", highlightthickness = 0, bd = 0,
				   command = reset_timer)  # button on the right side
btn_reset.grid(row = 2, column = 2)

lbl_check = Label(font = (FONT_NAME, 10, "normal"), fg = GREEN, bg = YELLOW)  # label for ticks
lbl_check.grid(row = 3, column = 1)

window.mainloop()  # ⚠️ DO NOT DELETE THIS LINE
