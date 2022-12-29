# 2022 Advent of Code - Day 12
#   https://adventofcode.com/2022/day/12
# Part 2 - Find the shortest path across a graph, being mindful of altitude.

inputFileName="day12/day12-sample-data.txt"

class Maze:
    def __init__(self):
        self.heightMap = []
        self.whereIveBeen = []
        self.start = tuple()
        self.end = tuple()
        self.path = []
    def __str__(self)->str:
        if len(self.heightMap) == 0:
            return "Data must be loaded (with loadHeightMap()) before Maze can be used."
        else:
            output = ""
            for rNum,row in enumerate(self.heightMap):
                for cNum,cell in enumerate(row):
                    output = output + cell
                output = output + "\n"
            output = f'{output}S:{self.start}, E:{self.end}'
            return output  
    def loadHeightMapFromFile(self,inputFileName:str):
        with open(inputFileName, 'r') as inputFile:
            row=[]
            for line in inputFile.readlines():
                row=list(line.strip())
                self.heightMap.append(row)

        # find Start (S) and End (E)
        for rNum,row in enumerate(self.heightMap):
            for cNum,cell in enumerate(row):
                if cell == 'S':
                    self.start=(cNum,rNum)
                elif cell == 'E':
                    self.end=(cNum,rNum)

        # need to create and zero out the I've been here mask
        #self.whereIveBeen = [[0] * len(self.heightMap[0])] * len(self.heightMap)
        for r in range(len(self.heightMap)):
            row = []
            for c in range(len(self.heightMap[0])):
                row.append(0)
            self.whereIveBeen.append(row)
        # and then set the Start location to 1 (we are already there)
        self.whereIveBeen[self.start[1]][self.start[0]]
    def canIMoveHere(self,currentLocation:tuple,testLocation:tuple) -> bool:
        currentx=currentLocation[0]
        currenty=currentLocation[1]
        x=testLocation[0]
        y=testLocation[1]
        maxRows = len(self.heightMap)
        maxCols = len(self.heightMap[0])
        #Check to make we are test location is in bounds
        if x<0 or y<0 or x>maxCols-1 or y>maxRows-1: 
            return False
        #Check to make sure we haven't been to the test location yet
        if self.whereIveBeen[y][x] == 1:
            return False
        # Check height map to see if we can go to the test location.  
        # Height of test location can be no more than "1" unit more 
        # than height of starting location.  Also "E" has height "z",
        # "S" has height "a".
        currentHeight = self.heightMap[currenty][currentx]
        testHeight = self.heightMap[y][x]
        if testHeight == 'E':
            testHeight = 'z'
        if currentHeight == 'S':
            currentHeight = 'a'
        if ord(currentHeight) + 1 < ord(testHeight):
            return False
        #We should be OK    
        return True
    def findShortestPath(self)->int:
        dist = 0
        print(f'{self.start}->{self.end}')
        x=self.start[0]
        y=self.start[1]
        self.whereIveBeen[y][x]=1
        nRows = len(self.heightMap)
        nCols = len(self.heightMap[0])
        dist1 = nRows*nCols+1
        dist2 = dist1
        dist3 = dist2
        dist4 = dist3
        if x==self.end[0] and y==self.end[1]: #start == end:
            print("I think I'm at the end")
            return dist
        else:
            #if not in top row, probe up
            if self.canIMoveHere((x,y),(x,y-1)):
                print("UP")
                dist1 = findShortestPath((x,y-1), end, nRows)
            #if not in bottom row, probe down
            if self.canIMoveHere((x,y),(x,y+1)):
                print("DOWN")
                dist2 = findShortestPath((x,y+1), end, nRows)
            #if not in left col, probe left
            if self.canIMoveHere((x,y),(x-1,y)):
                print("LEFT")
                dist3 = findShortestPath((x-1,y), end, nRows)
            #if not in right col, probe right
            if self.canIMoveHere((x,y),(x+1,y)):
                print("RIGHT")
                dist4 = findShortestPath((x+1,y), end, nRows)

    def findAPath(self, start)->bool:
        #print(f'{start}->{self.end}')
        x=start[0]
        y=start[1]
        self.whereIveBeen[y][x]=1
        self.path.append(start)
        nRows = len(self.heightMap)
        nCols = len(self.heightMap[0])
        if x==self.end[0] and y==self.end[1]: #start == end:
            #print("I'm at the end")
            return True
        else:
            #if not in top row, probe up
            if self.canIMoveHere((x,y),(x,y-1)):
                #print("UP")
                self.findAPath((x,y-1))
            #if not in bottom row, probe down
            if self.canIMoveHere((x,y),(x,y+1)):
                #print("DOWN")
                self.findAPath((x,y+1))
            #if not in left col, probe left
            if self.canIMoveHere((x,y),(x-1,y)):
                #print("LEFT")
                self.findAPath((x-1,y))
            #if not in right col, probe right
            if self.canIMoveHere((x,y),(x+1,y)):
                #print("RIGHT")
                self.findAPath((x+1,y))

            #not at end
            return False
    def showPath(self)->str:
        #make empty grid with dots
        grid=[]
        for r in range(len(self.heightMap)):
            row = []
            for c in range(len(self.heightMap[0])):
                row.append(".")
            grid.append(row)
        #add in path
        for stepNum in range(len(self.path)-1):
            #print(self.path[stepNum], self.path[stepNum+1])
            deltax = self.path[stepNum+1][0] - self.path[stepNum][0]
            deltay = self.path[stepNum+1][1] - self.path[stepNum][1]
            if (deltax,deltay) == (0,1): # down
                grid[self.path[stepNum][1]][self.path[stepNum][0]] = 'V'
            if (deltax,deltay) == (0,-1): # up
                grid[self.path[stepNum][1]][self.path[stepNum][0]] = '^'               
            if (deltax,deltay) == (-1,0): # left
                grid[self.path[stepNum][1]][self.path[stepNum][0]] = '<'
            if (deltax,deltay) == (1,0): # right
                grid[self.path[stepNum][1]][self.path[stepNum][0]] = '>'
        #mark S and E
        grid[self.start[1]][self.start[0]] = 'S'
        grid[self.end[1]][self.end[0]] = 'E'        
        #generate string
        output = ""
        for r in range(len(self.heightMap)):
            for c in range(len(self.heightMap[0])):
                output = output + grid[r][c]
            output = output + "\n"

        return output


        return output     
      

# create the maze
maze = Maze()

# load the heightMap
with open(inputFileName, 'r') as inputFile:
    maze.loadHeightMapFromFile(inputFileName)

print(f'Maze data loaded from {inputFileName}, here is the height map:')
print(maze)

maze.findAPath(maze.start)

print("Here is a path:")
print(maze.showPath())
print(f'Path length: {len(maze.path)}')


