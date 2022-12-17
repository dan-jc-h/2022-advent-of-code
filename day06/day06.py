# 2022 Advent of Code - Day 6 parts 1&2
#
# Step through a string checking preceding 4 chars to see if they are unique, 
# if you find a unique group you are done.
#
# Part 2 - just a different value for MARKER_LENGTH

inputFileName = "day06-input-data.txt"
#inputFileName = "day06-sample-data.txt"

# uniqueCharsInString - return True if all the characters in a string are unique
#
# This uses the tradition python trick of turning the sting into a list, then comparing the length 
# of the list to a set of the same list.  If the lengths are the same the elements are unique.
#
def uniqueCharsInString(str):
    return len(list(str)) == len(set(list(str)))

# markerLength is 4 for part 1, 14 for part 2.
MARKER_LENGTH = 14 

# This reads multiple lines of input instead of just one
with open(inputFileName, 'r') as inputFile:
    for line in inputFile.readlines():
        for i in range(MARKER_LENGTH,len(line)):
            subStr = line[i-MARKER_LENGTH:i]
            #print(f'{i}: [{i-markerLength}:{i}] str: "{subStr}" unique: {uniqueCharsInString(subStr)}')
            if uniqueCharsInString(subStr):
                break
        print(i)

        