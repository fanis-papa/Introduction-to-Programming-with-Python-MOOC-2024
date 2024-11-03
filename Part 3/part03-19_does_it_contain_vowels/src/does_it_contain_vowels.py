# Write your solution here

word = input("Please type in a string: ")
letters = ["a", "e", "o"]

for letter in letters:
    if letter in word:
        print(f"{letter} found")
    else:
        print(f"{letter} not found")    