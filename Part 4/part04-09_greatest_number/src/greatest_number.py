
def greatest_number(value1, value2, value3):
    if value1 >= value2 and value1 >= value3:
        return value1
    elif value2 >= value1 and value2 >= value3:
        return value2
    return value3




if __name__ == '__main__':
    greatest_number(3, 4, 1)