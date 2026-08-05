def check_number(n):
    try:
        result = 100 / n
        print("Result:", result)

    except Exception:
        print("Logging error...")
        raise


check_number(0)