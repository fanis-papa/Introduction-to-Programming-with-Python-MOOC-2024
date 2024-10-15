# Write your solution here

input_num = int(input("Upper limit: "))
# input_num = 100
base = int(input("Base: "))
# base = 4
total_sum = 1

while total_sum <= input_num:
    print(total_sum)
    total_sum *= base