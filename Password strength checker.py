def password_checker(password):
    has_digit = False
    has_special = False
    if len(password) < 8:
        return "Weak Password"
    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch in "@#$":
            has_special = True
    if has_digit and has_special:
        return "Strong Password"
    else:
        return "Weak Password"
pwd = input("Enter password: ")
print(password_checker(pwd))