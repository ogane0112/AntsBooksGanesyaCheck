import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import os

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Editor and Test Runner")

        # Create text widget for main.py content
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=20)
        self.text_area.pack(pady=10)

        # Load the content of main.py
        self.load_code()

        # Create save button
        self.save_button = tk.Button(root, text="Save", command=self.save_code)
        self.save_button.pack(pady=5)

        # Create run tests button
        self.run_tests_button = tk.Button(root, text="Run Tests", command=self.run_tests)
        self.run_tests_button.pack(pady=5)

        # Create text widget for displaying test output
        self.test_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=20)
        self.test_output.pack(pady=10)

    def load_code(self):
        with open('src/main.py', 'r') as file:
            code = file.read()
            self.text_area.insert(tk.END, code)

    def save_code(self):
        new_code = self.text_area.get("1.0", tk.END)
        with open('src/main.py', 'w') as file:
            file.write(new_code)
        messagebox.showinfo("Info", "Code saved successfully!")

    def run_tests(self):
        result = subprocess.run(['pytest', '-s', 'tests/'], capture_output=True, text=True)
        self.test_output.delete("1.0", tk.END)
        self.test_output.insert(tk.END, result.stdout)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
