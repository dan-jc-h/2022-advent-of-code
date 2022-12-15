# 2022 Advent of Code - Day 3 part 1
#
# given a file that represents the contents of a bunch of rucksacks, inspect each 
# line (rucksack), first half of each line is compartment 1, second half 
# compartment 2.  find items in common between compartments and tally up priorities

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
    for rucksack in inputFile:
        #get rucksack
        rucksack=rucksack.strip()
        #split into compartments 
        compartment1=rucksack[:int(len(rucksack)/2)]
        compartment2=rucksack[int(len(rucksack)/2):]
        #find common elements using set intersection
        common = set(compartment1).intersection(set(compartment2))
        if common is not None:
            for x in common:
                #print(f'{x}: {priority(x)}')
                #Add up priorities
                prioritySum = prioritySum + priority(x)

print(prioritySum)
