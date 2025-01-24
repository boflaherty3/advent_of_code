##DAY 3 PART 1
import re
with open("day3/data.txt", "r") as file:
    content = file.read()
#print(content)
p = re.compile("mul\(\d{1,3},\d{1,3}\)") # compile phrase to search for "mul(XXX,XXX)"
result = p.findall(content) # find all matches of regular expression in the text file
#print(result)
p2 = re.compile("\d{1,3},\d{1,3}") # compile phrase to search for "XXX,XXX"
result_wo_mul = [p2.findall(result[i]) for i in range(len(result))] # find all results of "XXX,XXX" without the "mul"
#print(result_wo_mul)
split_results = [result_wo_mul[i][0].split(",") for i in range(len(result_wo_mul))] #split all numbers by the comma separating them
mult = [int(split_results[i][0]) * int(split_results[i][1]) for i in range(len(split_results))] # multiply first and second value of each pair and add to list
final_answer = sum(mult) # sum all of the multiplications in the list
print("Part 1: {}".format(final_answer))

## PART 2
removed_sum = [] # initialize
split_by_dont = re.split('(?<=don\'t\(\))', content) # split text file on don't()
for split in range(1, len(split_by_dont)): # omit first string since no Don't's before it
    split_by_do = re.split('(?<=do\(\))', split_by_dont[split]) # split it on the do()s
    """ the following section is the same method as above to find the Mul's and then take numbers and multiply them and sum the results"""
    p3 = re.compile("mul\(\d{1,3},\d{1,3}\)") # compile phrase to search for "mul(XXX,XXX)"
    remove_muls = p.findall(split_by_do[0]) # find all matches after don't and before do
    p4 = re.compile("\d{1,3},\d{1,3}") # compile phrase to search for "XXX,XXX"
    result_wo_mul2 = [p4.findall(remove_muls[i]) for i in range(len(remove_muls))] # find all results of "XXX,XXX" without the "mul"
    split_results_part2 = [result_wo_mul2[i][0].split(",") for i in range(len(result_wo_mul2))] #split all numbers by the comma separating them
    mult_removed = [int(split_results_part2[i][0]) * int(split_results_part2[i][1]) for i in range(len(split_results_part2))] # multiply first and second value of each pair and add to list
    removed_sum.append(sum(mult_removed)) # sum all of the multiplications in the list and append to list

part2_answer = final_answer - sum(removed_sum) # subtraqct the don't() mul's from original total
print("Part 2: {}".format(part2_answer))