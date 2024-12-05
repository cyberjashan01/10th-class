import tkinter as tk
from time import strftime, time
from tkinter import font

root = tk.Tk()
root.title("Clock and Timer")
root.geometry("500x300")
root.configure(bg='#e0f7fa')  

start_time = None
running = False
timer_label_text = tk.StringVar()

header_font = font.Font(family="Helvetica", size=24, weight="bold")
timer_font = font.Font(family="Helvetica", size=36, weight="bold")
button_font = font.Font(family="Helvetica", size=12, weight="bold")

def update_time():
    time_string = strftime('%d-%m-%y %A %H:%M:%S %p')
    time_label.config(text=time_string)
    time_label.after(1000, update_time)  

def update_timer():
    if running:
        elapsed_time = time() - start_time
        hours, remainder = divmod(int(elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        timer_label_text.set(f"{hours:02}:{minutes:02}:{seconds:02}")
        root.after(1000, update_timer)  

def start_timer():
    global start_time, running
    if not running:
        start_time = time()
        running = True
        update_timer()

def stop_timer():
    global running
    running = False

def reset_timer():
    global start_time, running
    start_time = None
    running = False
    timer_label_text.set("00:00:00")

time_label = tk.Label(root, font=header_font, background='#e0f7fa', foreground='#00796b')
time_label.pack(pady=20)

timer_label = tk.Label(root, font=timer_font, background='#e0f7fa', foreground='#d32f2f', textvariable=timer_label_text)
timer_label.pack(pady=20)

button_frame = tk.Frame(root, bg='#e0f7fa')
button_frame.pack(pady=10)

def create_button(frame, text, command, bg_color, fg_color):
    button = tk.Button(frame, text=text, command=command, font=button_font, bg=bg_color, fg=fg_color,
                       relief='flat', borderwidth=2, padx=10, pady=5, bd=1)
    button.pack(side=tk.LEFT, padx=10)
    return button

start_button = create_button(button_frame, "Start Timer", start_timer, '#388e3c', 'white')
stop_button = create_button(button_frame, "Stop Timer", stop_timer, '#d32f2f', 'white')
reset_button = create_button(button_frame, "Reset Timer", reset_timer, '#1976d2', 'white')

update_time()
root.mainloop()