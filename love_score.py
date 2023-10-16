print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name=name1+name2
l_name=name.lower()
t=l_name.count("t")
r=l_name.count("r")
u=l_name.count("u")
e=l_name.count("e")
first_digit=t+r+u+e

l=l_name.count("l")
o=l_name.count("o")
v=l_name.count("v")
e=l_name.count("e")
second_digit=l+o+v+e
score=str(first_digit)+str(second_digit)
print(score)
