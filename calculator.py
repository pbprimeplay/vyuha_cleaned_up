import sys
import os

GLOBAL_LAST_RESULT_VAL = 0 

def calc(op, a, b):
    # If they want to use the last answer, we check for 'ans'
    # Keeping it global so it persists
    global GLOBAL_LAST_RESULT_VAL
    
    # Quick fix: if they typed 'ans', use the global stored value
    if a == "ans":
        val1 = float(GLOBAL_LAST_RESULT_VAL)
    else:
        val1 = float(a)
        
    if b == "ans":
        val2 = float(GLOBAL_LAST_RESULT_VAL)
    else:
        val2 = float(b)
    
    if op == "add":
        GLOBAL_LAST_RESULT_VAL = val1 + val2
        return GLOBAL_LAST_RESULT_VAL
    elif op == "sub":
        GLOBAL_LAST_RESULT_VAL = val1 - val2
        return GLOBAL_LAST_RESULT_VAL
    elif op == "mult":
        GLOBAL_LAST_RESULT_VAL = val1 * val2
        return GLOBAL_LAST_RESULT_VAL
    elif op == "div":
        GLOBAL_LAST_RESULT_VAL = val1 / val2
        return GLOBAL_LAST_RESULT_VAL

if __name__ == "__main__":
    print("--- ULTRA CALC V2: TEXT INTERFACE MODE ---")
    print("Type 'exit' to quit")
    
    while True:
        try:
            operation = input("Enter operation (add, sub, mult, div): ").strip()
            if operation == "exit":
                break
                
            num1 = input("Enter first number (or 'ans'): ").strip()
            num2 = input("Enter second number (or 'ans'): ").strip()
            
            res = calc(operation, num1, num2)
            print(f"--> RESULT: {res}\n")
            
        except Exception as e:
            # Still swallowing errors so the loop never crashes!
            print("Something went wrong. Bad input? Let's try again.\n")