# Write your solution here

word = input("Word: ")
spaces = ((28 - len(word)) /2)
print("*" *30)

sentence = "*"
sentence += " " * int(spaces)
sentence += word
sentence += " "  * int(spaces)

if len(sentence) == 28:
    sentence += " "


sentence += "*"

print(sentence)
print("*" *30)

