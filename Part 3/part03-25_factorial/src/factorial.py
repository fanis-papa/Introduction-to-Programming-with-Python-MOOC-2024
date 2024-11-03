# Write your solution here
while True:
    num = int(input('Please type in a number: '))
    if num <= 0:
        break
    total = 1
    counter = 1
    while counter <= num:
        total *= counter
        counter += 1
    print(f'The factorial of the number {num} is {total}')

print('Thanks and bye!')
