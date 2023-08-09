import customtkinter

# Window Properties
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("300x300")
root.title("Eye Saver")

# Variable Initialization
default_timer_time = 1200  # Represents the total time in seconds that the timer will start from | Default is 1200
timer_time = default_timer_time
seconds = timer_time % 60
minutes = int(timer_time / 60) % 60
run_timer = False
start_button_toggle = True
timer_started = False
green_fg_hex = "#2fa572"
green_hover_hex = "#106a43"
red_fg_hex = "#B22222"
red_hover_hex = "#990000"


def start_button():
    global start_button_toggle, run_timer, timer_started
    if start_button_toggle:
        if not timer_started:
            timer_started = True
            start_timer()
        start_button.configure(fg_color=red_fg_hex, text="Pause", hover_color=red_hover_hex)
        run_timer = True
        start_button_toggle = False
    else:
        start_button.configure(fg_color=green_fg_hex, text="Start", hover_color=green_hover_hex)
        run_timer = False
        start_button_toggle = True


def update_timer_label():
    global seconds, minutes
    seconds = timer_time % 60
    minutes = int(timer_time / 60) % 60
    timer_label.configure(text=f"{minutes:02}:{seconds:02}")
    timer_label.configure(text_color="white")
    timer_label.pack()


def start_timer():  # Will start and continue the timer until the timer runs out
    global seconds, minutes, timer_time, run_timer
    if run_timer:
        timer_time = timer_time - 1
        update_timer_label()
        if timer_time < 1:
            run_timer = False
            end_timer()
    root.after(1000, start_timer)


def end_timer():
    timer_label.configure(text_color="red")
    show_custom_popup(on_popup_close)


def show_custom_popup(callback_func):
    custom_popup = customtkinter.CTkToplevel(root)
    custom_popup.title("")
    label = customtkinter.CTkLabel(custom_popup, text="Take A 20 Second Break Looking At Something 20 Feet Away")
    label.pack(padx=20, pady=10)
    close_button = customtkinter.CTkButton(custom_popup, text="Done", command=lambda: close_custom_popup(custom_popup, callback_func), font=("TkDefaultFont", 14, 'bold'))
    close_button.pack(pady=10)


def close_custom_popup(popup, callback_func):
    popup.destroy()
    if callback_func:
        callback_func()


def on_popup_close():
    global timer_time, start_button_toggle
    timer_time = default_timer_time
    update_timer_label()
    start_button_toggle = True
    start_button.configure(fg_color=green_fg_hex, text="Start", hover_color=green_hover_hex)


# UI Elements
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=30, padx=30, fill="both", expand=True)
main_label = customtkinter.CTkLabel(master=frame, pady=30, text="Eye Saver", font=("TkDefaultFont", 24, 'bold'))
main_label.pack()
timer_label = customtkinter.CTkLabel(master=frame, text=f"{minutes:02}:{seconds:02}", font=("TkDefaultFont", 24))
timer_label.pack(pady=10, padx=10)
start_button = customtkinter.CTkButton(master=frame, command=start_button, text="Start", font=("TkDefaultFont", 16, 'bold'))
start_button.pack(pady=20, padx=10)

root.mainloop()
