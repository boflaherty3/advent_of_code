import re
from collections import defaultdict

## Open data dile and separate into rules and updates
with open("day5/data.txt", "r") as file:
    rules,updates = file.read().strip().split('\n\n')
    int_rules = []
    for line in rules.split('\n'):
        a,b = line.split("|")
        int_rules.append((int(a),int(b)))
    updates = [list(map(int, line.split(','))) for line in updates.split("\n")]

# function to see if a given update of pages follows rules for part 1
def follows_rules(update):
    pages_dict = {}
    for i,num in enumerate(update):
        pages_dict[num] = i

    for a,b in int_rules:
        if a in pages_dict and b in pages_dict and not pages_dict[a] < pages_dict[b]:
            return False, 0 # if the nums from rules are both in the update, a must come before b. If not, return false, 0
    return True, update[len(update)//2] # if it follows rules, return True and the middle value

ans = 0
bad_updates = [] # in case we need these ones
for update in updates:
    good_updates, middle = follows_rules(update)
    if good_updates:
        ans += middle # add middle value to ongoing sum
    if not good_updates:
        bad_updates.append(update)
print(ans)

### Part 2
# Bubble sort function to sort the updates that aren't in the correct order
def bubble_sort(update):
    while True:
        is_sorted = True
        for i in range(len(update)-1):
            # check if out of order. If (next value in update, current value) is in rules, they should be flipped
            if (update[i+1], update[i]) in int_rules:
                is_sorted = False
                update[i], update[i+1] = update[i+1], update[i]

        if is_sorted:
            return update

ans = 0

# iterate through updates and if its already in order, skip. If not, bubble sort them into order and sum middle values
for update in updates:
    if follows_rules(update)[0]:
        continue
    sequence = bubble_sort(update)
    ans += sequence[len(sequence)//2]

print(ans)
