
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

class File:
    def __init__(self, _name: str, _size: int):
        self.name = _name
        self.size = _size

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

#def cd(pwd):