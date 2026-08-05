def safe_divide(a, b):
    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except TypeError:
        print("Error: Both values must be numbers.")


safe_divide(20, 4)
safe_divide(20, 0)
safe_divide(20, "5")