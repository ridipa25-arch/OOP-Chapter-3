class NegativeNumberError(Exception):
    pass


def check_number(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    else:
        print("Number is valid.")


try:
    number = int(input("Enter a number: "))
    check_number(number)
except NegativeNumberError as e:
    print("Error:", e)