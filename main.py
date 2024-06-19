# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.


# def print_hi(name):
#     print(f'Hi, {name}')


# if __name__ == '__main__':
#     print_hi(' this is not in Netbeans')


# =======================

import tkinter as tk
import subprocess

def open_page1():
    subprocess.Popen(["python", "page1.py"])

# Create the main window
window = tk.Tk()
window.title("Main Page")

# Create a button to open Page 1
page1_button = tk.Button(window, text="Go to Page 1", command=open_page1)
#page1_button.pack(pady=300)
page1_button.pack(padx=300,pady=300)

# Run the main loop
window.mainloop()