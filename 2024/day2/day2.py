## DAY 2
data = [] # initial data
new_data = [] # data after manipulation and convert to integers

with open("day2/data.txt", "r") as file: # read in data from filr
    content = file.readlines()
    for line in range(len(content)):
        data.append(content[line].strip().split())

for line in range(len(data)):
    int_data = [int(entry) for entry in data[line]] # convert data to integers
    new_data.append(int_data)

results = [] # initialize results

for sets in range(len(new_data)):
    my_list = new_data[sets]
    diff = [my_list[i] - my_list[i-1] for i in range(1, len(my_list))] # see if numbers are increasing or decreasing by taking diff
    case1 = [all(diffs > 0 for diffs in diff) or all(diffs < 0 for diffs in diff)] # case 1, if all negative or all positive, then they're all incr or decr so safe
    case2 = [all(abs(diffs) > 0 for diffs in diff) and all(abs(diffs) <= 3 for diffs in diff)] # case 2, the change must be between 1 and 3
    result = [True if case1[0] == True and case2[0] == True else False] # return true if case 1 & 2 are true, otherwise false
    results.append(result)

results_int = [int(results[item][0]) for item in range(len(results))] # convert to integers
print(sum(results_int)) # sum the number of 1's (trues) to see how many are safe

## PART 2
unsafe_indices = [i for i in range(len(results_int)) if results_int[i] == 0] #find the indices for the unsafe levels
unsafe_lists = [new_data[k] for k in range(len(unsafe_indices))] # list of the levels that are unsafe

count = 0 # initialize count of lists that will be now safe

for lists in range(len(unsafe_lists)):
    sample_list = unsafe_lists[lists] # the list to be evaluated
    for i in range(len(sample_list)): # loop through the list, remove each number and see if the level will pass
        popped_value = sample_list.pop(i) # remove a report
        sample_diff = [sample_list[i] - sample_list[i-1] for i in range(1, len(sample_list))] # take diff with a report removed
        sample_case1 = [all(diffs > 0 for diffs in sample_diff) or all(diffs < 0 for diffs in sample_diff)] # case 1
        sample_case2 = [all(abs(diffs) > 0 for diffs in sample_diff) and all(abs(diffs) <= 3 for diffs in sample_diff)] #case 2
        sample_result = [True if (sample_case1[0] == True and sample_case2[0] == True) else False] # get result
        if sample_result == [True]:
            count = count + 1 # increase count if true, break so we don't double count
            break
        sample_list.insert(i, popped_value) # add report back into level

print(count) # count of new safe levels
print(count + sum(results_int)) # add to exisitng safe levels