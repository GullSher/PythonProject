import tkinter as tk
import subprocess

def open_mainframe():
    subprocess.Popen(["python", "mainframe.py"])

# Create the main window
window = tk.Tk()
window.title("Main Form")

# Create a button to open Page 1
page1_button = tk.Button(window, text="Go to Main Frame", command=open_mainframe)
page1_button.pack(padx=300,pady=300)

# Run the main loop
window.mainloop()