# Write your solution here

def same_chars(word, index1, index2):
    if len(word) <= index1 or len(word) <= index2:
        return False
    elif word[index1] == word[index2]:
        return True
    return False




if __name__ == '__main__':
    print(same_chars('aaaa', 1, 2))
