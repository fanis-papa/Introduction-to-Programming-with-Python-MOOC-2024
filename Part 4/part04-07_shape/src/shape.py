# Copy here code of line function from previous exercise and use it in your solution


def line(int, text):
    if text == '':
        print('*' * int)
    else:
        print(text[0] * int)


def shape(width, char, height, filler):
    counter_chars = 1
    while counter_chars <= width:
        line(counter_chars, char)
        counter_chars += 1

    counter_filler = 1
    while counter_filler <= height:
        line(width, filler)
        counter_filler += 1



if __name__ == '__main__':
    shape(5, 'h', 3, '@')