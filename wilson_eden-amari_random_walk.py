
# rows, columns = (15, 15)
# grid = [[0]*columns]*rows

# for row in grid:
#     print(row)

# print(grid)

# grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# for thing in grid:
#     i = 1
#     while i < 15:
#         print(thing)
#         i += 1

# def print_grid():
#     grid = []
#     i = 0
#     while i < 15:
#         grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#         i += 1
#     print(grid)

import random

rows = int(input("Please enter a number of rows: "))
columns = int(input("Please enter a number of columns: "))
print("\n")
print("Starting Grid")

grid = [[0 for thing in range(columns)] for thing2 in range(rows)]

# Initial grid 
def print_grid():
    for row in range(len(grid)):
        print(grid[row])
print_grid()


agent_directions = random.randrange(1, 5)

def update_pos():
    # Agent Initial Position: Middle of the Board
    init1 = 7
    init2 = 7
    grid[init1][init2] = 1

    agent_pos = [init1, init2]
    # (x, y) coord for agent posiiton

    move_count = 0
    while move_count < 30: 
        # up
        if agent_directions == 1:
            agent_pos[1] += 1
            grid[init2] += 1
            move_count += 1

        # down
        elif agent_directions == 2:
            agent_pos[1] -= 1
            grid[init2] -= 1
            move_count += 1

        # left 
        elif agent_directions == 3:
            agent_pos[0] -= 1
            grid[init1] -= 1
            move_count += 1     
        # right
        elif agent_directions == 4:
            agent_pos[0] += 1
            grid[init1] += 1
            move_count += 1


print("\n")
print("Movement Heat Map")
update_pos()
print_grid()