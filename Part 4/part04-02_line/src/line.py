# Write your solution here
# You can test your function by calling it within the following block 


def line(int, text):
    if text == '':
        print('*' * int)
    else:
        print(text[0] * int)


if __name__ == '__main__':
    line(4, 'lol')