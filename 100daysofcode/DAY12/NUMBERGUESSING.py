_logo=(r'''__  __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
  / ___\|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
 / /_/  >  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \___  /|____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
/_____/             \/     \/     \/             \/     \/       \/            \/    \/     \/       
''')
import random
print(_logo)
print("welcome to the numbers guessing game!")
print("you'll get 5 chances to guess the number correctly")
number = random.randint(1, 100)
user_chances = 5
while user_chances > 0:
    user = int(input("guess a number between 1 and 100: "))
    if user == number:
        print("you guessed the number correctly")
        break
    elif user > number:
        print("you guessed the number incorrectly, your guess is too high")
        user_chances -= 1
    elif user < number:
        print("you guessed the number incorrectly, your guess is too low")
        user_chances -= 1
    if user_chances == 0:
        print("you have no chances left, you lose!")
        break
    else:
        print(f"you have {user_chances} chances left")