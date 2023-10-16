words=['hello','rabbit','ziraf']



import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

l=random.choice(words)
print(l)
display=[]
lenth=len(l)
k=6
for _ in l:
    display+="_"
print(display)   
end=False

while not end:

    guess=input("guess a letter ").lower()
    for position in range(lenth):
        letter=l[position]
        if letter==guess:
            display[position]=letter
    if guess not in l:
        k -= 1
        if k == 0:
            end = True
            print("You lose.")
    print(display)
    if "_" not in display:
        end=True
        print("you win")
    print(stages[k])
    

