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

inputFileName = "day07-input-data.txt"
#inputFileName = "day07-sample-data.txt"

root = Dir(None, "/")
pwd = root

with open(inputFileName, 'r') as inputFile:
    for line in inputFile.readlines():
        print(line.strip())
        if re.match("\$ cd \.\.",line):
            print("cd .. - change pwd to parent")
            pwd = pwd.parent
        elif re.match("\$ cd /",line):
            print("cd - change pwd root")
            pwd = root
        elif re.match("\$ cd",line):
            dn = (line.strip().split(" "))[2]
            print(f'cd - change to {dn}')
            pwd = findDir(dn, pwd)
        elif re.match("\$ ls",line):
            #print("ls - skip")
            pass
        elif re.match("dir",line):
            fn = (line.strip().split(" "))[1]
            print(f'dir - create dir {fn}')
            pwd.dirs.append(Dir(pwd,(line.strip().split(" "))[1]))
        elif re.match("[0-9]", line):
            fs,fn=line.strip().split()
            print(f'file - create file {fn}, {fs} bytes')
            pwd.files.append(File(fn,int(fs)))
        else:
            print("*** UNRECOGNIZED INPUT - this is a problem")
        
print(showTree(root))

# get total of all subtrees with size less than 100000
print(sumOfTreesUnder100k(root))
