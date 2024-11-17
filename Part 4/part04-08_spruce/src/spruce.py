# Write your solution here

def spruce(size):
    counter = size -1
    width = 1
    print('a spruce!')
    while counter >= 0:
        print(' ' * counter + '*'*width )
        counter -= 1
        width += 2
    print(' ' * (size-1) + '*')



if __name__ == '__main__':
    spruce(3)
    spruce(6)