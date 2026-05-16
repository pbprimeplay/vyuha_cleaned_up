import sys
import os

# PURE MATH LIBRARY MODE: No more command line argument junk!
GLOBAL_LAST_RESULT_VAL = 0 

def calc(op, a, b):
    val1 = float(a)
    val2 = float(b)
    
    if op == "add":
        return val1 + val2
    elif op == "sub":
        return val1 - val2
    elif op == "mult":
        return val1 * val2
    elif op == "div":
        return val1 / val2
    elif op == "pow":
        return val1 ** val2

if __name__ == "__main__":
    # If someone accidentally runs the backend directly, just guide them
    print("Ultra Calc Core Engine loaded successfully.")
    print("Please run 'gui.py' to use the application interface.")