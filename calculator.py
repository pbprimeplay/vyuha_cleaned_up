import sys
import os
import math # Imported math module for advanced operations

GLOBAL_LAST_RESULT_VAL = 0 

def calc(op, a, b=None): # Made 'b' optional with None because trig functions only need one number!
    val1 = float(a)
    
    # Only try to parse 'b' if it's actually needed for binary operations
    if op not in ["sin", "cos", "tan"]:
        if b is None:
            raise ValueError("This operation requires two numbers.")
        val2 = float(b)
    
    if op == "add":
        return val1 + val2
    elif op == "sub":
        return val1 - val2
    elif op == "mult":
        return val1 * val2
    elif op == "div":
        return val1 / val2
    # NOTE: 'pow' feature is missing on this branch! It only exists on feature/back-to-cli!
    
    # NEW SCIENTIFIC FEATURES ADDED PER CTO ORDERS
    elif op == "sin":
        return math.sin(math.radians(val1)) # Converts degrees to radians smoothly
    elif op == "cos":
        return math.cos(math.radians(val1))
    elif op == "tan":
        if val1 % 180 == 90:
            raise ValueError("Undefined (Tangent of 90/270 degrees)")
        return math.tan(math.radians(val1))