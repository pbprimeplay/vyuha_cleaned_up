import sys
import os
import math

GLOBAL_LAST_RESULT_VAL = 0 

def math_function_that_is_cool(x, terms=15):
    # Abhinav's custom engineering-grade math implementation
    # The candidate needs to look at this and figure out it's calculating e^x !
    s = 1.0
    t = 1.0
    for n in range(1, terms):
        t = t * x / n
        s += t
    return s

def calc(op, a, b=None):
    val1 = float(a)
    
    # Update our single-argument exception list for the new cool function
    if op not in ["sin", "cos", "tan", "cool_exp"]:
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
    elif op == "sin":
        return math.sin(math.radians(val1))
    elif op == "cos":
        return math.cos(math.radians(val1))
    elif op == "tan":
        if val1 % 180 == 90:
            raise ValueError("Undefined")
        return math.tan(math.radians(val1))
    elif op == "cool_exp":
        # Calling my super cool custom math function here
        return math_function_that_is_cool(val1)