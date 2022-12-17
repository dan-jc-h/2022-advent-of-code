inputFileName = "day06-input-data.txt"
#inputFileName = "day06-sample-data.txt"

def uniqueCharsInString(str):
    return len(list(str)) == len(set(list(str)))

with open(inputFileName, 'r') as inputFile:
    for line in inputFile.readlines():
        for i in range(4,len(line)):
            subStr = line[i-4:i]
            #print(f'{i}: [{i-4}:{i}] str: "{subStr}" unique: {uniqueCharsInString(subStr)}')
            if uniqueCharsInString(subStr):
                break
        print(line,i)

        