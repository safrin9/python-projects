import random
letters=['a', 'b', 'c', 'd' , 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy
#password=""
#for l in range(1,nr_letters+1):
   #r_char= random.choice(letters)
   #password=password+r_char
   #print(password)
#for s in range(1,nr_symbols+1):
  # r_s=random.choice(symbols)
   #password=password+r_s
   
   #print(password)
#for n in range(1,nr_numbers+1):
   #r_n=random.choice(numbers)
   #password=password+r_n

#print(password)

#hard5

password=[]
for l in range(1,nr_letters+1):
   r_char= random.choice(letters)
   password.append(r_char)
   
for s in range(1,nr_symbols+1):
   r_s=random.choice(symbols)
   password.append(r_s)

 
for n in range(1,nr_numbers+1):
   r_n=random.choice(numbers)
   password.append(r_n)
print(password)
random.shuffle(password)
print(password)
password1=""
for char in password:
    password1+=char
print(password1)
