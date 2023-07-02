import random
import string
import tkinter as tk
from tkinter import ttk
import pyperclip

def generate_password(length, use_numbers, use_special_chars):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    length = length_var.get()
    use_numbers = numbers_var.get()
    use_special_chars = special_chars_var.get()
    password = generate_password(length, use_numbers, use_special_chars)
    result_label.configure(text=password)

def copy_password():
    password = result_label.cget("text")
    pyperclip.copy(password)

# Create GUI window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")

# Style for the GUI elements
style = ttk.Style()
style.configure("TButton", padding=6)
style.configure("TLabel", padding=6, font=("Arial", 12))
style.configure("TCheckbutton", font=("Arial", 12))

# Length label and entry
length_label = ttk.Label(window, text="Password Length:")
length_label.pack()
length_var = tk.IntVar()
length_entry = ttk.Entry(window, textvariable=length_var)
length_entry.pack()

# Checkboxes for options
numbers_var = tk.IntVar()
numbers_check = ttk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

special_chars_var = tk.IntVar()
special_chars_check = ttk.Checkbutton(window, text="Include Special Characters", variable=special_chars_var)
special_chars_check.pack()

# Generate button
generate_button = ttk.Button(window, text="Generate Password", command=generate)
generate_button.pack()

# Result label
result_label = ttk.Label(window, text="")
result_label.pack()

# Copy button
copy_button = ttk.Button(window, text="Copy Password", command=copy_password)
copy_button.pack()

# Run the GUI window
window.mainloop()
