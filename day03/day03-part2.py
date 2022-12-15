# 2022 Advent of Code - Day 3 part 2
#
# given a file that represents the contents of a bunch of rucksacks... 
# each set of three lines represents a group of three ruck sacks
#  find the  item common to all three rucksacks in each group, 
# tally up priorities over all groups
#
# obviously some serious dependance on format of the data file... 
# must be a multiple of three lines, must have 1 element in common for each group of three, etc.

inputFileName = "day03-input-data.txt"
#inputFileName = "sample-data.txt"

# priority - returns priority number for a given item letter,
#   a=1, b=2, ... z=26, A=27, B=28, ... Z=52
#
# in: single character
# out:  priority according to above mapping
def priority(c):
    if c >= "a" and c <= "z":
        return ord(c)-ord('a')+1
    elif c >= "A" and c <= "Z":
        return ord(c)-ord('A')+1+26

prioritySum = 0
with open(inputFileName, 'r') as inputFile:
    while True:
        groupRucksacks = []
        #get three rucksacks for one group of elves
        for i in range (3):
            groupRucksacks.append(inputFile.readline().strip())
        #if one of those readlines came back empty we're done
        if "" in groupRucksacks:
            break
        print(groupRucksacks)
        #find common elements in 
        common = set(groupRucksacks[0])
        for rucksack in groupRucksacks[1:]:
            common=common.intersection(rucksack)
        #tally priorities
        for item in common:
            prioritySum = prioritySum + priority(item)

print(prioritySum)
