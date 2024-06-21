# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.


# def print_hi(name):
#     print(f'Hi, {name}')


# if __name__ == '__main__':
#     print_hi(' this is in vs code')


# =======================

#from curses import window
#import tkinter as tk
#import subprocess

#def open_page1():
 #   subprocess.Popen(["python", "page1.py"])

# Create the main window
#window = tk.Tk()
#framefull= tk.Tk()
#framefull.title("Main Page")
#changed background color of frame
#framefull.configure(bg="lightgreen")

#insert Sub frame 1
#frame1= tk.Tk()
#frame1.configure(bg="red")
#frame1.size(padx=200,pady=200)


#insert Sub frame 1
#frame2= tk.Tk()
#frame2.configure(bg="lightblue")
#frame2.size(padx=20,pady=20)

# Create a button to open Page 1
#page1_button = tk.Button(framefull, text="Go to Page 1", command=open_page1)
#page1_button.pack(pady=300)
#page1_button.pack(padx=300,pady=300)


# Run the main loop
#framefull.mainloop()

#===================

#from ctypes.wintypes import SIZE
#from re import X
#import tkinter as tk
#import subprocess

#def open_page1():
 #   subprocess.Popen(["python", "page1.py"])

# Create the main window
#window = tk.Tk()
#window.title("Main Page")
#window.configure(bg="lightblue")  # Change background color of the main window

# Create the main frame
#main_frame = tk.Frame(window, bg="red")
#main_frame.pack(fill="both", expand=True, padx=300, pady=300)


# Create the first sub-frame
#frame1 = tk.Frame(main_frame, bg="white", bd=5, relief="sunken")
#frame1.pack(side="left", fill="both", expand=True, padx=0, pady=5)


# Add a label to the first sub-frame
#label1 = tk.Label(frame1, text="Frame 1", bg="white")
#label1.pack(pady=15,padx=15)

# Create the second sub-frame
#frame2 = tk.Frame(main_frame, bg="white", bd=2, relief="sunken")
#frame2.pack(side="right", fill="both", expand=True, padx=90, pady=90)

# Add a label to the second sub-frame
#label2 = tk.Label(frame2, text="Frame 2", bg="white")
#label2.pack(pady=5)

# Create a button to open Page 1 in the first sub-frame
#page1_button = tk.Button(frame1, text="Go to Page 1", command=open_page1)
#page1_button.pack(padx=20, pady=20)

# Run the main loop
#window.mainloop()

#================
import tkinter as tk
import subprocess

def open_page1():
    subprocess.Popen(["python", "page1.py"])

# Create the main window
window = tk.Tk()
window.title("Main Page")
window.configure(bg="lightblue")  # Change background color of the main window
#window.geometry("1000x1000")  # Set window size to 450x450
window.geometry("1200x1200")
# Create the main frame
main_frame = tk.Frame(window, bg="red", width='1180px', height='1180px')
main_frame.pack(fill="both", expand=True, padx=2, pady=2)
main_frame.pack_propagate(False)  # Prevent the main frame from adjusting its size

# Create the first sub-frame
frame1 = tk.Frame(main_frame, bg="orange", bd=2, relief="sunken")
frame1.pack(side="left", padx=(0, 1), pady=2)
frame1.pack_propagate(False)  # Prevent the frame1 from adjusting its size
frame1.configure(width='600px', height='600px')

# Add a label to the first sub-frame
label1 = tk.Label(frame1, text="Frame 1", bg="white")
label1.pack(pady=5)

# Create the second sub-frame
frame2 = tk.Frame(main_frame, bg="green", bd=2, relief="sunken")
frame2.pack(side="left", padx=(1, 0), pady=2)
frame2.pack_propagate(False)  # Prevent the frame2 from adjusting its size
frame2.configure(width='300px', height='300px')

# Add a label to the second sub-frame
label2 = tk.Label(frame2, text="Frame 2", bg="white")
label2.pack(pady=5)

# Create a button to open Page 1 in the first sub-frame
page1_button = tk.Button(frame1, text="Go to Page 1", command=open_page1)
page1_button.pack(padx=20, pady=20)

# Run the main loop
window.mainloop()