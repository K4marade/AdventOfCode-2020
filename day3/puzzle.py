
with open("/Users/leonardcolin/code/AdventOfCode/day3/map.txt") as file:
    area = [line[0: -1] for line in file]
    
    

def number_of_trees(down_step, right_step):
    x, y = 0, 0
    trees_count = 0
    last_row = len(area) - 1
    col_modulo = len(area[0])

    while y <= last_row:

        if area[y][x] == "#":
            trees_count += 1

        x = (x + right_step) % col_modulo
        y += down_step
        
    return trees_count

# Part one:
print("There is " + str(number_of_trees(1, 3)) + " trees")




