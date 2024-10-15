# Write your solution here

# limit = 18
limit = int(input("Limit: "))
total_sum = 0
adder = 1

while total_sum < limit:
    
    total_sum += adder
    adder += 1

    # print("total sum: ", total_sum)
    # print("adder: ", adder)

print(total_sum)