# The Secret Auction Program
# Insert your name and bid and compare with friends which bid is the highest one

from replit import clear

bidders = []
def add_new_bidder(name, bid):
  bidders.append({"name": name,
                     "bid": bid})

bid_happening = True
while bid_happening == True:
  name = input("What's your name? ")
  bid = float(input("What's your bid? "))
  bid_validation = input("Are there any other bidders? Type 'yes' or 'no'.  ").lower()
  add_new_bidder(name, bid)
  if bid_validation == 'yes':
    clear()
  elif bid_validation == 'no':
    clear()
    bid_happening = False

highest_bid = 0
clear()
for i, bid in enumerate(bidders):
  if bid.get('bid') > highest_bid:
    highest_bid = bid.get('bid')
    highest_name = bid.get('name')

print(f"The highest bidder is: {highest_name}\nValue: ${highest_bid}")

