# 2022 Advent of Code - Day 10
#
# Part 1 - this is a simulation of a simplified CPU
# Part 2 - we add a display

from enum import Enum

class CPUState(Enum):
    """
    Enum Representing the state the CPU is in.  Only two options in our simple case.
    """
    PROCESSING = 1
    WAITING =2

class Instruction:
    """
    Class representing a CPU instruction.  Important attributes are the opcode, execution time and a function that actually performs the instruction
    """
    def __init__(self,_opcode:str,_executionTime:int,_fn) -> None:
        self.opcode = _opcode
        self.executionTime = _executionTime
        self.fn = _fn

class Cpu:
    """
    class representing a CPU. Important attributes are a set of valid instructions, the X register, the CPU state, the instruction currently being executed and it's parameters, number of cycles remaining in the active instruction.

    Normal use is to check the status, if WAITING, load an instruction and cycle the machine until it's WAITING again.
    """
    def __init__(self) -> None:
        """
        CPU initialization, valid instructions need to be set.
        """
        self.instructions=set() # dict?
        self.X=1
        self.state=CPUState.WAITING
        self.currentInstruction=None
        self.currentInstructionParms=""
        self.cyclesRemaining=0
    def execute(self)-> None:
        """
        execute the currently loaded instruction by calling its function
        """
        self.getInstruction(self.currentInstruction).fn(self,self.currentInstructionParms)
    def __str__(self) -> str:
        return f'state: {self.state.name} X={self.X}'
    def getInstruction(self,opcode:str)->Instruction:
        """
        get an instruction, given an opcode

        Args:
            opcode (str): the text opcode for an instruction

        Returns:
            Instruction: the requested instruction, None if not found
        """
        for i in self.instructions:
            if i.opcode==opcode:
                return i
        return None #TODO - this should maybe be an exception
    def loadInstruction(self,opcode:str,parms:str)->None:
        """
        load an instruction into the CPU to prepare for execution, set state to PROCESSING.  execution actually occurs at the END of the required clock cycles for this instruction.  E.g. register will not be updated until the last cycle of it's execution.  In previous cycles register will be unchanged.

        Args:
            opcode (str): The opcode for the instruction
            parms (str): any params (watch out... str, may need to convert to int to do anything in the instruction function)
        """
        self.currentInstruction=self.getInstruction(opcode).opcode
        self.currentInstructionParms=parms
        self.cyclesRemaining=self.getInstruction(self.currentInstruction).executionTime-1
        self.state=CPUState.PROCESSING
    def cycle(self) -> None:
        """apply a clock cycle to the CPU. If there are cycles remaining in the current instruction, decrement cycles remaining; if cycles remaining is zero - execute instruction by calling its function, and set state to WAITING
        """
        if self.cyclesRemaining > 0:
            self.cyclesRemaining = self.cyclesRemaining - 1
        else:
            self.execute()
            self.state=CPUState.WAITING

# Dimensions for our CRT display
CRT_WIDTH = 40
CRT_HEIGHT = 6

class CRT:
    """represents a CRT display, contains the dimensions and a buffer (list of lists... one list per line)
    """
    def __init__(self):
        """initialize display elements and set array to dots"""
        self.width=CRT_WIDTH
        self.height=CRT_HEIGHT
        self.buffer=[]
        for h in range(self.height):
            self.buffer.append([])
            for w in range(self.width):
                self.buffer[h].append(".")
    def __str__(self):
        output=""
        for h in range(self.height):
            for w in range(self.width):
                output=output+self.buffer[h][w]
            output=output+"\n"
        return (output)
    def update(self,_cpu:Cpu,x:int,y:int):
        """update the display.  The (annoying) rules are, that a particular element should be updated only if the x location in the row is equal to the current X register value... +/- 1.

        Args:
            _cpu (Cpu): the CPU
            x (int): X location
            y (int): Y location
        """
        x=x-1 # annoying correction
        if x>=_cpu.X-1 and x<=_cpu.X+1 :
            print(f'  in display.update -> x:{x} y:{y} X-reg={_cpu.X}')
            self.buffer[y][x]="#"

#
# Definitions of CPU Instruction functions.  REQUIRED PARMs are:
#   The CPU, and
#   a string containing parameters (which may be ignored)
#
def fnNoop(c:Cpu,p:str)->None:
    """noop CPU Instruction - do nothing

    Args:
        c (Cpu): CPU
        p (str): Optional arguments (ignored)
    """
    #print(":fnNoop")
    pass

def fnAddx(c:Cpu,y:int)->None:
    """addx CPU instruction - add a value to the X register

    Args:
        c (Cpu): CPU
        y (int): value to add (will need to be cast to int)
    """
    #print(":fnAddx")
    c.X = c.X + int(y)


#inputFileName = "day10/day10-simple-sample-data.txt"
#inputFileName = "day10/day10-sample-data.txt"
inputFileName = 'day10/day10-input-data.txt'


#build the virtual cpu and add instructions
adventOMatic9000 = Cpu()
adventOMatic9000.instructions.add(Instruction("noop",1,fnNoop))
adventOMatic9000.instructions.add(Instruction("addx",2,fnAddx))

#create display
display=CRT()

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
            #minor trick here to make sure we get at least two elements.  Maybe should have used re
            opcode,operand=(((line.strip())+" # #").split())[0:2]
            if operand == '#':
                operand = ''
            adventOMatic9000.loadInstruction(opcode,operand)
        elif adventOMatic9000.state == CPUState.PROCESSING:
            #CPU busy, pass
            pass
        else:
            exit() #FIXME - should be exception
        #calculate signal strength if we are at a sample point
        if cycleCounter in SIGNAL_SAMPLE_POINTS:
            signalStrength=signalStrength+(cycleCounter*adventOMatic9000.X)
        #update display
        display.update(adventOMatic9000,cycleCounter%display.width,cycleCounter//display.width)
        #cycle the machine
        adventOMatic9000.cycle()
        cycleCounter = cycleCounter + 1

print(f'Program complete after {cycleCounter} cycles and {programlineNumber} lines of instructions.')
print(f'Signal Strength: {signalStrength}')
print(display)

