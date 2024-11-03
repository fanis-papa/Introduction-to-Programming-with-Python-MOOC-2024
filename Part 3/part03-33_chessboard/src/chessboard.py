# Write your solution here

def chessboard(times):
    counter = 1
    while counter <= times:
        line = ''
        if counter % 2 == 0:
            line += '0'
        else:
            line += '1'
        inside_counter = 1
        while inside_counter < times:
            if line[-1] == '0':
                line += '1'
            else:
                line += '0'
            inside_counter+= 1
        print(line)
        counter += 1



# Testing the function
if __name__ == "__main__":
    chessboard(5)
