# Write your solution here

num = int(input('Please type in a number: '))
counter = 1

while counter <= num:
    counter1 = 1
    while counter1 <= num:
        print(f"{counter} x {counter1} = {counter * counter1}")
        counter1 += 1
    counter += 1


