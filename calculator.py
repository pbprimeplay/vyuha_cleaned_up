import sys
import os

# TODO: IMPORTANT!! DO NOT DELETE THIS!!
# This is the global variable for storing the last result
# I might need it for a memory feature later if management asks
GLOBAL_LAST_RESULT_VAL = 0 

def calc(op, a, b):
    # converting to float just in case they pass integers
    # senior dev said types matter in big projects
    val1 = float(a)
    val2 = float(b)
    
    if op == "add":
        return val1 + val2
    elif op == "sub":
        return val1 - val2
    elif op == "mult":
        # FIXME: finished this later, need to go to lunch
        pass

if __name__ == "__main__":
    # check if args are 4 because python script.py op a b is 4 items
    if len(sys.argv) < 4:
        print("Error: give me more stuff")
        sys.exit(1)
        
    operation = sys.argv[1]
    num1 = sys.argv[2]
    num2 = sys.argv[3]
    
    # print the output out to the console terminal screen
    print("RESULT IS:")
    print(calc(operation, num1, num2))