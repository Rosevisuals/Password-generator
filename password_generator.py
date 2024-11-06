import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showwarning("Warning", "Password length should be at least 6 for security.")
            return
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
        all_characters = letters + digits + symbols
        password = ''.join(random.choice(all_characters) for _ in range(length))
        
        # Display the password in the entry field
        entry_password.config(state=tk.NORMAL)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
        entry_password.config(state='readonly')  # Make it read-only for easy copying
        
        # Copy password to clipboard
        root.clipboard_clear()
        root.clipboard_append(password)
        
        # Notify the user
        messagebox.showinfo("Copied", "Password generated and copied to clipboard!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg='#2c3e50')  # Background color for the window

# Font style
font_style = ("Helvetica", 12)

# Create and place widgets with improved styling
label_length = tk.Label(root, text="Password Length:", bg='#2c3e50', font=font_style)
label_length.pack(pady=10)

entry_length = tk.Entry(root, font=font_style)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password, bg='blue', fg='white', font=font_style)
button_generate.pack(pady=10)

label_password = tk.Label(root, text="Generated Password:", bg='#2c3e50', fg='white', font=font_style)
label_password.pack(pady=10)

entry_password = tk.Entry(root, width=30, font=font_style, state='readonly', readonlybackground='#34495e', fg='white')
entry_password.pack(pady=5)

root.mainloop()
