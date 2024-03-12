from replit import clear



print("Welcome to the secret auction program.")

other_bidders = 'yes'
bidder_dictionary = {}
bidders_string = ""
while other_bidders == 'yes':
    name = input("What's your name?\n").lower()
    bid = int(input("What's your bid?\n€"))
    bidder_dictionary[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    bidders_string += "".join(f"{name.capitalize()}:€{bid}, ")
print(f"Bidders: {bidders_string}")
if other_bidders == 'yes':
    clear()



highest_bidder = max(bidder_dictionary, key=bidder_dictionary.get)
highest_bid = bidder_dictionary[highest_bidder]

print(f"The highest bid was {highest_bid} made by {highest_bidder}")



