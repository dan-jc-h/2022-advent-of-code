# 2022 Advent of Code - Day 7 - Module

class Dir:
    """
    Represents a directory entry in a file tree

    Attributes:
        parent - parent Dir
        name - name of Dir
        files - an array of File objects
        dirs - an array of Dirs (sub directories)
    """
    def __init__(self, _parent, _name: str):
        """
        Create Dir

        Args:
            _parent (Dir): Parent Dir
            _name (str): Name
        """
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

class File:
    """
    Represents a file in a file system, with a name, and size.
    """
    def __init__(self, _name: str, _size: int):
        self.name = _name
        self.size = _size

INDENT = 0
INDENT_SIZE = 4
def showTree(root: Dir) -> str:
    """
    Returns a string with a (somewhat) readable representation of the file system

    Args:
        root (Dir): Starting dir

    Returns:
        str: readable output
    """
    global INDENT
    output = " " * INDENT_SIZE * INDENT + str(root)
    INDENT = INDENT + 1
    for n in root.dirs:
        output = output + '\n' + showTree(n)
    INDENT = INDENT - 1
    return output

def ls(dir:Dir) -> str:
    """
    lists contents of a directory

    Args:
        dir (Dir): Directory that you want to see contents of

    Returns:
        str: list of files and dirs in a directory
    """
    output = ""
    for d in dir.dirs:
        output = output + "dir " + d.name + "\n"
    for f in dir.files:
        output = output + str(f.size) + " " + f.name + "\n"
    return output

def findDir(dn:str,dir:Dir)-> Dir:
    """
    Finds a sub-directory by name in a directory (does not recurse)

    Args:
        dn (str): name of the directory being sought
        dir (Dir): directory to look in

    Returns:
        Dir: The directory being sought
    """
    for d in dir.dirs:
        if dn == d.name:
            #FIXME - this really needs some safe return or exception if the directory isn't found
            return d

def treeSize(dir:Dir)->int:
    """
    calculate the size, in bytes, of a sub-tree

    Args:
        dir (Dir): starting directory

    Returns:
        int: total space used, in bytes
    """
    totalSize = 0
    #first add up sizes of files in this dir...
    for f in dir.files:
        totalSize=totalSize+f.size
    #... then add sizes of all files below this directory
    for d in dir.dirs:
        totalSize=totalSize+treeSize(d)
    #print(f'Treesize at {dir.name}: {totalSize} bytes')
    return totalSize

#
# sumOfTreesUnder100k - add up the amount of space used in directories, 
# BUT ONLY IF THE SIZE IS LESS THAN 100,000
#
def sumOfTreesUnder100k(dir:Dir)->int:
    """
    add up space used by directories that use less than 100k bytes - weird requirement!

    This is to satisfy part 1 of the exercise

    Args:
        dir (Dir): starting dir

    Returns:
        int: space used by directories which do not exceed 100 k in size
    """
    sum = 0
    if treeSize(dir)<=100000:
        sum=sum+treeSize(dir)
    for d in dir.dirs:
        sum=sum+sumOfTreesUnder100k(d)
    #print(f"{dir.name}:{sum}")
    return(sum)

def makeSpaceList(dir:Dir) -> list:
    """
    Create a list of the sizes of all directories in the file tree

    Args:
        dir (Dir): starting directory (search below this directory)

    Returns:
        List of integers: The list of sizes of directories.
    """
    spaceList = []
    spaceList.append(treeSize(dir))
    for d in dir.dirs:
        #print(d.name)
        spaceList.extend(makeSpaceList(d))
    return spaceList
