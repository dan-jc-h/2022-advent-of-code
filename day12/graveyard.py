# some scraps i was working on but abandoned

--------------------

    def findShortestPath(self,start):
        #status printing etc.
        #print(f'{start}->{self.end} length: {self.shortLength}')
        self.heartbeat = self.heartbeat + 1
        if self.heartbeat % 250_000 == 0:
            print(f'\t{self.heartbeat} calls to findShortestPath() - current shortest: {self.shortLength} %visited:{self.percentVisited()}')
            print(f'\t  {len(self.tempPath)} {self.tempPath[0:5]}...{self.tempPath[-5:]}')
            print(self.showPath(self.tempPath))
            s=input("Press a key.")
        # set x and y to save typing and typos    
        x=start[0]
        y=start[1]

        #We got to the end
        if x==self.end[0] and y==self.end[1]:
            self.hasPath=True # this isn't really used at this point
            self.shortLength=min([self.length,self.shortLength])
            #this is the new shortest path
            if self.length == self.shortLength:
                self.shortestPath=self.tempPath.copy()
                self.shortestPath.append(self.end) # need to do this - for reasons TODO fix this comment
                print(f"I'm at the end, iteration:{self.heartbeat}, length={self.shortLength}, path_{self.shortestPath}")
            return

        #we aren't at the end yet, keep looking
        self.tempPath.append(start)
        self.whereIveBeen[y][x]=1
        self.length = self.length + 1
        #probe in cardinal directions.  But randomize to avoid traps
        deltas = [(0,-1),(0,+1),(-1,0),(+1,0)]
        random.shuffle(deltas)
        for delta in deltas:
            dx=delta[0]
            dy=delta[1]
            if self.canIMoveHere((x,y),(x+dx,y+dy)):
                self.findShortestPath((x+dx,y+dy))
        #backtrack
        self.whereIveBeen[y][x]=0
        self.tempPath.pop()
        self.length=self.length-1

--------------------

   visitedSet = set()
    def dfs(self, start):
        x=start[0]
        y=start[1]
        if start not in self.visitedSet:
            self.visitedSet.add(start)
            print(f'dfs: {start}')
            #probe in cardinal directions.
            deltas = [(0,-1),(0,+1),(-1,0),(+1,0)]
            for delta in deltas:
                dx=delta[0]
                dy=delta[1]
                if self.canIMoveHere((x,y),(x+dx,y+dy)):
                    self.dfs((x+dx,y+dy))

--------------------

    def percentVisited(self)->int: #TODO - graveyard this.
        total = 0
        for r in self.whereIveBeen:
            total = total + sum(r)
        count = len(self.whereIveBeen)*len(self.whereIveBeen[0])
        return int(total*100/count)
--------------------

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

------------------

# this in loadHeightMapFromFile
       self.resetWhereHaveIBeen()

    def resetWhereHaveIBeen(self):
        #Need to create and zero out the I've been here mask
        #self.whereIveBeen = [[0] * len(self.heightMap[0])] * len(self.heightMap)
        self.whereIveBeen=[]
        for r in range(len(self.heightMap)):
            row = []
            for c in range(len(self.heightMap[0])):
                row.append(0)
            self.whereIveBeen.append(row)
        # and then set the Start location to 1 (we are already there)
        self.whereIveBeen[self.start[1]][self.start[0]]
-------------------


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

--------------

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


--------------
