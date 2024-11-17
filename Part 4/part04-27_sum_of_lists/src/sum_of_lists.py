# Write your solution here

def list_sum(list_a, list_b) -> list:
    total = []
    for i in range(len(list_a)):
        total.append(list_a[i] + list_b[i])
    
    return total


if __name__ == '__main__':
    a = [1,3,3,22]
    b = [22,35,11,111]

    print(list_sum(a, b))