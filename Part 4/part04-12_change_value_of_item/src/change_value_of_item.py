# Write your solution here

my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input('Please provide the index: '))
    if index == -1:
        break
    value = int(input('Please provide the value: '))
    my_list[index] = value
    
    print(my_list)