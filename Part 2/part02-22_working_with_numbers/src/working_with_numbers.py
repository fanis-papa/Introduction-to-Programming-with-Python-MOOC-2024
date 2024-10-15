# Write your solution here
total_nums = 0
total_sum = 0
negative_nums = 0

print("Please type in integer numbers. Type in 0 to finish. ")
while True:
    input_num = int(input("Number: "))
    if input_num != 0:
        total_nums += 1
        total_sum += input_num
        if input_num < 0:
            negative_nums += 1
    else:
        print(f"Numbers typed in {total_nums}")
        print(f"The sum of the numbers is {total_sum}")
        print(f"The mean of the numbers is {total_sum / total_nums}")
        print(f"Positive numbers {total_nums - negative_nums}")
        print(f"Negative numbers {negative_nums}")
        break