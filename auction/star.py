

auction={}
def find(record):
    h=0
    winner=""
    for bidder in record:
      amount=record[bidder]  
      if amount>h:
          h=amount
          winner=bidder
    print(f"winner is {winner} with highest bid {h}")
finished=False
while not finished:
    name=input("name\n")
    price=int(input("bid\n"))
    auction[name]=price
    h=input("anyone? yes or no?\n")
    if h=="no":
        finished=True
        find(auction)
    elif h=="no":
        auction.clear()