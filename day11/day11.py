# 2022 Advent of Code - Day 11
#   https://adventofcode.com/2022/day/11
# Part 1 - monkeys throwing stuff around.
#
# note: this is would be very sensitive to problems in the input file

import re

class Monkey:
    """represents a monkey.  Important aspects of the monkey's decision making are stored as attributes
    """
    def __init__(self,_items,_operation,_testDivisor:int,_trueDest:int,_falseDest:int):
        self.items=_items
        self.operation=_operation
        self.testDivisor=_testDivisor
        self.trueDest = _trueDest
        self.falseDest = _falseDest
        self.inspectionCount = 0
    def __str__(self)->str:
        output = f'items: {self.items}, op: {self.operation}, div:{self.testDivisor}, T/F:{self.trueDest}/{self.falseDest} inspects:{self.inspectionCount}'
        return output

#show me the monkeys!
def showMeTheMonkeys(troop:list[Monkey])->None:
    for i,m in enumerate(troop):
        print(f"Monkey {i}: {m}")

inputFileName = "day11/day11-sample-data.txt"
inputFileName = "day11/day11-input-data.txt"

#our troop of monkeys...
troop=[]
with open(inputFileName, 'r') as inputFile:
    # get a monkey descriptor - monkey descriptions are divided by double newlines
    for monkeyChunk in inputFile.read().split("\n\n"):
        print("- "*20)
        print(monkeyChunk)
        print("- "*20)
        lineNum=0
        for line in monkeyChunk.split('\n'):
            print(f'  {lineNum:02d}:{line}')
            lineNum=lineNum+1
            #This is risky - skip the first line and hope monkeys are in increasing order starting with 0
            if lineNum == 1:
                continue
            monkeyProperty,monkeyPropertyText=line.split(': ')
            monkeyProperty=monkeyProperty.strip()
            print(f'    [{monkeyProperty}] -> {monkeyPropertyText}')
            if monkeyProperty.lower() == "starting items":
                monkeyItems = monkeyPropertyText.split(", ")
                # convert each item to an int
                for i,item in enumerate(monkeyItems):
                    monkeyItems[i]=int(item)
                # need to reverse this to get the stack operations to work as per examples, 
                # I don't think this actually matters in terms of solving the problem.
                monkeyItems.reverse()
                print(f'      items: {monkeyItems}')
            elif monkeyProperty.lower() == "operation":
                #This is always format: new = old <operator> <num or "old">
                # so just need last two tokens, the operator and either a number or "old"
                monkeyOperation=(monkeyPropertyText.rsplit(" ",2))[-2:]
                print(f'      operation: {monkeyOperation}')
                pass
            elif monkeyProperty.lower() == "test":
                #just need to grab final number as divisor
                monkeyDivisor=int((monkeyPropertyText.split(' '))[-1])
                print(f'      divisor: {monkeyDivisor}')
            elif monkeyProperty.lower() == "if true":
                #number of the monkey that this monkey throws an item to if the remainder operation is true
                monkeyThrowOnTrue=int((monkeyPropertyText.split(' '))[-1])
                print(f'      on true, throw to: {monkeyThrowOnTrue}')
            elif monkeyProperty.lower() == "if false":
                #number of the monkey that this monkey throws an item to if the remainder operation is true
                monkeyThrowOnFalse=int((monkeyPropertyText.split(' '))[-1])
                print(f'      on false, throw to: {monkeyThrowOnFalse}')
            else:
                print("ERROR - Unrecognized Monkey property encountered, aborting.") # TODO should be exception
                exit()
            #make a monkey and add to the troop
        troop.append(Monkey(monkeyItems,monkeyOperation,monkeyDivisor,monkeyThrowOnTrue,monkeyThrowOnFalse))


showMeTheMonkeys(troop)

MAX_ROUNDS=20
round=0
while round<MAX_ROUNDS:
    round=round+1
    # go through the list of monkeys...
    for mnum,m in enumerate(troop):
        # go through this monkey's items
        while m.items:
            item=m.items.pop()
            print(f'Monkey {mnum} examines item {item}')
            # keep track of inspection count for later book keeping
            m.inspectionCount = m.inspectionCount + 1
            #execute the monkey's operation on the item
            if m.operation[1]=='old':
                expression = f'item {m.operation[0]} {item}'
            else:
                expression = f'item {m.operation[0]} {m.operation[1]}'
            item = eval(expression)
            print(f'Monkey {mnum} applies operation to item... {expression} -> {item}')
            # divide item value by 3.0
            item = int(item/3.0)
            print(f'Monkey gets bored and worry drops by 1/3... {item}')
            # decide which monkey to trow the item to
            if item % m.testDivisor == 0:
                print(f'Monkey {mnum} throws item with worry level {item} to Monkey {m.trueDest}')
                troop[m.trueDest].items.append(item)
            else:
                print(f'Monkey {mnum} throws item with worry level {item} to Monkey {m.falseDest}')
                troop[m.falseDest].items.append(item)
    print(f'----------\nEND OF ROUND {round}')
    showMeTheMonkeys(troop)

#finish up by calculations monkey business factor, which only considers the two busiest monkeys.
mostBusyMonkeys=[]
for m in troop:
    mostBusyMonkeys.append(m.inspectionCount)
mostBusyMonkeys.sort()
mostBusyMonkeys.reverse()
# monkey business only considers the two busiest monkeys
monkeyBusiness = mostBusyMonkeys[0]*mostBusyMonkeys[1]
print(f'After {MAX_ROUNDS}, Monkey Business = {monkeyBusiness}')

    

            
            
