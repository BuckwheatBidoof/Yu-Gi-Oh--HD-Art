import customtkinter as ctk
from tkinter import filedialog
import api

#*================================================================

def directory_event():
    global path
    path = filedialog.askdirectory()
    if path != "" and len(path) > 32:
        temp = path[:32] + "..."
    else:
        temp = path
    textbox.configure(state="normal")
    textbox.delete("0.0", "end")
    textbox.insert("0.0", temp)
    textbox.configure(state="disabled")
    download_button.configure(state="normal")

def download_cards(download_all_cards):
    download_button.configure(state="disabled")
    if not download_all_cards:
        api.download(path, False)
    else:
        api.download(path, True)
    download_button.configure(state="normal")

#*================================================================

global path
path = ""

#window
window = ctk.CTk()
window.title("EDOPro HD Image Downloader")
window.geometry("400x300")
window.iconbitmap("ygo.ico")
window.resizable(False, False)
ctk.deactivate_automatic_dpi_awareness()
ctk.set_window_scaling(1.3)
ctk.set_widget_scaling(1.25)

#widgets
label = ctk.CTkLabel(
    window, 
    text="Yu-Gi-Oh! EDOPro\nHD Image Downloader", 
    font=("Terminal", 25),
    padx=10,
    pady=10)
label.pack(expand=True)

instructions = ctk.CTkLabel(
    window, 
    text="Select EDOPro Root Folder", 
    font=("Terminal", 15),
    padx=10,
    pady=10)
instructions.pack(expand=True)

#directory path
textbox = ctk.CTkTextbox(
    window, 
    state="disabled", 
    corner_radius=10,
    width=250,
    height=10,
    padx=5,
    pady=5)
textbox.pack(expand=True)

folder_button = ctk.CTkButton(
    window, 
    text="Select Folder", 
    command=directory_event,
    font=("Terminal", 14))
folder_button.pack(padx=5, pady=5, expand=True)

check_var = ctk.BooleanVar(value=False)
checkbox = ctk.CTkCheckBox(
    window, 
    text="Include Rush Duel/Speed Duel Skill Cards", 
    font=("Terminal", 15),
    variable=check_var, 
    onvalue=True, 
    offvalue=False)
checkbox.pack(padx=5,pady=5, expand=True)

download_button = ctk.CTkButton(
    window, 
    text="Download", 
    command=lambda:download_cards(check_var.get()),
    font=("Terminal", 14),
    state="disabled")
download_button.pack(padx=5, pady=5, expand=True)

notice = ctk.CTkLabel(
    window,
    text="*Including Rush Duel will make\n"
    "some of those downloaded cards in the original\n"
    "language in the OCG, so that's Japanese. Do NOT enable\n"
    "if you don't want this.",
    font=("Terminal", 12))
notice.pack(padx=5, pady=5, expand=True)

#run
window.mainloop()