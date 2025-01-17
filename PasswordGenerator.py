import tkinter as tk
from tkinter import ttk
import string
import random
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x450")
        
        # Variables
        self.password_length = tk.IntVar(value=12)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Length selection
        ttk.Label(main_frame, text="Password Length:").grid(row=0, column=0, sticky=tk.W)
        length_spinbox = ttk.Spinbox(main_frame, from_=4, to=50, textvariable=self.password_length, width=5)
        length_spinbox.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Character type checkboxes
        ttk.Checkbutton(main_frame, text="Uppercase Letters", variable=self.include_uppercase).grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Checkbutton(main_frame, text="Lowercase Letters", variable=self.include_lowercase).grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Checkbutton(main_frame, text="Numbers", variable=self.include_numbers).grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Checkbutton(main_frame, text="Special Characters", variable=self.include_symbols).grid(row=4, column=0, sticky=tk.W, pady=5)
        
        # Generated password display
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, width=40)
        password_entry.grid(row=5, column=0, columnspan=2, pady=20)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Generate Password", command=self.generate_password).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=0, column=1, padx=5)
        
    def generate_password(self):
        chars = ''
        if self.include_uppercase.get():
            chars += string.ascii_uppercase
        if self.include_lowercase.get():
            chars += string.ascii_lowercase
        if self.include_numbers.get():
            chars += string.digits
        if self.include_symbols.get():
            chars += string.punctuation
            
        if not chars:
            self.password_var.set("Please select at least one character type")
            return
            
        password = ''.join(random.choice(chars) for _ in range(self.password_length.get()))
        self.password_var.set(password)
        
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password and password != "Please select at least one character type":
            pyperclip.copy(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()