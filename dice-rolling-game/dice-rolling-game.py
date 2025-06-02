import random
# n=input("How many times do you want to run the loop : ")
# for i in range(int(n)):
#     choice = input("Do you want to roll the dice (y/n) : ")
#     if choice == "y":
#         dice1= random.randint(1,6)
#         dice2= random.randint(1,6)
#         print(f'({dice1}, {dice2})')
#     elif choice == "n":
#         print("thanks for playing")
#         break
#     else :
#         print("Invalid respones!")

# guess the random number b/w 1-10
# random = random.randint(1,10)
# print(random)
# while True:
#     try:
#         guess=int(input("guess the number : "))
#         if guess<random:
#             print("too low")
#         elif guess>random:
#             print("too high")
#         else:
#             print("congrats you guessed the number : ", random)
#             break
#     except:
#         print("please type a number")

# rolling dice game

pick = input("pick rock-paper or scissors : (r/p/c) - ")

comp = random.choice(["r", "p", "c"])

if pick == "r":
    if comp == "p":
        print("you lost computer chose : ", comp)
    elif comp == "r":
        print("Its a draw computer chose : ", comp)
    elif comp == "c":
        print("Congrats you won computer chose : ", comp)

elif pick == "p":
    if comp == "p":
        print("Its a draw computer chose : ", comp)
    elif comp == "r":
        print("Congrats you won computer chose : ", comp)
    elif comp == "c":
        print("you lost computer chose : ", comp)

elif pick == "c":
    if comp == "p":
        print("Congrats you won computer chose : ", comp)
    elif comp == "r":
        print("you lost computer chose : ", comp)
    elif comp == "c":
        print("Its a draw computer chose : ", comp)

