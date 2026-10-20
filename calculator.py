"""Core calculation engine for Nexus Calc.

Import it as a library (gui.py and interactive.py do this) or run it as a
command-line tool, which the automated integration tests depend on:

    python calculator.py <op> <a> [b]
"""
import sys
import math

BINARY_OPS = ["add", "sub", "mult", "div", "pow"]
# Single-input operations; any second operand passed to calc() is ignored.
UNARY_OPS = ["sin", "cos", "tan", "exp"]
OPERATIONS = BINARY_OPS + UNARY_OPS


def taylor_exp(x, tol=1e-15):
    """Return e**x by summing the Taylor series 1 + x + x^2/2! + x^3/3! + ...

    Terms are added until they no longer change the result. Negative inputs
    use e^x = 1 / e^-x, because the alternating series loses precision.
    """
    if x < 0:
        return 1.0 / taylor_exp(-x)
    s = 1.0
    t = 1.0
    n = 1
    while t > tol * s:
        t = t * x / n
        s += t
        n += 1
    return s


def calc(op, a, b=None):
    """Apply `op` to `a` (and `b` for binary ops) and return the result as a float.

    Operands may be numbers or numeric strings; trig angles are in degrees.
    Raises ValueError for unknown operations, bad operands and undefined
    results, and OverflowError if the result is too large.
    """
    if op not in OPERATIONS:
        raise ValueError(f"Unknown operation '{op}'. Choose from: {', '.join(OPERATIONS)}")

    val1 = float(a)
    if op in BINARY_OPS:
        if b is None or b == "":
            raise ValueError("This operation requires two numbers.")
        val2 = float(b)

    if op == "add":
        return val1 + val2
    elif op == "sub":
        return val1 - val2
    elif op == "mult":
        return val1 * val2
    elif op == "div":
        if val2 == 0:
            raise ValueError("Cannot divide by zero.")
        return val1 / val2
    elif op == "pow":
        # math.pow raises ValueError where ** would return a complex number, e.g. (-8) ** 0.5
        return math.pow(val1, val2)
    elif op == "sin":
        return math.sin(math.radians(val1))
    elif op == "cos":
        return math.cos(math.radians(val1))
    elif op == "tan":
        if val1 % 180 == 90:
            raise ValueError("tan is undefined at 90 degrees + k*180.")
        return math.tan(math.radians(val1))
    elif op == "exp":
        return taylor_exp(val1)


def format_result(value):
    """Format a result for display, hiding float noise (sin 30 -> 0.5, not 0.49999999999999994)."""
    return f"{value:.10g}"


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4):
        print("Usage: python calculator.py <op> <a> [b]", file=sys.stderr)
        print(f"Operations: {', '.join(OPERATIONS)}", file=sys.stderr)
        sys.exit(2)

    try:
        print(format_result(calc(*sys.argv[1:])))
    except (ValueError, OverflowError) as e:
        # Non-zero exit code so the test pipeline can detect failures
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
