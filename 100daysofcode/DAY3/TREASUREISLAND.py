print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad. Do you want to go left or right? (left/right)\n").lower()
if choice1 == "left":
    choice2=input("You've come to a lake. There is an island in the middle of the lake. Do you want to swim across or wait for a boat? (swim/wait)\n").lower()
print(choice2)
if choice1 == "right":
    print("You fell into a hole. Game Over.")
    exit()
if choice2 == "swim":
    print("You arrive at the island unharmed.")
else:
    print("You get attacked by a trout. Game Over.")
    exit()

choice3 = input("On the island, you find a cave with strange markings. Do you want to enter or stay outside? (enter/stay)\n").lower()

if choice3 == "enter":
    print("You have entered the cave, you see a strange creature guarding a treasure chest.")
else:
    print("You decide to stay outside and suddenly a pirate crew arrives! Without a hiding spot, they capture you. Game Over.")
    exit()
choice4 = input("Do you want to fight the creature or try to sneak past it? (fight/sneak)\n").lower()
if choice4 == "fight":
    print("You bravely fight the creature and win!")
else:
    print("You try to sneak past the creature, but it catches you. Game Over.")
    exit()
choice5 = input("You find there are two treasure chests. Do you want to open first or second? (first/second)\n").lower()
if choice5 == "first":
    print("the first chest had a bomb inside, you died. Game Over.")
    exit()
elif choice5 == "second":
    print("Congratulations! You found the treasure and won the game!")