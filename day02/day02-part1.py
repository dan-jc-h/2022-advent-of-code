# 2022 Advent of Code - Day 2 part 1
#
# input file is a bunch of rock paper scissors scores, aim is to decode,score and sum scores.
# 
# DJCH 2022-12-14

inputFileName = 'day02-input-data.txt'

scores = {
    "AX" : 4,
    "AY" : 8,
    "AZ" : 3,
    "BX" : 1,
    "BY" : 5,
    "BZ" : 9,
    "CX" : 7,
    "CY" : 2,
    "CZ" : 6
}

lineNum = 1
totalScore = 0
with open(inputFileName, 'r') as inputFile:
    for x in inputFile:
        x = x.strip()
        key = x.replace(" ","")
        score = scores[key]
        #print(f'{lineNum}: {x} -> {x.replace(" ","")}, {key}, {score}')
        lineNum=lineNum + 1
        totalScore = totalScore + score

print(totalScore)