# Advanced CLI Calculator
# by <Mohamud Adam Eggee> (simple utility project)

import math

def main():
    print("Advanced Calculator")
    print("type 'exit' to quit, use 'ans' for last result\n")

    prev = 0
    history = []

    while True:
        expr = input("calc> ").strip()
        if not expr:
            continue
        if expr.lower() == 'exit':
            print("bye!")
            break

        # allow using previous answer
        expr = expr.replace('ans', str(prev))

        try:
            # safe eval - only allow math functions and constants
            allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
            res = eval(expr, {"__builtins__": None}, allowed)
            prev = res
            history.append(expr + " = " + str(res))
            print("=", res)
        except ZeroDivisionError:
            print("division by zero")
        except Exception:
            print("invalid expression")

    # optional: print history at the end
    if history:
        print("\n--- session history ---")
        for h in history:
            print(h)

if __name__ == "__main__":
    main()



