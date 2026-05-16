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
        # added multiplication, very straightforward
        return val1 * val2
    elif op == "div":
        # added division, looks good to go
        return val1 / val2

if __name__ == "__main__":
    # Wrap everything so the user never sees a scary python traceback crash trace
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
        # If anything goes wrong anywhere, just say this. 
        # Clean UI!
        print("Something went wrong. Try passing better numbers next time.")