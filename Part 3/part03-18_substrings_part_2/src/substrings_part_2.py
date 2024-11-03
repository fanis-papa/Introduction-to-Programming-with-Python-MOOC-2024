# Write your solution here
word = input("Please type in a string: ")
counter = len(word)

while counter >= 0:
    print(word[counter:len(word)])
    counter -=1