# Write your solution here

# word = "mammoth"
# word = "bamana"
# word = "tomato"
# word = "pythom"
word = input("Please type in a word: ")
letter = input("Please type in a character: ")


while len(word) != 0:
    finder = word.find(letter)
    if finder >= 0:
        if len(word) >= finder + 3:
            print(word[finder:finder + 3])
        word = word[finder + 1:]     
    else:
        break



