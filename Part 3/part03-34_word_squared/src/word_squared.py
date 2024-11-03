# Write your solution here


def squared(word, times):     
    big_word = word * times *  times
    counter = 1

    while counter <= times:
        print(big_word[:times])
        big_word = big_word[times:-1]
        counter += 1

if __name__ == '__main__':
    squared('python', 15)