# Write your solution here
word1 = input("Please type in the 1st word:")
word1_to_lower = word1.lower()


word2 = input("Please type in the 2nd word:")
word2_to_lower = word2.lower()


if word1_to_lower > word2_to_lower:
    print(f"{word1_to_lower} comes alphabetically last")
elif word1_to_lower < word2_to_lower:
    print(f"{word2_to_lower} comes alphabetically last")   
else:
    print("You gave the same word twice.") 