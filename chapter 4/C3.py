class PasswordError(Exception):
    pass


class PasswordTooShortError(PasswordError):
    pass


class PasswordTooWeakError(PasswordError):
    pass


def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError(
            "Password must contain at least 8 characters."
        )

    if not any(char.isupper() for char in password) or \
       not any(char.isdigit() for char in password):
        raise PasswordTooWeakError(
            "Password must contain an uppercase letter and a number."
        )

    print("Password is valid.")


try:
    password = input("Enter password: ")
    validate_password(password)
except PasswordTooShortError as e:
    print("Error:", e)
except PasswordTooWeakError as e:
    print("Error:", e)