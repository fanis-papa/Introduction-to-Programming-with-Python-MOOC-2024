# Write your solution here


def everything_reversed(my_list: list) -> list:
    reversed_copy = my_list[::-1]
    reversed_list = []

    for i in reversed_copy:
        reversed_list.append(i[::-1])

    return reversed_list


if __name__ == "__main__":
    everything_reversed(["Hi", "there", "example", "one more"])