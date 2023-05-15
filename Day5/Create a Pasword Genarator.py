import random

letters = ["a","b","c","d","e","f","g","h","ı","i","u","ü","j","k","l","m","n","t","s","ş","z","y"
           "A","B","C","D","E","F","G","H","I","İ","U","Ü","J","K","L","M","N","T","S","Ş","Z","Y"]

numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","#","$","%","&","(",")","*","+"]

print("Welcome to the PyPassword Genarator!")

nr_letters = int(input(f"How many letters would you like in your pasword?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_number = int(input(f"How many number would you like?\n"))

pasword_list = []
for i in range(1,nr_letters + 1):
    pasword_list.append(random.choice(letters))
for i in range(1,nr_symbols + 1):
    pasword_list.append(random.choice(symbols))
for i in range(1,nr_number + 1):
    pasword_list.append(random.choice(numbers))

random.shuffle(pasword_list)
 
pasword = ""
for char in pasword_list:
    pasword += char

print(pasword)