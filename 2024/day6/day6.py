from itertools import product, chain
import math
Point = tuple[int,int] # defining to simplify functions
Space = dict[Point, str] # defining to simplify functions
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
available_directions = list(directions.keys())

# function to create a dictionary. Each Letter has coordinates r and c
def lookup(lines: list[str]) -> Space:
    return{(r,c): char for r,row in enumerate(lines) for c,char in enumerate(row)}

def next_direction(direction):
    return available_directions[
        (available_directions.index(direction) + 1)
        % len(available_directions)]

def guard_in_grid(position):
    return (0<= position[0] < 130 and 0<= position[1] < 130)

def start(space: Space):
    carrots = ['^','<', '>', 'v']
    start = [key for key,val in space.items() if val in carrots]
    start_position = (start[0])
    if space.get(start_position) == '^':
        direction = 'up'
    elif space.get(start_position) == '<':
        direction = 'left'
    elif space.get(start_position) == '>':
        direction = 'right'
    elif space.get(start_position) == 'v':
        direction = 'down'
    return start_position, direction

def move(space, start_position, direction):
    x,y = start_position[0], start_position[1]
    if direction == 'up':
        new_position = (x - 1, y)
        space[start_position] = 'X'
        space[new_position] = '^'
    elif direction == 'left':
        new_position = (x, y - 1)
        space[start_position] = 'X'
        space[new_position] = '<'
    elif direction == 'right':
        new_position = (x, y + 1)
        space[start_position] = 'X'
        space[new_position] = '>'
    elif direction == 'down':
        new_position = (x + 1, y)
        space[start_position] = 'X'
        space[new_position] = 'v'
    return new_position

def pos_in_front(start_position, direction):
    x,y = start_position[0], start_position[1]
    if direction == 'up':
        new_position = (x - 1, y)
    elif direction == 'left':
        new_position = (x, y - 1)
    elif direction == 'right':
        new_position = (x, y + 1)
    elif direction == 'down':
        new_position = (x + 1, y)
    return new_position

def part_one(space, start_position, direction):
    position = start_position
    while guard_in_grid(position):
        in_front = pos_in_front(position, direction)  #get position in front of guard, return position front of me
        val_in_front = space.get(in_front)  # check what's in that position
        if val_in_front == "#":
            direction = next_direction(direction)   #if obstacle, rotate 90 degs
            position = move(space, position, direction) 
        else:
            position = move(space, position, direction)  #if not obstacle, move forward
    return 

def x_count(space):
    return len([key for key,val in space.items() if val == 'X'])

def part_two():
    pass


def day6() -> None:
    with open("day6/example.txt", "r") as file:
        lines = [l.strip() for l in file.readlines()]

    space = lookup(lines)
    start_position, direction = start(space)
    #print(space)
    print(start(space))

    # new_position = move(space, start_position, direction)
    # print(space)
    # print(new_position)
    part_one(space, start_position, direction)
    #print(space)
    print(x_count(space))

day6()
