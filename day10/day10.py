# 2022 Advent of Code - Day 10
#
# this is a simulation of a simplified CPU

from enum import Enum

class CPUState(Enum):
    PROCESSING = 1
    WAITING =2

class Instruction:
    def __init__(self,_opcode:str,_executionTime:int,_fn) -> None:
        self.opcode = _opcode
        self.executionTime = _executionTime
        self.fn = _fn

class Cpu:
    def __init__(self) -> None:
        self.instructions=set() # dict?
        self.X=1
        self.state=CPUState.WAITING
        self.currentInstruction=None
        self.currentInstructionParms=""
        self.cyclesRemaining=0
    def execute(self)-> None:
        #find the fn
        for inst in self.instructions:
            if inst.opcode == self.currentInstruction:
                inst.fn(self,self.currentInstructionParms)
    def __str__(self) -> str:
        return f'state: {self.state.name} X={self.X}'
    def getInstruction(self,opcode:str)->Instruction:
        for i in self.instructions:
            if i.opcode==opcode:
                return i
        return None #FIXME - this should be an exception
    def loadInstruction(self,opcode:str,parms:str)->None:
        #print(f"Loading Instruction: {opcode}({parms}) ")
        self.currentInstruction=self.getInstruction(opcode).opcode
        self.currentInstructionParms=parms
        self.cyclesRemaining=self.getInstruction(self.currentInstruction).executionTime-1
        self.state=CPUState.PROCESSING
    def cycle(self) -> None:
        # if there are cycles remaining in the current instruction:
        #   - decrement cycles remaining
        # if cycles remaining hits zero - execute instruction, and set state to WAITING
        if self.cyclesRemaining > 0:
            self.cyclesRemaining = self.cyclesRemaining - 1
        else:
            self.execute()
            self.state=CPUState.WAITING


def fnNoop(c:Cpu,p:str):
    #print(":fnNoop")
    pass

def fnAddx(c:Cpu,y:int):
    #print(":fnAddx")
    c.X = c.X + int(y)


inputFileName = "day10/day10-simple-sample-data.txt"
inputFileName = "day10/day10-sample-data.txt"
inputFileName = 'day10/day10-input-data.txt'


#build the virtual cpu
adventOMatic9000 = Cpu()
adventOMatic9000.instructions.add(Instruction("noop",1,fnNoop))
adventOMatic9000.instructions.add(Instruction("addx",2,fnAddx))

#set up sampling
SIGNAL_SAMPLE_POINTS=[20,60,100,140,180,220]
signalStrength = 0

# read and execute program
with open(inputFileName, 'r') as inputFile:
    cycleCounter = 1
    programlineNumber = 0
    while True:
        print(f'[cycle: {cycleCounter:04d} Program Line: {programlineNumber:04d}] CPU: {adventOMatic9000}')
        if adventOMatic9000.state == CPUState.WAITING:
            #get an instruction and load it to CPU
            line = inputFile.readline()
            programlineNumber = programlineNumber + 1
            if line == '':
                break
            opcode,operand=(((line.strip())+" # #").split())[0:2]
            if operand == '#':
                operand = ''
            adventOMatic9000.loadInstruction(opcode,operand)
        elif adventOMatic9000.state == CPUState.PROCESSING:
            #CPU busy, pass
            pass
        else:
            exit() #FIXME - should be exception
        #calculate signal strenght if we are at a sample point
        if cycleCounter in SIGNAL_SAMPLE_POINTS:
            signalStrength=signalStrength+(cycleCounter*adventOMatic9000.X)
        #cycle the machine
        adventOMatic9000.cycle()
        cycleCounter = cycleCounter + 1

print(f'Program complete after {cycleCounter} cycles and {programlineNumber} lines of instructions.')
print(f'Signal Strength: {signalStrength}')

