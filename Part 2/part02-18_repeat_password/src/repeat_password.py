# Write your solution here
password = input("Password: ")

while True:
    repeat_pass = input("Repeat password: ")
    if repeat_pass != password:
        print("They do not match!")
    else:
        break
print("User account created!")