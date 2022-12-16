inputFileName = "day05-sample-data.txt"


with open(inputFileName, 'r') as inputFile:
    stackData=[]
    while True:
        line=inputFile.readline()
        if line == "\n":
            break
        stackData.append(line.strip('\n'))
        #print(line.strip('\n'))
    #print(stackData)
    #"rotate" the stack data into text representation of stacks
    stacks=[]
    for i in range(len(stackData[0])):
        stack=""
        for j in range(len(stackData)-1,-1,-1):
            #print(f'[{i}],[{j}],"{stackData[j][i]}"')
            stack = stack + stackData[j][i]
        if stack[0]>='0' and stack[0]<='9':
            print(stack)
            stacks.append(list(stack[1:].strip(' ')))
    print(stacks)
    
