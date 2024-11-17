 # Copy here code of line function from previous exercise



def line(int, text):
    if text == '':
        print('*' * int)
    else:
        print(text[0] * int)

def box_of_hashes(height):
    counter = 1
    while counter <= height:
        line(10, '#')
        counter += 1





if __name__ == '__main__':
    box_of_hashes(5)