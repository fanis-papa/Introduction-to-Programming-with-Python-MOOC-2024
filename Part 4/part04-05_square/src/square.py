# Copy here code of line function from previous exercise

def line(int, text):
    if text == '':
        print('*' * int)
    else:
        print(text[0] * int)

def square(times, char):
    counter = 1
    while counter <= times:
        line(times, char)
        counter += 1


if __name__ == '__main__':
    square(5, 'o')