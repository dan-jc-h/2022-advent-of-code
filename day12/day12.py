# 2022 Advent of Code - Day 12
#   https://adventofcode.com/2022/day/12
# Part 2 - Find the shortest path across a graph, being mindful of altitude.

import sys
import random

class Maze:
    def __init__(self):
        self.heightMap = []
        self.whereIveBeen = []
        self.start = tuple()
        self.end = tuple()
        self.path = []
        self.shortestPath = []
        self.tempPath = []
        self.shortLength = sys.maxsize
        self.length = 0
        self.hasPath=False
        self.heartbeat = 0
        self.bfsVisited=[]
        self.bfsQueue=[]
        self.bfsDists=[]
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



    def canIMoveHerebfs(self,currentLocation:tuple,testLocation:tuple) -> bool:
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
        if testLocation in self.bfsVisited:
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

 

 

    def bfs(self,start):
        #set all distances to something big
        self.bfsDists=[]
        for r in range(len(self.heightMap)):
            row = []
            for c in range(len(self.heightMap[0])):
                row.append(sys.maxsize)
            self.bfsDists.append(row)
        self.bfsVisited.append(start)
        self.bfsQueue.append(start)
        self.bfsDists[start[1]][start[0]]=0
        while self.bfsQueue:
            (x,y)=self.bfsQueue.pop()
            if (x,y)==self.end:
                print(f"TADA - {self.bfsDists[y][x]}")
            #probe in cardinal directions.
            deltas = [(0,-1),(0,+1),(-1,0),(+1,0)]
            for delta in deltas:
                dx=delta[0]
                dy=delta[1]
                if self.canIMoveHerebfs((x,y),(x+dx,y+dy)):
                    self.bfsVisited.append((x+dx,y+dy))
                    self.bfsQueue.append((x+dx,y+dy))
                    self.bfsDists[y+dy][x+dx]=self.bfsDists[y][x] + 1 #TODO is having this in the delta loop blowing up counts on nearby cells







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
    def showPath(self, path:[])->str:
        #make empty grid with dots
        grid=[]
        for r in range(len(self.heightMap)):
            row = []
            for c in range(len(self.heightMap[0])):
                row.append(".")
            grid.append(row)
        #add in path
        for stepNum in range(len(path)-1):
            #print(path[stepNum], path[stepNum+1])
            deltax = path[stepNum+1][0] - path[stepNum][0]
            deltay = path[stepNum+1][1] - path[stepNum][1]
            if (deltax,deltay) == (0,1): # down
                grid[path[stepNum][1]][path[stepNum][0]] = 'V'
            if (deltax,deltay) == (0,-1): # up
                grid[path[stepNum][1]][path[stepNum][0]] = '^'               
            if (deltax,deltay) == (-1,0): # left
                grid[path[stepNum][1]][path[stepNum][0]] = '<'
            if (deltax,deltay) == (1,0): # right
                grid[path[stepNum][1]][path[stepNum][0]] = '>'
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
      
inputFileName="day12/day12-sample-data.txt"
inputFileName="day12/day12-input-data.txt"

# create the maze
maze = Maze()

# load the heightMap
with open(inputFileName, 'r') as inputFile:
    maze.loadHeightMapFromFile(inputFileName)

# print(f'Maze data loaded from {inputFileName}, here is the height map:')
# print(maze)

# maze.findAPath(maze.start)
# print("Here is a path:")
# print(maze.path)
# print(maze.showPath(maze.path))
# print(f'Path length: {len(maze.path)}')

# maze.resetWhereHaveIBeen() #FIXME _ this should be automatic once either findAPath or findShortestPath completes



# print("Looking for shortest path...")
# maze.findShortestPath(maze.start)
# print(f'Shortest Path found is {maze.shortLength} units long.')
# print(f'{maze.heartbeat} calls to the shortest path routine were made.')
# print("Here is the shortest path:")
# print(maze.shortestPath)


# # #FIXME _ why do I need to append the maze.end here to get the drawing to work right (loses last element)?
# # maze.shortestPath.append(maze.end)

# print(maze.showPath(maze.shortestPath))

maze.bfs(maze.start)

#print(maze.bfsDists)

print(maze.bfsDists[maze.end[1]][maze.end[0]])

# for r in maze.bfsDists:
#     output=""
#     for c in r:
#         if c > 999:
#             c=999
#         output = output + f' {c:3d},'
#     print(output)


