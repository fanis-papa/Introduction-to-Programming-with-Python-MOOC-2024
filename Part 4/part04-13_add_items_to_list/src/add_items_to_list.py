# Write your solution here

times = int(input('How many items to add: '))
counter = 1
items_list = []

while counter <= times:
    items_list.append(int(input(f'Item {counter}: ')))
    counter += 1

print(items_list)