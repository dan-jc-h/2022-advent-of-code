# 2022 Advent of Code - Day 9 Part 2
#
# Ok - here we are dragging a whole rope around...

inputFileName = "day09-input-data.txt"
#inputFileName = "day09-sample-data.txt"
#inputFileName = "day09-sample2-data.txt"

class knot:
    """
    Represents a knot on a rope.  Contains a location and a link to the next knot.
    If the link to the next knot is None, then we are at the end of the rope.
    """
    def __init__(self,_location:tuple, _next) -> None:
        self.location=_location
        self.nextKnot=_next
    def __str__(self)-> str:
        return f'({self.location[0]},{self.location[1]}) {self.nextKnot.__str__()}'

def moveKnot(k1:knot,k2:knot):
    """Move a knot relative to another.  k1 is "fixed" and k2 moves in relation to it

    Args:
        k1 (knot): fixed knot
        k2 (knot): moving knot
    """
    # Rules are:
    # if k1 and k2 are on top of each other, don't move
    # if k1 and k2 are in adjacent locations, don't move
    # if k1 and k2 are NOT adjacent and are directly above or 
    #    beside each other (same row or column, not diagonal), then
    #    k2 moves 1 towards k1, along the row or column.
    # if k1 and k2 are NOT adjacent and are not in the same
    #    row or column, then T moves one diagonally
    # default is to stay still
    (k1x,k1y)=k1.location
    (k2x,k2y)=k2.location
    xMove=0
    yMove=0
    if k1.location==k2.location:
        #H is on top of T so newLocation is already set correctly
        pass
    elif abs(k1x-k2x)<=1 and abs(k1y-k2y)<=1:
        #H and T are adjacent
        pass
    elif k1y==k2y:
        #H and T separated, but in same row
        if k1x>k2x: # k1x-k2x is +
            xMove = +1
        if k2x>k1x: # k1x-k2x is -
            xMove = -1
    elif k1x==k2x:
        #H and T separated, but in same column
        if k1y>k2y: # k1x-k2x is +
            yMove = +1
        if k2y>k1y: # k1x-k2x is -
            yMove = -1
    else:
        #H and T separated, but in different colum and row
        if k1x>k2x: # k1x-k2x is +
            xMove = +1
        if k2x>k1x: # k1x-k2x is -
            xMove = -1
        if k1y>k2y: # k1x-k2x is +
            yMove = +1
        if k2y>k1y: # k1x-k2x is -
            yMove = -1
    # update location
    k2.location=(k2.location[0]+xMove,k2.location[1]+yMove)
    return 

def moveRope(rope:knot):
    """
    given that the first element on the rope has moved, move the
    remaining elements by walking down the rope and applying rules.   

    Args:
        rope (knot): the linked list of knots to move
    """
    # if nextKnot is None, then we are at the end and we can leave
    if rope.nextKnot is None:
        return
    else:
        #move the next knot
        moveKnot(rope,rope.nextKnot)
        #move the rest of the rope
        moveRope(rope.nextKnot)

def getTail(rope:knot)->knot:
    """Find the last knot in a rope (the one with a None nextKnot link)

    Args:
        rope (Knot): The head of the rope of knots

    Returns:
        knot: The last knot in the rope
    """
    if rope.nextKnot is not None:
        return getTail(rope.nextKnot)
    else:
        return (rope)

# create rope
ROPE_LENGTH = 10
rope = knot((0,0),None)
for i in range(ROPE_LENGTH-1):
    #add at head of rope (easier than wandering to the end)
    newKnot = knot((0,0),rope)
    rope = newKnot

# need to keep track of the unique places the tail goes... set is perfect for this.
whereHasTheTailBeen=set()

print("Starting Conditions:")
print(f'  Rope: {rope}')
whereHasTheTailBeen.add(getTail(rope).location)
print(f'  Places Tail has been: {whereHasTheTailBeen}')

# walk through the file executing commands as documented on the Advent of Code website
# <https://adventofcode.com/2022/day/9>
with open(inputFileName, 'r') as inputFile:
    for line in inputFile.readlines():
        command,count = line.split(' ')
        count=int(count)
        print("Command read from file:",command,", Count:", count)
        for i in range(count):
            if command == "U":
                print("  Head moving UP one.")
                rope.location=(rope.location[0],rope.location[1]+1)
            elif command == "D":
                print("  Head moving DOWN one.")
                rope.location=(rope.location[0],rope.location[1]-1)
            elif command == "L":
                print("  Head moving LEFT one.")
                rope.location=(rope.location[0]-1,rope.location[1])
            elif command == "R":
                print("  Head moving RIGHT one.")
                rope.location=(rope.location[0]+1,rope.location[1])
            else:
                #FIXME - make this an exception
                print("***PROBLEM")
                exit()
            #after each move of the head we have to move the rest of the rope            
            moveRope(rope)
            print(rope)
            #update where the tail has been
            whereHasTheTailBeen.add(getTail(rope).location)

print("Ending Conditions:")
print(f'  Rope: {rope}')
print(f'  Places Tail has been: {whereHasTheTailBeen}')
print(f'  Tail has been {len(whereHasTheTailBeen)} locations.')
