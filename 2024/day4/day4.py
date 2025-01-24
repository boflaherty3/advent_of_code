"""with open("day4/data.txt", "r") as file:
    content = file.read()
    content_no_spaces = content.replace(" ", "")
row_length = 141
print(len(content))
#print(content[139])

forward_match = []
# check for forwards matches of XMAS
for i in range(len(content)-3):
    if content[i] == 'X':
        if content[i + 1] == 'M':
            if content[i + 2] == 'A':
                if content[i + 3] == 'S':
                    forward_match.append(i)

backward_match = []
# check for backwards matches of XMAS
for i in range(len(content)-3):
    if content[i] == 'S':
        if content[i + 1] == 'A':
            if content[i + 2] == 'M':
                if content[i + 3] == 'X':
                    backward_match.append(i)

downward_match = []
# check for downwards matches of XMAS
for i in range(len(content)-3*row_length -1):
    if content[i] == 'X':
        if content[i + 1*row_length] == 'M':
            if content[i + 2*row_length] == 'A':
                if content[i + 3*row_length] == 'S':
                    downward_match.append(i)

upward_match = []
# check for upwards matches of XMAS

for i in range(len(content)-1, 3*row_length,-1):
    if content[i] == 'X':
        if content[i - 1*row_length] == 'M':
            if content[i - 2*row_length] == 'A':
                if content[i - 3*row_length] == 'S':
                    upward_match.append(i)
for i in range(len(content)-3*row_length -1):
    if content[i] == 'S':
        if content[i + 1*row_length] == 'A':
            if content[i + 2*row_length] == 'M':
                if content[i + 3*row_length] == 'X':
                    upward_match.append(i)

import itertools
d_r_diag_match = []
diag_range = range(136)
diag_range2 = range(141, 276)
diag_range3 = range(281, 416)
new_diag_range = list(itertools.chain(diag_range, diag_range2, diag_range3))

# create range to index for diagonal down right and diagonal up left
partial_range = range(137)
for i in range(1,138):
    x = 140*(i) + 1
    y = 140*(i) + 140 - 4
    partial_range = list(itertools.chain(partial_range, range(x,y)))

# check for down-right diagonal matches of XMAS
for i in partial_range:
    if content[i] == 'X':
        if content[i + 1*row_length + 1] == 'M':
            if content[i + 2*row_length + 2] == 'A':
                if content[i + 3*row_length + 3] == 'S':
                    d_r_diag_match.append(i)

# check for up-left diagnoal matches of XMAS
u_l_diag_match = []
for i in partial_range:
    if content[i] == 'S':
        if content[i + 1*row_length + 1] == 'A':
            if content[i + 2*row_length + 2] == 'M':
                if content[i + 3*row_length + 3] == 'X':
                    u_l_diag_match.append(i)

# create range to index for diagnoal down left and diagonal up right
r1 = range(3,140)
r2 = range(144, 281)
r3 = range(285, 422)
partial_range2 = range(3,140)
for i in range(1,137):
    x2 = 141*(i) + 3
    y2 = 141*(i) + 140
    partial_range2 = list(itertools.chain(partial_range2, range(x2,y2)))

# check for down-left diagnoal matches of XMAS
d_l_diag_match = []
for i in partial_range2:
    if content[i] == 'X':
        if content[i + 1*row_length - 1] == 'M':
            if content[i + 2*row_length - 2] == 'A':
                if content[i + 3*row_length - 3] == 'S':
                    d_l_diag_match.append(i)

# check for up-right diagnoal matches of XMAS
u_r_diag_match = []
for i in partial_range2:
    if content[i] == 'S':
        if content[i + 1*row_length - 1] == 'A':
            if content[i + 2*row_length - 2] == 'M':
                if content[i + 3*row_length - 3] == 'X':
                    u_r_diag_match.append(i)


print(len(forward_match))
print(len(backward_match))
print(len(downward_match))
print(len(upward_match))
print(len(d_r_diag_match))
print(len(d_l_diag_match))
print(len(u_l_diag_match))
print(len(u_r_diag_match))

part1_ans = len(forward_match) + len(backward_match) + len(downward_match) + len(upward_match) + len(d_l_diag_match) + len(d_r_diag_match) + len(u_l_diag_match) + len(u_r_diag_match)
print(part1_ans)"""

## Day 4 Start over using dictionary method
from itertools import product, chain
Point = tuple[int,int] # defining to simplify functions
Space = dict[Point, str] # defining to simplify functions

# function to create a dictionary. Each Letter has coordinates r and c
def lookup(lines: list[str]) -> Space:
    return{(r,c): char for r,row in enumerate(lines) for c,char in enumerate(row)}

# find XMAS in all directions.
def xmas(point: Point, space: Space) -> list[bool]:
    r,c = point
    directions = product((-1,0,1), repeat=2) # Gives a matrix for all directions
    word = list("XMAS") # Word to match
    return [[space.get((r+dr*n,c+dc*n)) for n in range(4)] == word for dr,dc in directions] #dr, dc are incremental direction, n is how many times we go in that direction

# Part one
def part_one(space: Space) -> int:
    return sum(chain.from_iterable(xmas(point, space) for point in space))

# Function to Find MAS/SAM in shape of X
def x_mas(point: Point, space: Space) -> bool:
    r,c = point
    direction = (-1,0,1) # only need diagonals now
    words = list("MAS"), list("SAM")
    return [space.get((r+d,c+d)) for d in direction] in words and [space.get((r+d,c-d)) for d in direction] in words

# Part two
def part_two(space: Space) -> int:
    return sum(x_mas(point,space) for point in space)


# Main function that calls other functions and prints answer
def day4() -> None:
    with open("day4/data.txt", "r") as file:
        lines = [l.strip() for l in file.readlines()]

    space = lookup(lines)
    print(space)

    print(part_one(space))
    print(part_two(space))

day4()