import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
Num_Of_letters = int(input("How many LETTERS would you like in your password?\n"))
Num_Of_symbols = int(input("How many SYMBOLS would you like in your password?\n"))
Num_Of_numbers = int(input("How many NUMBERS would you like in your password?\n"))

Password = []
#Passwors = ""

for let in range(1,Num_Of_letters+1):
    Password.append(random.choice(letters))#Here we add num_of_letters times random letters to list

for num in range(1,Num_Of_numbers+1):
    Password.append(random.choice(numbers))#Same

for symb in range(1,Num_Of_symbols+1):
    Password.append(random.choice(symbols))#Same

random.shuffle(Password)#Then we call 'shuffle' function to mix the order

Result = ""
for a in Password:
    Result += a

print(f"Your password has been generated: {Result}")
