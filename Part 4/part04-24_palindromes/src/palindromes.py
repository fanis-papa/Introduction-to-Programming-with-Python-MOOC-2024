

def palindromes(word: str) -> bool:
    word_in_reverse = ''
    for i in range(len(word)-1, -1, -1):
        word_in_reverse += word[i]

    if word != word_in_reverse:
        print("that wasn't a palindrome")
        return False
    print(f'{word} is a palindrome!')
    return True







while True:
    user_inp = input('Please type in a palindrome:')
    if palindromes(user_inp) == True:
        break