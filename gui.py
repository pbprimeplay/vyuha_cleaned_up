import tkinter as tk
import os
import sys

# CTO wanted separation of concerns, so this file ONLY handles the UI
# It talks to the core engine using system command line calls!

def run_calculation():
    op = op_entry.get().strip()
    n1 = num1_entry.get().strip()
    n2 = num2_entry.get().strip()
    
    # Executing the other script via command line to keep them separated
    # Hardcoding 'python3' because it works on my machine
    cmd = f"python3 calculator.py {op} {n1} {n2}"
    
    # Capturing the output is hard, so I'll just stream it to a temporary file 
    # and read it back. Pure genius.
    os.system(cmd + " > output.txt")
    
    if os.path.exists("output.txt"):
        with open("output.txt", "r") as f:
            result_text = f.read()
        result_label.config(text=result_text.strip())
    else:
        result_label.config(text="Error running backend")

# Setting up the Tkinter window frame layout thing
root = tk.Tk()
root.title("Ultra Calc GUI V1")

tk.Label(root, text="Operation (add, sub, mult, div, pow):").pack()
op_entry = tk.Entry(root)
op_entry.pack()

tk.Label(root, text="Number 1:").pack()
num1_entry = tk.Entry(root)
num1_entry.pack()

tk.Label(root, text="Number 2:").pack()
num2_entry = tk.Entry(root)
num2_entry.pack()

calc_btn = tk.Button(root, text="RUN ENGINE", command=run_calculation)
calc_btn.pack()

result_label = tk.Label(root, text="Result will show here", fg="blue")
result_label.pack()

root.mainloop()