# Write your solution here
attempts = 0

while True:
    input_pin = int(input("PIN: "))
    attempts += 1
    if input_pin == 4321 and attempts == 1:
        print("Correct! It only took you one single attempt!")
        break
    elif input_pin == 4321 and attempts > 1:
        print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")
        
 