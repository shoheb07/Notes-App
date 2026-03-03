import tkinter as tk
from tkinter import filedialog, messagebox

def new_note():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notes App")

def open_note():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        root.title(file_path + " - Notes App")
        text_area.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            text_area.insert(1.0, file.read())

def save_note():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(file_path + " - Notes App")
        messagebox.showinfo("Saved", "Note saved successfully!")

# Main Window
root = tk.Tk()
root.title("Notes App")
root.geometry("700x500")

# Text Area
text_area = tk.Text(root, font=("Arial", 14))
text_area.pack(fill=tk.BOTH, expand=True)

# Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_note)
file_menu.add_command(label="Open", command=open_note)
file_menu.add_command(label="Save", command=save_note)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
