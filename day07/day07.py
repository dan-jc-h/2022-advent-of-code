# 2022 Advent of Code - Day 7 Part 1
#
# Tree exercise to simulate a file system

# Create a root dir
# Parse the input and build tree
#   - cd - changes the working directory
#   - ls - can ignore
#   - dir d, dir: create directory d and add it
#   - num fname, file: create and add it
#   - cd .. - change working dir to parent
#  Scan tree and get sum of all directories which do not exceed 100k bytes

from  day07lib import *
import re

inputFileName = "day07-input-data.txt"
#inputFileName = "day07-sample-data.txt"

# create the root directory, and set pwd (present working directory)
root = Dir(None, "/")
pwd = root

# parse the file, (heavy reliance on re here) and build tree
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
            print("*** UNRECOGNIZED INPUT - this is a problem and should be an exception")
        
# Lest see what we have!
print(showTree(root))

# get total of all subtrees with size less than 100000 - this is the requested data
print(sumOfTreesUnder100k(root))
