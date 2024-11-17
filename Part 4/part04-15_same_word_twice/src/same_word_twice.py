# Write your solution here

my_list = []


while True:
     user_inp = input('Word: ')
     if user_inp in my_list:
          print(f'You typed in {len(my_list)} different words')
          break
     else:
          my_list.append(user_inp)



