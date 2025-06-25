import random
#Addition MathGame

def Generate_Number(): #for Addition
    Random_Number1 = random.randint(10,100)
    Random_Number2 = random.randint(10,100)
    Random_Number = Random_Number1 + Random_Number2
    print(f"what is {Random_Number1} + {Random_Number2}")
    return Random_Number

def level_up_game(): #for level up
    level = 1
    while level <= 10:
        Random_Number = Generate_Number()

        print(f"\n -----level {level}----- ")

        try:
            User_input = int(input("Your answer := "))
        except ValueError:
            print("Wrong 'ANSWER' try again")
            continue 

        if User_input == Random_Number:
            print(f"{User_input} GUESSED IT CORRECT! 😘")
            level += 1
            if level <= 10:
                print(f"You're now at Level {level}!")

        else:
            print(f"Wrong! The correct answer was {Random_Number}")
            print("-------GAME OVER-------")
            break

    else:
        print("\nCongratulations! You completed all 10 levels! 🏆")

level_up_game()