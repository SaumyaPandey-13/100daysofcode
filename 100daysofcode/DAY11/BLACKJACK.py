import random
logo =( r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print("Welcome to the game of BLACKJACK!")
print(logo)
user=input("do you want to play the game of blackjack?write 'y' for yes and 'n' for no:")
if user.lower() == "n":
    print("Thank you for your time, Goodbye!")
    exit()
elif user.lower() == "y":
    print("Let's start the game of BLACKJACK!")
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0

    def deal_card():
        return random.choice(cards)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    while user_score < 21:
        another_card = input("Do you want to draw another card? Type 'y' or 'n': ")
        if another_card.lower() == 'y':
            user_cards.append(deal_card())
            user_score = sum(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
        else:
            break

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = sum(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score > 21:
        print("You went over 21. You lose!")
    elif computer_score > 21 or user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")
