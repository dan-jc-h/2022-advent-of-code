# 2022 Advent of Code - Day 4 part 1 & 2
#
# Read pairs of ranges from file, we need to find if one range is entirely contained in the other.
# Using a set approach, find intersection, if intersection equals one of the original ranges (sets), 
# then one fully contains the other.
#
# Part 2 is a simple add on to sum up any overlaps at all.


inputFileName = "day04-input-data.txt"
#inputFileName = "day04-sample-data.txt"

rangesOverlapped = 0
rangesEnveloped = 0
with open(inputFileName, 'r') as inputFile:
    for line in inputFile:
        line=line.strip()
        #break line into sections
        section1,section2=line.split(',')
        #get ends of each section
        low1,high1=section1.split('-')
        low2,high2=section2.split('-')
        #build ranges (need the +1, because python)
        range1=range(int(low1),int(high1)+1)
        range2=range(int(low2),int(high2)+1)
        #find intersection
        common = set(range1).intersection(range2)
        #print(line , range1, range2, common)
        # for part2 - there's an overlap if common is not empty
        if common:
            rangesOverlapped = rangesOverlapped + 1
        # for part1 - if either range equals the intersection of the two ranges, one range is completely enveloped
        if set(range1)==common or set(range2)==common:
            rangesEnveloped = rangesEnveloped + 1

print(f'Part1: {rangesEnveloped} ranges where one completely envelopes the other.')
print(f'Part1: {rangesOverlapped} overlap.')
        