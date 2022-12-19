# 2022 Advent of Code - Day 7 - Module

# Directory class, represents a directory with a name, parent link, an array of file and an array of subdirs
class Dir:
    def __init__(self, _parent, _name: str):
        self.parent = _parent
        self.files = []
        self.dirs = []
        self.name = _name
    def __str__(self):
        if self.parent is None:
            parentName = "<None>"
        else:
            parentName = self.parent.name
        dirNames = ""
        for d in self.dirs:
            dirNames = dirNames + d.name + ","
        fileNames = ""
        for f in self.files:
            fileNames = fileNames + f.name +","
        return f'[{self.name}] parent:{parentName}, dirs:{dirNames} files:{fileNames}'


# File class, represents a file with a name, and size
class File:
    def __init__(self, _name: str, _size: int):
        self.name = _name
        self.size = _size


# indented string representation of a tree or directories and files, just makes it easier to visualize
INDENT = 0
INDENT_SIZE = 4
def showTree(root: Dir) -> str:
    global INDENT
    output = " " * INDENT_SIZE * INDENT + str(root)
    INDENT = INDENT + 1
    for n in root.dirs:
        output = output + '\n' + showTree(n)
    INDENT = INDENT - 1
    return output

def ls(n:Dir) -> str:
    output = ""
    for d in n.dirs:
        output = output + "dir " + d.name + "\n"
    for f in n.files:
        output = output + str(f.size) + " " + f.name + "\n"
    return output

# Find a directory, by name in the list of directories, below a directory
#   input: dn: the name of the directory you are looking for
#   input: dir: the directory to look in
#   return: the directory we are seeking
#
def findDir(dn:str,dir:Dir)-> Dir:
    for d in dir.dirs:
        if dn == d.name:
            return d

# treeSize - add up all the file sizes in a tree
def treeSize(dir:Dir)->int:
    totalSize = 0
    #first add up sizes of files in this dir...
    for f in dir.files:
        totalSize=totalSize+f.size
    #... then add sizes of all files below this directory
    for d in dir.dirs:
        totalSize=totalSize+treeSize(d)
    print(f'Treesize at {dir.name}: {totalSize} bytes')
    return totalSize

#
# sumOfTreesUnder100k - add up the amount of space used in directories, 
# BUT ONLY IF THE SIZE IS LESS THAN 100,000
#
def sumOfTreesUnder100k(dir:Dir)->int:
    sum = 0
    if treeSize(dir)<=100000:
        sum=sum+treeSize(dir)
    for d in dir.dirs:
        sum=sum+sumOfTreesUnder100k(d)
    print(f"{dir.name}:{sum}")
    return(sum)
