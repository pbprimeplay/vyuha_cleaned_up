"""Interactive text interface for Nexus Calc (kept for a future standalone client).

Run with: python interactive.py
"""
from calculator import calc, format_result, OPERATIONS, UNARY_OPS


def main():
    print("--- NEXUS CALC: TEXT INTERFACE MODE ---")
    print("Type 'exit' to quit. Enter 'ans' to reuse the last result.")
    last_result = 0.0

    while True:
        try:
            operation = input(f"Enter operation ({', '.join(OPERATIONS)}): ").strip()
            if operation == "exit":
                break
            if operation not in OPERATIONS:
                print("Unknown operation, try again.\n")
                continue

            num1 = input("Enter first number (or 'ans'): ").strip()
            num2 = None
            if operation not in UNARY_OPS:
                num2 = input("Enter second number (or 'ans'): ").strip()

            num1 = last_result if num1 == "ans" else num1
            num2 = last_result if num2 == "ans" else num2

            last_result = calc(operation, num1, num2)
            print(f"--> RESULT: {format_result(last_result)}\n")

        except (ValueError, OverflowError) as e:
            print(f"Error: {e}\n")
        except (EOFError, KeyboardInterrupt):
            # Exit cleanly on Ctrl+C / end of input instead of looping forever
            print()
            break


if __name__ == "__main__":
    main()
