def divide(a, b):
    try:
        return a/b
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error occurred:{e}")
        raise
    try:
        divide(10,0)
    except ZeroDivisionError:    
        print("Handled: cannot divide by zero")
    try:
        divide(10, "a")  
    except TypeError:
        print("Handled: invalid types for division")
