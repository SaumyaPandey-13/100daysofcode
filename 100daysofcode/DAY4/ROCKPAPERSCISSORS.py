print("welcome to rock paper scissors")
import random

chances_left = 3
game_ongoing = True

while game_ongoing and chances_left > 0:
    user = input("choose rock, paper or scissors: ").lower()

    if user == "rock":
        print(r'''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')
    elif user == "paper":
        print(r'''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')
    elif user == "scissors":
        print(r'''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')
    else:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue  # skips the rest of the loop and asks again

    options = ["rock", "paper", "scissors"]
    x = random.choice(options)
    print(x)
    if x == "rock":
        print(r'''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')
    elif x == "paper":
        print(r'''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')
    else:
        print(r'''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')

    if user == x:
        print("It's a tie!")
    elif (user == "rock" and x == "scissors") or \
         (user == "scissors" and x == "paper") or \
         (user == "paper" and x == "rock"):
        print("You win!")
    else:
        print("You lose!")
        chances_left -= 1
        if chances_left == 0:
            print("You have no chances left. Game over!")
            game_ongoing = False
        else:
            print(f"Chances left: {chances_left}")
