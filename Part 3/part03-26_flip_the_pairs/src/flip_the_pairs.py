# Write your solution here

num = int(input('Please type in a number: '))
counter = 1

while counter <= num:
    if counter % 2 == 0:
        print(counter - 1)
    elif counter % 2 != 0 and counter < num:
        print(counter + 1)
    else:
        print(counter)
    counter += 1