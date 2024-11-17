# Write your solution here

def sum_of_positives(my_list: list) -> int:
    total = 0
    for i in my_list:
        if i > 0:
            total += i
    return total



if __name__ == '__main__':
    print(f'the result is {sum_of_positives([1,-3, 4, -4, 5])}')