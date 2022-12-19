# 2022 Advent of Code - Day 7 Part 1 & Part 2
#
# Tree exercise to simulate a file system

# Create a root dir
# Parse the input and build tree
#   - cd - changes the working directory
#   - ls - can ignore
#   - dir d, dir: create directory d and add it
#   - num fname, file: create and add it
#   - cd .. - change working dir to parent
#  
# Part 1 - Scan tree and get sum of all directories which do not exceed 100k bytes
#
# Part 2 - find the size of the smallest directory to delete, to free up space for an update.

from  day07lib import *
import re

inputFileName = "day07-input-data.txt"
#inputFileName = "day07-sample-data.txt"

# create the root directory, and set pwd (present working directory)
root = Dir(None, "/")
pwd = root

# parse the file, (heavy reliance on re here) and build tree
# this is pretty fragile
with open(inputFileName, 'r') as inputFile:
    for line in inputFile.readlines():
        print(line.strip())
        if re.match("\$ cd \.\.",line):
            # cd ..
            print("cd .. - change pwd to parent")
            pwd = pwd.parent
        elif re.match("\$ cd /",line):
            # cd /
            print("cd - change pwd root")
            pwd = root
        elif re.match("\$ cd",line):
            #cd <dir>
            dirName = (line.strip().split(" "))[2]
            print(f'cd - change to {dirName}')
            pwd = findDir(dirName, pwd)
        elif re.match("\$ ls",line):
            #ls is ignorable
            pass
        elif re.match("dir",line):
            fileName = (line.strip().split(" "))[1] # file name
            print(f'dir - create dir {fileName}')
            pwd.dirs.append(Dir(pwd,(line.strip().split(" "))[1]))
        elif re.match("[0-9]", line):
            fileSize,fileName=line.strip().split()
            print(f'file - create file {fileName}, {fileSize} bytes')
            pwd.files.append(File(fileName,int(fileSize)))
        else:
            #FIXME - this should probably throw an exception
            print("*** UNRECOGNIZED INPUT - this is a problem")
        
# Lets see what we have!
print(showTree(root))

# get total of all subtrees with size less than 100000 - this is the requested data for Part 1
print("Part 1: Sum of all directories with less than 100,000 bytes in them:")
print(sumOfTreesUnder100k(root))

# part 2
# Need to calculate space needed to apply update, then find the size of the 
# smallest directory that you can delete to make enough space available.

TOTAL_SPACE = 70000000
SPACE_REQUIRED_FOR_UPDATE = 30000000
totalSpaceUsed = treeSize(root)
freeSpace = TOTAL_SPACE - totalSpaceUsed
needToFree = SPACE_REQUIRED_FOR_UPDATE - freeSpace

print('\n**Part 2 **\n')
print(f'Total space on device:     {TOTAL_SPACE:>8}')
print(f'Space in use:              {totalSpaceUsed:>8}')
print(f'Free space:                {freeSpace:>8}')
print(f'Space required for update: {SPACE_REQUIRED_FOR_UPDATE:>8}')
print(f'Must free at least:        {needToFree:>8}')

# generate a list of the size of all directories
spaceList = makeSpaceList(root)
# Delete list elements which don't which are too small to free up enough space.
# There's probably a better way to do this.  Want to delete items under a specific size, by
# going *backwards* through the array you avoid messing up indexes.
for i in range(len(spaceList)-1,-1,-1):
    if spaceList[i] < needToFree:
        del spaceList[i]
spaceList.sort()
print("\n Part 2: Size of smallest directory to delete to free up space for update:")
print(spaceList[0])

    