# Write your solution here

my_list = []

while True:
    user_inp = int(input("New item: "))
    if user_inp == 0:
        print('Bye!')
        break
    else:
        my_list.append(user_inp)
        print(f'The list now: {my_list}')
        print(f'The list in order: {sorted(my_list)}')