import random

list = ["Rock","Paper","Scissors"]

num_items = len(list)

random_choice = random.randint(0,num_items-1)
Computer_choice = list[random_choice]

Player_Choice = int(input("What do you  Choose? Type 0 for Rock 1 for Paper 2 for Scissors"))
Choose = list[Player_Choice]
print(f"The number you chose {Choose}, The option chosen by the computer {Computer_choice}")

if Choose == Computer_choice:
    print("The result is a draw")
elif Player_Choice - random_choice == 1:
    print("Player Win")
elif Player_Choice - random_choice == 2:
    print("Computer Win")
elif Player_Choice - random_choice == -1:
    print("Computer Win")
elif Player_Choice - random_choice == -2:
    print("Player Win")