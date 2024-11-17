# Write your solution here

def formatted(nums_list: list) -> list:
    formatted_list = []
    for i in nums_list:
        formatted_list.append(f'{i:.2f}')

    return formatted_list




if __name__ == "__main__":
    formatted([1.234, 0.3333, 0.11111, 3.446])