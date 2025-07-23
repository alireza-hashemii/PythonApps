import os
import tkinter as tk
from tkinter import messagebox

def count_python_files(directory):
    """Count the number of Python files in the specified directory."""
    count = 0
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    count += 1
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return 0
    return count

def search_files():
    """Get the directory from the entry and count Python files."""
    directory = entry.get()
    if not directory:
        messagebox.showwarning("Input Error", "Please enter a directory path.")
        return

    if not os.path.isdir(directory):
        messagebox.showwarning("Input Error", "The entered path is not a valid directory.")
        return

    count = count_python_files(directory)
    messagebox.showinfo("Result", f"Number of Python files: {count}")

# Set up the main window
root = tk.Tk()
root.title("Python File Counter")

# Create a label
label = tk.Label(root, text="Enter directory path:")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create a button to search
search_button = tk.Button(root, text="Count Python Files", command=search_files)
search_button.pack(pady=20)

# Start the main event loop
root.mainloop()