def check_number(n):
    try:
        result = 100 / n
        print("Result:", result)

    except Exception:
        print("Logging error...")
        raise


try:
    check_number(0)

except ZeroDivisionError:
    print("Caller caught the exception successfully.")