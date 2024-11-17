
def first_word(sentence):
    return sentence[0:sentence.find(' ')]

def second_word(sentence):
    new_sentence = sentence[sentence.find(' ')+1:]
    if new_sentence[new_sentence.find(' ')] != ' ':
        return new_sentence[0:]
    return new_sentence[0:new_sentence.find(' ')]

def last_word(sentence):
    counter = -1
    while sentence[counter] != ' ':
        counter -=1
    return sentence[counter+1:]

if __name__ == '__main__':
    first_word("it was a dark and stormy python")
    second_word("it was a dark and stormy python")
    last_word("it was a dark and stormy python")
    print(second_word('first second'))
    print(second_word('it was a dark and stormy python'))
    