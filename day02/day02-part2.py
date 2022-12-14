# 2022 Advent of Code - Day 2 part 2
#
# input file is a bunch of rock paper scissors scores, aim is to decode,score and sum scores.
#
# part 2 just updates the scoring dict
#
# DJCH 2022-12-14

inputFileName = 'day02-input-data.txt'

scores = {
    "AX" : 3,
    "AY" : 4,
    "AZ" : 8,
    "BX" : 1,
    "BY" : 5,
    "BZ" : 9,
    "CX" : 2,
    "CY" : 6,
    "CZ" : 7
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