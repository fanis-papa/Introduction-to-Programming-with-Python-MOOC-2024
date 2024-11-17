# Write your solution here

def length_of_longest(words_list) -> int:
    longest = 0

    for i in words_list:
        if len(i) > longest:
            longest = len(i)
    
    return longest



if __name__ == '__main__':
    print(length_of_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))