class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}")


def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print("Age is valid.")


try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Error:", e)
    print("Invalid age value:", e.age)