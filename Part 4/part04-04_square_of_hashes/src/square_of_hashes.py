# Copy here code of line function from previous exercise

def line(int, text):
    if text == '':
        print('*' * int)
    else:
        print(text[0] * int)


def square_of_hashes(times):
    counter = 1
    while counter <= times:
        line(times, '#')
        counter += 1

    return

if __name__ == '__main__':
    square_of_hashes(5)