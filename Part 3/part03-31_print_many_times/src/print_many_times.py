# Write your solution here

def print_many_times(text, times):
    counter = 0
    while counter < times:
        print(text)
        counter +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)