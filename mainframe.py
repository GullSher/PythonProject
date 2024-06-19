import tkinter as tk

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    message = message_entry.get()
    
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    
    # You can add your own logic here to process the form data

# Create the main window
window = tk.Tk()
window.title("Form")

# Create the name label and entry field
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create the email label and entry field
email_label = tk.Label(window, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(window)
email_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the message label and text area
message_label = tk.Label(window, text="Message:")
message_label.grid(row=2, column=0, padx=10, pady=10)
message_entry = tk.Text(window, height=5)
message_entry.grid(row=2, column=1, padx=10, pady=10)

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
window.mainloop()