number = int(input("Give a number:"))
if number % 4 == 0:
    print("The number is a multiple of 4")
elif number % 2 == 0:
        print("The number is even")
else:
    print("The number is odd")
#__________________________________

num = int(input("Give a number(num):"))
check = int(input("Give a number(check):"))
if num % check == 0:
    print(num, "divides evenly into", check)
else: print(num, "do not divides evenly into", check)