# Write your solution here

def anagrams(string1: str, string2: str) -> bool:
    if sorted(string1.lower()) == sorted(string2.lower()):
        return True
    return False



if __name__ == '__main__':
    print(anagrams('tame', 'meta'))
    print(anagrams('tabby', 'batty'))
