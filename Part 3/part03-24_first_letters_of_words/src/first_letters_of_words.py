# Write your solution here
sentence = input('Please type in a sentence: ')
length = len(sentence)
counter = 0
print(sentence[counter])


while counter < length:
    if sentence[counter] == ' ':
        print(sentence[counter + 1])
    counter += 1
