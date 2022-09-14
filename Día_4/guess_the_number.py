from random import randint

menu = """
Welcome to the game!
Rules:
1- You need to guess a number in the range of 1-100
2- You have only 8 attempts to guess the number
Lets Start
"""
print(menu)


attempts = 0
num_to_guess = randint(1,101)

# Ciclo para evaluar el numero ingresado por el usuario

while attempts < 8:
    user_choice = int(input("what do you think is the number?: "))
    if user_choice == num_to_guess:
        attempts += 1
        print(f"You WIN! it took you {attempts} attempts")

        break
    elif user_choice not in  range(1,101):
        print(f"{user_choice} is not allowed only number from 1 to 100")
        continue

    elif user_choice < num_to_guess:
        print(f"{user_choice} is smaller than the number")
        attempts += 1
        print(f"You have {attempts} attempts left")

    elif user_choice > num_to_guess:
        print(f"{user_choice} is larger than the number")
        attempts += 1
        print(f"You have {attempts} attempts left")

if user_choice != num_to_guess:
    print(f"You LOSE!! the number was {num_to_guess}")








