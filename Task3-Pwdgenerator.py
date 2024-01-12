import tkinter as tk
from tkinter import StringVar
import random
import string
import pyperclip  # For copying to clipboard

def generate_password():
    password_length = int(length_var.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    result_var.set(password)

def copy_to_clipboard():
    pyperclip.copy(result_var.get())

# Create the main window
window = tk.Tk()
window.title("Password Generator")


# Styling
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg='#3498db')  # Set background color

# Create and place widgets in the window
title_label = tk.Label(window, text="Password Generator", font=("Helvetica", 20), bg='#3498db', fg='#ffffff')
title_label.pack(pady=10)

length_label = tk.Label(window, text="Password Length:", font=("Helvetica", 12), bg='#3498db', fg='#ffffff')
length_label.pack(pady=5)

length_var = StringVar()
length_entry = tk.Entry(window, textvariable=length_var, font=("Helvetica", 12))
length_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password, font=("Helvetica", 12), bg='#2ecc71', fg='#ffffff')
generate_button.pack(pady=10)

result_var = StringVar()
result_entry = tk.Entry(window, textvariable=result_var, font=("Helvetica", 12), state='readonly')
result_entry.pack(pady=10)

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, font=("Helvetica", 12), bg='#e74c3c', fg='#ffffff')
copy_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
