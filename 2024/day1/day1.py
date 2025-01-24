# Day 1 of Advent of Code 2024

## PART 1
col1 = []
col2 = []

with open("day1/data.txt", "r") as file: # Open data file
    for line in file:
        left, right = line.strip().split() # strip any spaces and split each line into 2 
        col1.append(int(left)) # append column 1 with all the data on the left, convert to integer
        col2.append(int(right)) # append column 2 with all the data on the right, convert to integer

col1.sort() # sort ascending
col2.sort() # sort ascending

diff = [x - y for x,y in zip(col1, col2)] # subtract values of each pair from col1 and col2
answer = [sum(abs(num) for num in diff)] # sum of absolute values of all the differences in pairs
print(answer)

## PART 2

# Steps: iterate through each element in col1. Find how many times that ocurrs in col2. Calculate sim score by multiplying value times
# number of ocurrences. sum the similarity score
scores = [col2.count(num)*num for num in col1]
answer2 = sum(scores)
print(answer2)