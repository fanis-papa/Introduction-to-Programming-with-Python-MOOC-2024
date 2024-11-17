# Write your solution here


def no_vowels(sentence: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_vowels_sentence = ''

    for i in sentence:
        if i in vowels:
            continue
        no_vowels_sentence += i

    return(no_vowels_sentence)


if __name__ == "__main__":
    no_vowels("this is an example")
    no_vowels("bcdfghjklmnpqrstvwxyz")