# Copy here code of line function from previous exercise

def line(int, text):
    if text == '':
        print('*' * int)
    else:
        print(text[0] * int)


def triangle(times):
    counter = 1
    while counter <= times:
        line(counter, '#')
        counter += 1



if __name__ == '__main__':
    triangle(5)
