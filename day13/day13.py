# 2022 Advent of Code - Day xx
#   https://adventofcode.com/2022/day/xx
#
# Part 1 - read pairs of data packets and determine, 
# using some ugly rules, if they are in the right order or not.
#
# Part 2 -

def comparePackets(left:list,right:list)->bool:
    print(f'  Compare {left} vs {right}')
    if isinstance(left,int):
        left=[left]
    if isinstance(right,int):
        right=[right]
    # both sides will be lists, need to walk through elements
    while left:
        if len(left)==0: # we've run out of input on the left
            print("    out of data on left -> True")
            return True
        else:
            l=left[0]
        if len(right)==0: # we've run out of input on the right
            print("    out of data on left -> True")
            return False
        else:
            r=right[0]
        if isinstance(l,int) and isinstance(r,int):
            print(f'    Compare {l} vx {r}')
            if l < r:
                print("    left < right -> True")
                return True
            return
        elif isinstance(l,int) and isinstance(r,list):
            return comparePackets([l],right)
        elif isinstance(l,list) and isinstance(r,int):
            return comparePackets(left,[r])
        # we must be comparing two lists
        else:
            return comparePackets(l[0],r[0]) or comparePackets(left[1:],right[1:])

def comparePackets2(left:list,right:list)->bool:
    """Compares two packets according to rules at https://adventofcode.com/2022/day/xx.
    Args:
        left (list): packet
        right (list): packet
    Returns:
        bool: True if packets are in order, False otherwise
    """
    # left and right are always lists,
    # condition 1: one may be a null list
    # condition 2: one may be a single integer in a list
    # condition 3: both items are single integers in a list
    # condition 4: both items are lists, in which case, compare 1st elements, then second etc.
    
    print(f'Compare {left} vs {right} ')
    #condition 1: is either null?  If left is null, return True, if right is null return False
    if not left:
        return True
    if not right:
        return False
    # we may have been handed ints or lists.  If we were handed ints, 
    # or a list with just one int, assign that value to a side.  
    # If we got a list, assign first element to a side.
    if isinstance(left,int):
        l = left
    else:
        l = left[0]
    if isinstance(right,int):
        r = right
    else:
        r = right[0]
    
    #condition 3: both are single integers, is left is smaller, True, else rest of list
    if isinstance(l,int) and isinstance(r,int):
        if l < r:
            return True
        elif r < l:
            return False
        else:
            if isinstance(left,list) and isinstance(right,list):
                return comparePackets2(left[1:],right[1:])
            else:
                return

    #condition 2: one side is an integer - convert the integer to a list which contains that integer as its only value, then retry the comparison.
    if isinstance(l,int) and isinstance(r,list):
        return comparePackets2([l],r[0])
    if isinstance(l,list) and isinstance(r,int):
        return comparePackets2(l[0],[r])

    #condition 4: both are lists - compare element by element
    return comparePackets2(l,r) and comparePackets2(left[1:],right[1:])

def comparePackets3(left:list,right:list)->bool:
    # left and right are always lists,
    # condition 1: one (or both) may be a null list
    # condition 2: one may be a single integer in a list
    # condition 3: both items are single integers in a list
    # condition 4: both items are lists, in which case, compare 1st elements, then second etc.
    print(f'Compare {left} vs {right} ')
    #condition 1: is either null?  If left is null, return True, if right is null return False
    if not left:
        return True
    if not right:
        return False
    l=left.pop(0)
    r=right.pop(0)
    # condition 2: one side is an integer, the other is a list - convert the integer to a list 
    # which contains that integer as its only value, then re-try the comparison.
    # ... but that should just recurse forever... alternate...
    # grab first element from list, keep doing that until you hit an int, them make comparison
    if isinstance(l,int) and isinstance(r,list):
        rr=r[0]
        while not isinstance(rr,int):
            rr=r[0]
        if l < rr:
            return True
        if rr < l:
            return False
        #TODO - do we have to put whatever's left of the list back?
        return comparePackets3(left,right)
    if isinstance(l,list) and isinstance(r,int):
        ll=l[0]
        while not isinstance(ll,int):
            ll=l[0]
        if ll < r:
            return True
        if r < ll:
            return False
        #TODO - do we have to put whatever's left of the list back?
        return comparePackets3(left,right)
    if isinstance(l,list) and isinstance(r,int):
        right = [right]
        left = left.insert(0,left)
        return comparePackets3(left,right)
    #condition 3: both are single integers, if left is smaller, True, if right is smaller false.
    # if equal we need to go to the next elements in the list.
    if isinstance(l,int) and isinstance(r,int):
        if l < r:
            return True
        elif r < l:
            return False
        else:
            return comparePackets3(left,right)

    # condition 4: both sides are lists, in which case compare first elements, then continue down list.
    if isinstance(l,list) and isinstance(r,list):
        return comparePackets3(l,r) and comparePackets3(left,right)



# # # # # # # #  
#   M A I N   #
# # # # # # # #
print(" "+ "* "*19)
print("* * * ADVENT OF CODE 2022 - DAY 13 * * *")
print("* * *          - Part 1 -          * * *")   
print(" "+ "* "*19)                
# where to find input
inputFileName="day13/day13-sample-data.txt"
#inputFileName="day13/day13-input-data.txt"
print(f"Using data from: {inputFileName}")

 
sumOfIndices=0
pairIndex = 1
with open(inputFileName, 'r') as inputFile:
    while True:
        line = inputFile.readline()
        if line == '':
            break
        if line != '\n':
            line1 = line.strip()
            line2 = inputFile.readline().strip()
            left = eval(line1)
            right = eval(line2)
            print(f'== Pair {pairIndex} ==')
            if comparePackets3(left,right):
                print("TRUE")
                sumOfIndices = sumOfIndices + pairIndex
            pairIndex = pairIndex + 1
print(f'Sum of indices: {sumOfIndices}')

print(" "+ "* "*19)
print("* * *          - Part 2 -          * * *")   
print(" "+ "* "*19)  
