# Write your solution here


def all_the_longest(word_list: list) -> list:
    long_words = [word_list[0]]
    for i in word_list:
        if len(i) > len(long_words[-1]):
            long_words = []
            long_words.append(i)
        elif len(i) == len(long_words[-1]) and i != long_words[-1]:
            long_words.append(i)
    
    return long_words


if __name__ == "__main__":
    all_the_longest(["first", "second", "fourth", "eleventh"])
    all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])
    all_the_longest(('Mark', 'Paul', 'Bill', 'Jan', 'Tim', 'Jean'))
    all_the_longest(('Seraenina', 'Gandalf', 'Harry', 'Walter'))

    
