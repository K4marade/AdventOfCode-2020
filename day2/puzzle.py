from os import replace


with open("/Users/leonardcolin/code/AdventOfCode/day2/password_list.txt") as file:
    data = [line for line in file]

password_lst = []
for policy in data:
    num = policy.split()[0]
    num = [num for num in num.split("-", 1)]

    min = int(num[0])
    max = int(num[1])

    letter = policy.split()[1].strip(":")
    password = policy.split()[2]
    
    if min <= password.count(letter) <= max:
        password_lst.append(password)
    
print(len(password_lst))


    