# 2022 Advent of Code - Day 12
#   https://adventofcode.com/2022/day/12
# Part 2 - Find the shortest path across a graph, being mindful of altitude.

import sys
import random

class Maze:
    def __init__(self):
        self.heightMap = []
        self.start = tuple()
        self.end = tuple()
        self.bfsVisited=set()
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

    def bfs(self,_start):
        #set all distances to something big
        self.bfsDists=[]
        for r in range(len(self.heightMap)):
            row = []
            for c in range(len(self.heightMap[0])):
                row.append(sys.maxsize)
            self.bfsDists.append(row)
        # add start node to queue and visited set, and mark this dist to 0 (starting)
        self.bfsVisited.clear()
        self.bfsVisited.add(_start)
        self.bfsQueue.clear()
        self.bfsQueue.append(_start)
        self.bfsDists[_start[1]][_start[0]]=0
        # keep going while there is anywhere left to search
        while self.bfsQueue:
            #print(self.bfsQueue)
            # get next location
            (x,y)=self.bfsQueue.pop(0)
            # found the end point! Could stop now.
            if (x,y)==self.end:
                print(f"TADA - {self.bfsDists[y][x]}")
            #probe in cardinal directions.
            for dx,dy in [(0,-1),(0,+1),(-1,0),(+1,0)]:
                if (x+dx,y+dy) == (0,18):
                    zzz=1
                if self.canIMoveHerebfs((x,y),(x+dx,y+dy)):
                    self.bfsVisited.add((x+dx,y+dy))
                    self.bfsQueue.append((x+dx,y+dy))
                    self.bfsDists[y+dy][x+dx]=self.bfsDists[y][x] + 1 #TODO is having this in the delta loop blowing up counts on nearby cells


inputFileName="day12/day12-sample-data.txt"
inputFileName="day12/day12-input-data.txt"

# create the maze
maze = Maze()

# load the heightMap
with open(inputFileName, 'r') as inputFile:
    maze.loadHeightMapFromFile(inputFileName)

# print(f'Maze data loaded from {inputFileName}, here is the height map:')
# print(maze)

print("Looking for shortest path...")
maze.bfs(maze.start)
print(f'Shortest path length: {maze.bfsDists[maze.end[1]][maze.end[0]]}')

# for y,r in enumerate(maze.bfsDists):
#      output=""
#      for x,c in enumerate(r):
#          if c > 999:
#              c=999
#          output = output + f' {maze.heightMap[y][x]}{c:3d},'
#      print(output)

for y,r in enumerate(maze.bfsDists):
     output=""
     for x,c in enumerate(r[0:2]):
         if c > 999:
             c=999
         output = output + f' {maze.heightMap[y][x]}{c:3d},'
     print(output)


