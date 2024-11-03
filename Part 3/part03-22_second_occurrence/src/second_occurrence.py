# Write your solution here
word = input("Please type in a string: ")
word_copy = word
letter = input("Please type in a string: ")
finder = word.find(letter)


if finder >= 0:
    word_copy = word[finder + len(letter):]
    if word_copy.find(letter) >= 0:
        word_copy_length_diff = len(word) - len(word_copy)
        print(f"The second occurrence of the substring is at index {word_copy_length_diff + word_copy.find(letter)}.")
    else:
        print("The substring does not occur twice in the string.")
else:
        print("The substring does not occur twice in the string.")
