# Write your solution here
num = int(input('Please type in a number: '))
# num = 6
num_copy = num
counter = 1


while counter <= num_copy/2 :
    print(counter)
    print(num)
    num -= 1 
    counter += 1

if num_copy % 2 != 0:
    print(counter)