import random
n=input("How many times do you want to run the loop : ")
for i in range(int(n)):
    choice = input("Do you want to roll the dice (y/n) : ")
    if choice == "y":
        dice1= random.randint(1,6)
        dice2= random.randint(1,6)
        print(f'({dice1}, {dice2})')
    elif choice == "n":
        print("thanks for playing")
        break
    else :
        print("Invalid respones!")
