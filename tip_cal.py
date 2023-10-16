print("Welcome to the tip calculator!")
p=float(input("What was the total bill?"))
t=int(input("How much tip would you like to give? 10, 12, or 15?"))
s=int(input("How many people to split the bill?"))
bill=t/100*p+p
pay=bill/s

print(f"Each person should pay:{round(pay,2)}")