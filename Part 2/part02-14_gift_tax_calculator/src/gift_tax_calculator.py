# Write your solution here
gift_amount = int(input("Value of gift: "))

if gift_amount >= 5000 and gift_amount < 25000:
    tax = 100 + (gift_amount - 5000) * 0.08

elif gift_amount >= 25000 and gift_amount < 55000:
    tax = 1700 + (gift_amount - 25000) * 0.1

elif gift_amount >= 55000 and gift_amount < 200000:
    tax = 4700 + (gift_amount - 55000) * 0.12

elif gift_amount >= 200000 and gift_amount < 1000000:
    tax = 22100 + (gift_amount - 200000) * 0.15

elif gift_amount >= 1000000:
    tax = 142100 + (gift_amount - 1000000) * 0.17


if gift_amount < 5000:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")


    


