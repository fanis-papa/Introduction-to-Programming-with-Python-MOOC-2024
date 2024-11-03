# Write your solution here
# word = "python"
# word = "pascal"
word = input("Please type in a string: ")
sec_char = word[1]
sec_to_last_char = word[-2]

if sec_char == sec_to_last_char:
    print(f"The second and the second to last characters are {sec_char}")
else:
    print("The second and the second to last characters are different")