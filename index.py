import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import shutil
from den3 import calculate_image_density, GUI

root = tk.Tk()
root.geometry('800x800') 
root.title('Detect Images')

home_content = None

def homepage():
    global home_content  # Use the global variable to store the "Home" tab content

    # Clear the main_frame before showing the content of the "Home" page
    for widget in main_frame.winfo_children():
        widget.destroy()

    #"Home" tab
    desc_text = "Welcome to the Endoscopic Image Detection Application."
    desc_label = tk.Label(main_frame, text=desc_text, font=('Arial', 20))
    desc_label.pack(pady=20)

    desc_text = "This application helps you find the infected part in endoscopic images."
    desc_label = tk.Label(main_frame, text=desc_text, font=('Arial', 14))
    desc_label.pack()

    #"Check" option
    desc_text = "Click on the 'Check' button to get started."
    desc_label = tk.Label(main_frame, text=desc_text, font=('Arial', 14))
    desc_label.pack(pady=10)
    check_link = tk.Label(main_frame, text='Check >>', font=('Bold', 15), fg='#158aff', cursor='hand2')
    check_link.pack(pady=10)
    check_link.bind("<Button-1>", lambda event: indicate(check_indicate, check))

    # Store the content of the "Home" page in the global variable
    home_content = main_frame.winfo_children()

def confirm_exit():
    response = messagebox.askyesno("Warning", "Do you want to close the application?")
    if response:
        root.destroy() 

def check():
    for widget in main_frame.winfo_children():
        widget.destroy()

    root_den = tk.Toplevel()
    root_den.transient(root)
    root_den.attributes("-topmost", False)
    den_gui = GUI(root_den)

    root_den.protocol("WM_DELETE_WINDOW", lambda: on_child_window_close(root_den))

def on_child_window_close(child_window):
    child_window.destroy()
    homepage()

def hide_indicate():
    home_indicate.config(bg='#c3c3c3')
    check_indicate.config(bg='#c3c3c3')

def indicate(lb, page=None):
    hide_indicate()
    lb.config(bg='#158aff')
    if page:
        page()

options_frame = tk.Frame(root, bg='#c3c3c3')

home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(home_indicate, homepage))
home_btn.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.grid(row=0, column=1, pady=10, sticky=tk.W)

check_btn = tk.Button(options_frame, text='Check', font=('Bold', 15),
                      fg='#158aff', bd=0, bg='#c3c3c3',
                      command=lambda: indicate(check_indicate, check))
check_btn.grid(row=1, column=0, pady=10, padx=10, sticky=tk.W)
check_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
check_indicate.grid(row=1, column=1, pady=10, sticky=tk.W)

options_frame.grid(row=0, column=0, sticky=tk.N)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2, bg='white')
main_frame.grid(row=0, column=1, sticky=tk.NSEW)

root.grid_rowconfigure(0, weight=1)  # Allow the main frame to expand vertically
root.grid_columnconfigure(1, weight=1)  # Allow the main frame to expand horizontally

# Update the window title based on resizing
def update_window_title(event):
    width = event.width
    height = event.height
    root.title(f'Detect Images - {width}x{height}')

root.bind('<Configure>', update_window_title)

homepage() 
indicate(home_indicate)  

submit_btn = tk.Button(main_frame, text='Submit', font=('Bold', 15),
                       fg='white', bg='red', command=confirm_exit)
submit_btn.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.SE)

root.mainloop()
