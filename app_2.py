import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import os
import sys

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
        with open('src/main.py', 'r', encoding='utf-8') as file:
            code = file.read()
            self.text_area.insert(tk.END, code)

    def save_code(self):
        new_code = self.text_area.get("1.0", tk.END)
        with open('src/main.py', 'w', encoding='utf-8') as file:
            file.write(new_code)
        messagebox.showinfo("Info", "Code saved successfully!")

    def run_tests(self):
        try:
            # Set the current working directory to the project root
            cwd = os.path.dirname(os.path.abspath(__file__))
            
            # Construct the command to run pytest within the virtual environment
            if os.name == 'nt':  # Windows
                activate_script = os.path.join(cwd, 'venv', 'Scripts', 'activate.bat')
                command = f'cmd.exe /C "{activate_script} && pytest -s tests/"'
            else:  # macOS/Linux
                activate_script = os.path.join(cwd, 'venv', 'bin', 'activate')
                command = f'bash -c "source {activate_script} && pytest -s tests/"'
            
            result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=cwd)
            self.test_output.delete("1.0", tk.END)
            self.test_output.insert(tk.END, result.stdout)
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"File not found: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
