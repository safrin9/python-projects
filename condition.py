print("welcome to rollercoaster")
bill=0
height=int(input("enter your height in cm\n"))
if height>=120:
    print("you can ride")
    age=int(input("enter your age"))
    if age<12:
        bill=5
        print("child tip is $7")
    elif age<=18:
        bill=12
        print("young tip is $12")
    elif age>=45 and age<=55:
      print(" Your ride is free")
    else:
        bill=15
        print("adult tip is $15")
    photo=input("do you want a photo? Y or N")
    if photo=="Y":
        bill+=3
    print(f"pay {bill}")
else:
    print("you cant ride")