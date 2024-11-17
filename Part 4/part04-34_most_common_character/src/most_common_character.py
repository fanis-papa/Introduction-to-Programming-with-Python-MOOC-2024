# Write your solution here



def most_common_character(word: str) -> str:
    letter_tracker = [word[0], 1]

    
    for letter in word:
        counter = word.count(letter)
        if letter == ' ':
            continue    
        if counter > letter_tracker[1]:
            letter_tracker[0] = letter
            letter_tracker[1] = counter


    return letter_tracker[0]


if __name__ == "__main__":
    most_common_character('aaaa bbb ccc ddddd bbb')
    most_common_character('exemplaryelementary')
    most_common_character('"How much wood would a woodchuck chuck if a woodchuck could chuck wood"')