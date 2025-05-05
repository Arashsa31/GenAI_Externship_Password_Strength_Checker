
score = 0
special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

#Step 1: Input the Password
password = input("Enter a password: ")

#Step 2: Evaluate the Password
if len(password) >= 8:
    score += 2
else:
    print("Your password needs to be at least 8 characters long.")

if any(char.isupper() for char in password):
    score += 2
else:
    print("Your password needs at least one uppercase letter.")

if any(char.islower() for char in password):
    score += 2
else:
    print("Your password needs at least one lowercase letter.")

if any(char.isdigit() for char in password):
    score += 2
else:
    print("Your password needs at least one digit.")

if any(char in special_chars for char in password):
    score += 2
else:
    print("Your password needs at least one special character.")

if score == 10:
    print("Your password is strong! 💪")

print(f"Password Strength:",score,"/10")


