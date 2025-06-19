names = {}
bidding_ongoing = True

while bidding_ongoing:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: ₹"))
    names[name] = bid

    print("\n" * 100)# Simulate clearing the screen for secrecy

    user = input("Are there any more bidders? Answer with 'y' or 'n': ").lower()
    if user == "n":
        bidding_ongoing = False

highest_bid = 0
winner = ""

for name in names:
    if names[name] > highest_bid:
        highest_bid = names[name]
        winner = name

print(f"\n The winner is {winner} with a bid of ₹{highest_bid}")
print("Thank you for participating in the secret bid program.")