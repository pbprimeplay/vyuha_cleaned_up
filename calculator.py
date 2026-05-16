import sys
import os

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
        # CTO wanted scientific stuff back on CLI, so here is exponents!
        # Using the double asterisk operator like a pro
        return val1 ** val2

if __name__ == "__main__":
    # Back to the CLI args so the automated pipeline stops throwing 500 errors
    try:
        if len(sys.argv) < 4:
            print("Error: give me more stuff")
            sys.exit(1)
            
        operation = sys.argv[1]
        num1 = sys.argv[2]
        num2 = sys.argv[3]
        
        print("RESULT IS:")
        print(calc(operation, num1, num2))
        
    except Exception as e:
        print("Something went wrong. Try passing better numbers next time.")