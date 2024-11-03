# Write your solution here

def hash_square(times):
    counter = 1
    while counter <= times:
        print('#'*times)
        counter+= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)