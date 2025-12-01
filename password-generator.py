import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Length must be at least 4")
            return
        
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        status_label.config(text="New password generated!", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        status_label.config(text="Copied to clipboard!", fg="blue")
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first")

#Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x280")
root.resizable(False, False)

#Title 
title_label = tk.Label(root, text="Secure Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

#Length input
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 10))
length_entry.pack(pady=5)
length_entry.insert(0, "12")

#Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
generate_btn = tk.Button(button_frame, text="Generate", command=generate_password,
                         bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=12)
generate_btn.pack(side=tk.LEFT, padx=10)

copy_btn = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard,
                     bg="#2196F3", fg="white", font=("Arial", 12, "bold"), width=15)
copy_btn.pack(side=tk.LEFT, padx=10)

#password display
tk.Label(root, text="Generated Password:", font=("Arial", 10)).pack(pady=(20,5))
password_entry = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
password_entry.pack(pady=5)

#Status label
status_label = tk.Label(root, text="Click Generate for new password", font=("Arial", 9), fg="gray")
status_label.pack(pady=5)

root.mainloop()
