# Write your solution here

# word = "mammoth"
# word = "bamana"
# word = "tomato"
# word = "pythom"
word = input("Please type in a word: ")

letter = input("Please type in a character: ")

finder = word.find(letter)

if finder >= 0:
    if len(word) >= finder + 3:
        print(word[finder:finder + 3])
    