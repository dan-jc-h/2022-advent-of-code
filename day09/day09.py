# 2022 Advent of Code - Day 9 Part 1
#
# Game plan:
# 1. start Head and Tail at locations 0,0
# 2. read the file line by line
# 3. Move head step by step (one command may send you many steps)
# 4. update Tail location with each move of Head
# 5. record where Tail is
# 6. report how many distinct locations the Tail visited

inputFileName = "day09-sample-data.txt"

class RopeEnd:
    def __init__(self,_location:tuple) -> None:
        self.location=_location
    def __str__(self)-> str:
        return f'({self.location[0]},{self.location[1]})'

def followHead(h:RopeEnd,t:RopeEnd)-> tuple:
    """calculate new location for the tail of a rope to move to

    Args:
        h (RopeEnd): head of rope
        t (RopeEnd): tail or rope

    Returns:
        tuple: new location for head of rope
    """
    (hx,hy)=h.location
    (tx,ty)=t.location
    # if head and tail are on top of each other, don't move
    # if head and tail are in adjacent locations, don't move
    # if head and tail are NOT adjacent and are directly above or 
    #    beside each other (same row or column, not diagonal), then
    #    tail moves 1 towards head, along the row or column.
    # if head and tail are NOT adjacent and are not in the same
    #    row or column, then T moves one diagonally


head = RopeEnd((0,0))
tail = RopeEnd((0,0))
whereHasTheTailBeen={}

print("Starting Conditions:")
print(f'  Head is here: {head}')
print(f'  Tail is here: {tail}')
print(f'  Places Tail has been: {whereHasTheTailBeen}')

with open(inputFileName, 'r') as inputFile:
    for line in inputFile.readlines():
        command,count = line.split(' ')
        count=int(count)
        print("Command read from file:",command,", Count:", count)
        for i in range(count):
            if command == "U":
                print("  Head moving UP one.")
                head.location=(head.location[0],head.location[1]+1)
            elif command == "D":
                print("  Head moving DOWN one.")
                head.location=(head.location[0],head.location[1]-1)
            elif command == "L":
                print("  Head moving LEFT one.")
                head.location=(head.location[0]-1,head.location[1])
            elif command == "R":
                print("  Head moving RIGHT one.")
                head.location=(head.location[0]+1,head.location[1])
            else:
                #FIXME - make this an exception
                print("***PROBLEM")
                exit()            
            print(f'Head now at : {head}')
            tail.location=followHead(head,tail)



print("Ending Conditions:")
print(f'  Head is here: {head}')
print(f'  Tail is here: {tail}')
print(f'  Places Tail has been: {whereHasTheTailBeen}')

        
