# Write your solution here

user_int = int(input("Please type in a positive integer: "))

for i in range(-user_int, user_int+1):
    if i == 0:
        continue
    print(i)
