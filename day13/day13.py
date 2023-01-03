# 2022 Advent of Code - Day xx
#   https://adventofcode.com/2022/day/xx
#
# Part 1 - read pairs of data packets and determine, 
# using some ugly rules, if they are in the right order or not.
#
# Part 2 -


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

def buildQ(l,q):
    for x in l:
        if isinstance(x,int):
            q.append(x)
        elif isinstance(x,list):
            buildQ(x,q)
        else: #null
            pass 

def comparePackets(left:list,right:list)->bool:
    """Compares two packets according to rules at https://adventofcode.com/2022/day/xx.

    Args:
        left (list): packet
        right (list): packet

    Returns:
        bool: True is packets are in order, False otherwise
    """
    # Rule 1 - both values are integers (wrapped in a list)
    # Rule 2 - both values are lists
    # Rule 3 - one value is an integer
    print(left,'|',right)
    leftQ=[]
    rightQ=[]
    buildQ(left,leftQ)
    buildQ(right,rightQ)
    #print(leftQ,rightQ)
    # two sets of nested nulls are a special case (i think)
    if not leftQ and not rightQ:
        #print("both side null (possibly nested)")
        leftCount=0
        rightCount=0
        while left:
            left = left[0]
            leftCount = leftCount + 1
        while right:
            right = right[0]
            rightCount = rightCount + 1
        print(f'left nested {leftCount} deep, right nested {rightCount} deep')
        if leftCount < rightCount:
            return True
        else:
            return False
    if not leftQ:
        return True
    if not rightQ:
        return False
    while leftQ:
        lVal=leftQ.pop(0)
        rVal=rightQ.pop(0)
        if lVal < rVal:
            return True
        if lVal > rVal:
            return False
        if not leftQ:
            return True
        if not rightQ:
            return False

def comparePackets2(left:list,right:list)->bool:
    # both sides will be lists, need to walk through elements
    while left:
        print(f'  l: {left} r: {right}')
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
        print(f'  {left} vs {right}')
        if isinstance(l,int) and isinstance(r,int):
            if l < r:
                print("    left < right -> True")
                return True
        if isinstance(l,int) and isinstance(r,list):
            return comparePackets2([l],right)
        if isinstance(l,list) and isinstance(r,int):
            return comparePackets2(left,[r])
        # we must be comparing two lists
        if comparePackets2([l],[r]):
            return comparePackets2(left[1:],right[1:])
 
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
            print(pairIndex,left,right)
            if comparePackets2(left,right):
                sumOfIndices = sumOfIndices + pairIndex
            pairIndex = pairIndex + 1
print(f'Sum of indices: {sumOfIndices}')

print(" "+ "* "*19)
print("* * *          - Part 2 -          * * *")   
print(" "+ "* "*19)  
