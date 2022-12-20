# Day08 Part 1 & 2
# 
# Part 1
#
# 1. Read the file representing the forest into an np array.
# 2. Create a "visibility array" and set all edges to visible
# 3. iterate over all other trees checking to see it that tree 
#    can be seen from all four edges or not.
#
# Part 2
# 4. determine the highest scenic score

import numpy as np


inputFileName = "day08-input-data.txt"
#inputFileName = "day08-sample-data.txt"

def howFarToEqualOrGreaterValue(val:int,ar:np.ndarray)->int:
    """How far do we need to walk along an array to get to an equal or greater value

    Args:
        val (int): a value
        ar (np.ndarray): a list of value

    Returns:
        int: how far along the array we need to go to get to an array value equal to or greater than val
    """
    i=0
    for test in ar:
        i = i +1
        if test >= val:
            return i
    # for to the end of the array - so we can see the entire length
    return len(ar)

def scenicScore(i:int,k:int,forest:np.ndarray)->int:
    """Calculate Scenic Score for a tree in the forest

    Scenic score is how far you can see from the tree 
    in each direction, before your view is blocked by 
    a tree that is the same height or taller.  All four 
    distances (one for each direction) are multiplied 
    together, to get a final Scenic Score for that tree.

    Args:
        i (int): x-index of tree
        k (int): y-index of tree
        forest (np.ndarray): 2D array representing the forest,
                             each element is the height of a tree 

    Returns:
        int: The Scenic score for the tree at [i,j]
    """
    print(f'Calculating Scenic Score for tree at [{i},{j}], height={forest[i,j]}')
    westerlyTrees=forest[i,:j]
    # use the array[::-1] to pass a reversed view of the array
    wDist = howFarToEqualOrGreaterValue(forest[i,j],westerlyTrees[::-1])
    print(f'  W:{westerlyTrees} Can see {wDist} units.')
    easterlyTrees=forest[i,j+1:]
    eDist = howFarToEqualOrGreaterValue(forest[i,j],easterlyTrees)
    print(f'  E:{easterlyTrees} Can see {eDist} units.')
    northerlyTrees=forest[:i,j]
    nDist = howFarToEqualOrGreaterValue(forest[i,j],northerlyTrees[::-1])
    print(f'  N:{northerlyTrees} Can see {nDist} units.')
    southerlyTrees=forest[i+1:,j]
    sDist = howFarToEqualOrGreaterValue(forest[i,j],southerlyTrees)
    print(f'  S:{southerlyTrees} Can see {sDist} units.')

    return  (wDist * eDist * nDist * sDist)

def amIVisible(height:int,trees:np.ndarray)->bool:
    """Determine if a tree is visible

    A tree is visible if all the trees in the sight line to it are 
    shorter.  If any tree is as tall, or taller, then the tree
    can't be seen.

    Args:
        height (int): height of the subject tree
        trees (np.ndarray): a 1D array of tree heights along the sight line

    Returns:
        bool: True=Tree can be seen.  False=Tree cannot be seen
    """
    #print(f'Checking visibility: height: {height}, trees: {trees}')
    highestBlockingTree = trees.max()
    #print(highestBlockingTree)
    if height > highestBlockingTree:
        #print("    Visible.")
        return True
    else:
        #print("    Not Visible.")
        return False

# Read the array into a np Array
forest=np.genfromtxt(inputFileName, delimiter=1, dtype=int)
print(f'Forest:\n{forest}')

# create the visibility array
visibility = np.zeros(forest.shape,dtype=int)

# set edges of visibility array to 1 - these are always visible
visibility[0,:]=1
visibility[:,0]=1
visibility[visibility.shape[0]-1,:]=1
visibility[:,visibility.shape[1]-1]=1
#print(visibility)

# iterate over each tree, starting just inside the edge, 
# for each tree consider the slice going from the tree to
# the N, S, E and W.  if an intervening tree is equal to 
# or higher than the subject tree it cannot be seen.  We 
# can use the numpy max fn to find the highest tree in the
# path
#
# If a tree is visible from any direction, set the flag
# in the visibility matrix and we are done, if the tree
# is not visible from another direction it doesn't make
# it invisible from this direction.
for i in range(1,(forest.shape)[0]-1):
    for j in range(1,(forest.shape)[1]-1):
        #print(f'[{i}][{j}]={forest[i,j]}')
        westerlyTrees=forest[i,:j]
        if amIVisible(forest[i,j],westerlyTrees) and visibility[i][j]==0:
            visibility[i,j]=1
        easterlyTrees=forest[i,j+1:]
        if amIVisible(forest[i,j],easterlyTrees) and visibility[i][j]==0:
            visibility[i,j]=1
        northerlyTrees=forest[:i,j]
        if amIVisible(forest[i,j],northerlyTrees) and visibility[i][j]==0:
            visibility[i,j]=1
        southerlyTrees=forest[i+1:,j]
        if amIVisible(forest[i,j],southerlyTrees) and visibility[i][j]==0:
            visibility[i,j]=1

#print(forest)
#print(visibility)
print(f'Part 1, number of trees visible: {visibility.sum()}')

# determine maximum scenic score
maxScenicScore = 0
MaxI=0
MaxJ=0
for i in range((forest.shape)[0]):
    for j in range((forest.shape)[1]):
        print(i,j)
        thisTreesScore = scenicScore(i,j,forest)
        if thisTreesScore>maxScenicScore:
            maxScenicScore=thisTreesScore
            MaxI=i
            MaxJ=j

print(f'Part 2: Max Scenic Score is: {maxScenicScore}.  This tree is at [{MaxI},{MaxJ}]')
