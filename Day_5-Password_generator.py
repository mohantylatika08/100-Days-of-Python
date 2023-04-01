import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level

# password1 = ""
# for i in range(0, nr_letters):
#     random_letters = random.choice(letters)
#     password1 = password1 + random_letters

# password2 = ""
# for j in range(0,nr_symbols):
#      random_symbols = random.choice(symbols)
#      password2 += random_symbols

# password3 = ""
# for k in range(0,nr_numbers):
#     random_numbers = random.choice(numbers)
#     password3 += random_numbers

# password = password1 + password2 +password3
# print("\nYour password is:" ,password)

# Difficult level

password = []
for i in range(0, nr_letters):
    random_letters = random.choice(letters)
    password.append(random_letters)

for j in range(0,nr_symbols):
     random_symbols = random.choice(symbols)
     password.append(random_symbols)

for k in range(0,nr_numbers):
    random_numbers = random.choice(numbers)
    password.append(random_numbers)

#password = password1 + password2 +password3
random.shuffle(password)

final_password= ""
for char in password:
    final_password+=char
print("\nYour password is:" ,final_password)