# Write your solution here


# limit = 18
limit = int(input("Limit: "))
total_sum = 0
adder = 1
calculations_esentence = ""

while total_sum < limit:
    if adder != 1:
        calculations_esentence += " + "
    total_sum += adder
    calculations_esentence += str(adder) 
    adder += 1

    # print("total sum: ", total_sum)

print("The consecutive sum: ",calculations_esentence, f"= {total_sum}")
