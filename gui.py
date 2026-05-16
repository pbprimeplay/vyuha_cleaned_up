import tkinter as tk
import sys
import os
# PROPER ARCHITECTURE: Importing the backend module directly!
import calculator 

def run_calculation():
    op = op_entry.get().strip()
    n1 = num1_entry.get().strip()
    n2 = num2_entry.get().strip()
    
    try:
        # Calling the function directly in-memory smoothly
        res = calculator.calc(op, n1, n2)
        result_label.config(text=f"Result: {res}", fg="green")
    except Exception as e:
        # Catching conversion errors (like if they type letters)
        result_label.config(text="Error: Invalid Input or Operation", fg="red")

root = tk.Tk()
root.title("Ultra Calc GUI V2 - Production Ready")

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

result_label = tk.Label(root, text="System Ready", fg="blue")
result_label.pack()

root.mainloop()