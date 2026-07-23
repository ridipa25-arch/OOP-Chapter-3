class MyCustomError(Exception):
    """" A custom exception for my application"""
    pass
def check_age(age):
    if age < 0:
        raise MyCustomError("Age cannot be negative")
    return age
try:
    check_age(-5)
except MyCustomError as e:
    print(f"Caught: {e}")   