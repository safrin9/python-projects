import random
rock='''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors='''
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) 
'''
game_images=[rock,paper,Scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice>=3 or user_choice<0:
    print("you typed an invalid number. you lose!")
else:
    print(game_images[user_choice])
    com_choice=random.randint(0,2)
    print("computer chose: ")
    print(game_images[com_choice])

    if user_choice==0 and com_choice==2:
        print("you win!")
    elif com_choice==0 and user_choice==2:
        print("you lose!")
    elif com_choice>user_choice:
        print("you lose!")
    elif user_choice>com_choice:
        print("you win!")
    elif com_choice==user_choice:
        print("its a draw")