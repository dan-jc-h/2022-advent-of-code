# 2022 Advent of Code - Day 5 Part 2
#
# This is pretty ugly and a lot depends on how worried you want to be about the input data.  
# The applying part is parsing the stack depiction at the start of the data file, can cranes 
# have numbers greater than 10, can they even alpha names, not numbers.
#
# In the spirit of not burning too much time on this the details are (as always) in the code.
#
# Here's some discussion of the stacks data structure.  It's a list of lists...
#
#    [ stackname1 (int), [stack1(list of chars)]],
#    [ stackname2 (int), [stack2(list of chars)]],
#    ... etc.
#
#    e.g.
#
#         [1, ['Z', 'N']],
#         [2, ['M', 'C', 'D']],
#         [3, ['P']]]
#
# I decided to go with storing an explicit stackname (number) instead of relying solely on 
# position in the list, because there no indication that the cranes are numbered contiguously 
# or even starting at 1 etc.
#
# Part 2 is a change to how boxes get moved.
#

import re

inputFileName = "day05-input-data.txt"
#inputFileName = "day05-sample-data.txt"

# Given the name of a stack (an int), find the corresponding stack in the stacks structure 
def getStackByNumber(stacks,n):
    for s in stacks:
        if s[0] == n:
            return s[1]

# return a string that gives is a list of the top boxes on each stack
def topBoxes(stacks):
    topBoxes=""
    for i in range(1,len(stacks)+1):
        topBoxes=topBoxes+getStackByNumber(stacks,i).pop()
    return topBoxes

# main
# 
# read the datafile, first read the stack depiction and set up stacks structure, 
# then read/process the commands.
#
with open(inputFileName, 'r') as inputFile:
    #first get the data depicting the stacks
    stackData=[]
    while True:
        line=inputFile.readline()
        if line == "\n":
            break
        stackData.append(line.strip('\n'))
    #now we "rotate" the stack data into text representation of stacks
    stacks=[]
    for i in range(len(stackData[0])):
        stack=""
        for j in range(len(stackData)-1,-1,-1):
            #print(f'[{i}],[{j}],"{stackData[j][i]}"')
            stack = stack + stackData[j][i]
        # we are only interested in strings that start with a number, rest is decoration
        if stack[0]>='0' and stack[0]<='9':
            # we have a stack!  e.g.  4ABX, the 4 is the stackNumber and the ABX is the stackBody
            # need to strip off the stack number
            stackNumber = re.match("\d+",stack,re.ASCII).group(0)
            # and the stack body
            stackBody = re.search("\D+",stack,re.ASCII).group(0).strip()
            # put these together and add to the stacks
            stacks.append([int(stackNumber),list(stackBody)])
    print("Stack Data read.")
    print(stacks)
    # Now read the commands.  Parse and apply movements to stacks
    # commands follow the format: "move n from a to b" 
    # where n is number of boxes, and a is source stack, and b is destination stack
    while True:
        line=inputFile.readline().strip()
        if not line:
            break
        print(line)
        tokens=re.findall("\d+",line)
        # tokens will be nMoves, source stack, destination stack
        nBoxes=int(tokens[0])
        fromStackNumber=int(tokens[1])
        toStackNumber=int(tokens[2])
        fromStack=getStackByNumber(stacks,fromStackNumber)
        toStack=getStackByNumber(stacks,toStackNumber)
        # execute moves - this is where the part 1 code and part 2 code differ
        # part 2 move: move a sub array from source to dest, then del source subarray
        movingBoxes = fromStack[-1-(nBoxes-1):]
        print(f'{fromStack} -> <{movingBoxes}> -> {toStack}')
        toStack = toStack.extend(movingBoxes) # yeah...extend, not append... 
        del fromStack[-1-(nBoxes-1):]
        print(stacks)
        print(" - - -")
print("Final stacks:\n")
print(stacks)
print(f'\nTop Boxes: {topBoxes(stacks)}')




    
