# Write your solution here

my_list = []
print(f"The list is now {my_list}")

while True:
    
    user_inp = input("a(d)d, (r)emove or e(x)it: ").lower()
    
    if user_inp == 'x':
        break
    elif user_inp == 'd':
        if my_list == []:
            my_list.append(1)
        else:
            last_list_item = my_list[-1]
            my_list.append(last_list_item + 1)   
        print(f"The list is now {my_list}")
    elif user_inp == 'r':
        my_list.pop()
        print(f"The list is now {my_list}")

print('Bye!')
    
    
