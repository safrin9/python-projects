import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
n=len(cards)
game=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
def chose(you,com):
    print(f"Your final hand: {you}, final score: {sum(you)}")
    print(f"Computer's final hand: {com}, final score: {sum(com)}")
    if sum(you)>sum(com) and sum(you)<21:
        print("you win")
    elif sum(com)>sum(you) and sum(com)>21:
        print("you win")
    elif sum(you)>sum(com) and sum(you)>21:
        print("you lose")
    else:
        print("you lose, your opponent has Blackjack")
if game=='y':
    you=[]
    com=[]
    you=random.choices(cards,k=2)
    print(f" Your cards: {you}, current score: {sum(you)}")
    com=random.choices(cards,k=2)
    print(f"computer first card: {com[0]}")
    again=input("Type 'y' to get another card, type 'n' to pass:")
    if again=="y":
        you.append(random.choice(cards))
        print(f" Your cards: {you}, current score: {sum(you)}")
        print(f"computer first card: {com[0]}")
       # print(f"Your final hand: {you}, final score: {sum(you)}")
        com.append(random.choice(cards))
        #print(f"Computer's final hand: {com}, final score: {sum(com)}")
        #if sum(you)>sum(com) and sum(you)<22:
         #   print("you win")
        #elif sum(com)>sum(you) and sum(com)>22:
         #   print("you win")
        #else:
         #   print("you lose")
        chose(you,com)
    else:
        chose(you,com)


    
