
def distinct_numbers(my_list) -> list:
    sorted_list = sorted(my_list)
    new_list = [sorted_list[0]]

    for i in sorted_list:
        if new_list[-1] != i:
            new_list.append(i)


    return new_list



if __name__ == '__main__':
    distinct_numbers([4,4,3,3,2,4,5,1,2,2])