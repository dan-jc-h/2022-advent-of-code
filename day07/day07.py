# Create a root dir
# Parse the input
#   - cd - changes the working directory
#   - ls - can ignore
#   - dir d, dir: create directory d and add it
#   - num fname, file: create and add it
#   - cd .. - change working dir to parent
#  
# 
from  day07lib import *
import re

inputFileName = "day07-sample-data.txt"

root = Dir(None, "/")
pwd = root

with open(inputFileName, 'r') as inputFile:
    for line in inputFile.readlines():
        print(line.strip())
        if re.match("\$ cd \.\.",line):
            print("cd .. - change pwd to parent")
        elif re.match("\$ cd",line):
            print(f'cd - change to {(line.strip().split(" "))[2]}')
        elif re.match("\$ ls",line):
            #print("ls - skip")
        elif re.match("dir",line):
            print(f'dir - create dir {(line.strip().split(" "))[1]}')
        elif re.match("[0-9]", line):
            fs,fn=line.strip().split()
            print(f'file - create file {fn}, {fs} bytes')
        else:
            print("*** UNRECOGNIZED INPUT")
        
        
