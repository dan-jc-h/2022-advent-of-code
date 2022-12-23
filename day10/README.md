# day10

<https://adventofcode.com/2022/day/10>

## Day 10 Part 1

This is a really basic cpu simulation with a CPU that supports only 2 instructions and a single register (`X`). 
We need to step through a simple program and calculate some metrics around the register and how many clock cycles 
we are into the program.  The "challenge" seems to be that one instruction `noop` takes a single cycle to execute, while the other 
instruction `addx` (add to the register) takes two.

Presumably Part 2 will introduce additional instructions (spoiler: it doesn't), so I'll try to generalize how the instructions are handled.

I always wanted to write a simple CPU simulator... maybe this will give me some ideas/inspiration!

## Day 10 Part 2

Add a display with some really funky rules about how it's updated.  This took some tweaking to match the 
reauired conditions, but I got it working.
