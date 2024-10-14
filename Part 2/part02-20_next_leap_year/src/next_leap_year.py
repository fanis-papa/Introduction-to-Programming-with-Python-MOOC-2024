# Write your solution here
year = int(input("Please type in a year: "))
year_copy = year

while True:
    year_copy += 1
    if year_copy % 4 == 0:
        if year_copy % 100 == 0:
            if year_copy % 400 == 0:
                print(f"The next leap year after {year} is {year_copy}")
                break

        else:
            print(f"The next leap year after {year} is {year_copy}")
            break
