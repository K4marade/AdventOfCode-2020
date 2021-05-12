with open("/Users/leonardcolin/code/AdventOfCode/day2/password_list.txt") as file:
    data = [line for line in file]

for password in data:
    print(password.split()[0])