# Write your solution here
sentence = ""
last_word = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == last_word:
        print(sentence)
        break
    else :
        sentence += word + " "
        last_word = word
    