import random
letters= list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_chars = []

for _ in range(nr_letters):
    password_chars.append(random.choice(letters))

for _ in range(nr_symbols):
    password_chars.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_chars.append(random.choice(numbers))

random.shuffle(password_chars)

password = "".join(password_chars)

print(f"\nYour password: {password}")
