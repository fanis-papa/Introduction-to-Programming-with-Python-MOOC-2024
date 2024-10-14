# Write your solution here
int1 = int(input("Please type in the first number:"))
int2 = int(input("Please type in the second number:"))

if int1 > int2:
    print("The greater number was", int1)
elif int2 > int1:
    print("The greater number was", int2)
else:
    print("The numbers are equal!")