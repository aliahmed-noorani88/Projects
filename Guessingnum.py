import random

print("WELCOME IN THIS GAME")
print("-----GAME START-----")

Generated_Number = random.randint(1,100)

while True:
    Userinput = input("GUESS THE NUMBE:- ")
    if Userinput.lower() == "quit":
        print(f"YOU QUITE\nTHE ANSWER IS {Generated_Number}")
        break

    try:
        Userinput = int(Userinput)
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if(Userinput == Generated_Number):
        print(f"SUCESS! YOU GUESS IS MATCH {Userinput} = {Generated_Number}")
        break
    elif(Userinput < Generated_Number):
        print("Too low. TAKE A BIGGER GUESS.....")
    else:
        print("Too high. TAKE A SMALLER GUESS.....")


print('----GAME OVER----')

