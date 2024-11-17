# Write your solution here

def even_numbers(my_list: list) -> list:
    only_evens = []
    for i in my_list:
        if i % 2 == 0:
            only_evens.append(i)
    return only_evens




if __name__ == '__main__':
    print(even_numbers([1,2,3,4,5]))