import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Diary")
        self.root.geometry("600x400")

        # Create the text area for writing entries
        self.text_area = tk.Text(self.root, wrap="word", font=("Arial", 14), padx=10, pady=10)
        self.text_area.pack(expand=True, fill="both")

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create a file menu for Save, Open, and Exit
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save", command=self.save_entry)
        self.file_menu.add_command(label="Open", command=self.open_entry)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Create a button to clear the text area
        self.clear_button = tk.Button(self.root, text="Clear", font=("Arial", 12), command=self.clear_entry)
        self.clear_button.pack(side="bottom", pady=10)

    def save_entry(self):
        """Save the diary entry to a text file."""
        diary_entry = self.text_area.get("1.0", tk.END).strip()
        if not diary_entry:
            messagebox.showwarning("Empty Entry", "You must write something before saving!")
            return

        # Prompt user to choose a file to save
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(diary_entry)
                messagebox.showinfo("Success", "Your diary entry has been saved.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

    def open_entry(self):
        """Open an existing diary entry from a text file."""
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.text_area.delete("1.0", tk.END)  # Clear any existing content
                    self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while opening the file: {e}")

    def clear_entry(self):
        """Clear the text area."""
        self.text_area.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()

# Initialize the DiaryApp class
app = DiaryApp(root)

# Run the tkinter main loop
root.mainloop()
