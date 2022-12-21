# day09

<https://adventofcode.com/2022/day/9>

## Day 9 Part 1

The scenario here is that you are pulling a rope around.  Movements of the head of the rope are provided
in a file.  Each line is in the format:

    {U,D,L,R} n

where:

- _{U,D,L,R}_ is the single character denoting    _U_ p, _D_ own, _L_ eft or _R_ ight, and
- _n_ is the number of steps to move.

There are specific rules about how the tail follows the head.

Part 1 wants the number of distinct positions that the tail visits.

### Implementation

I think this can be down with out and array, just tracking coordinates of the head and then updating coordinates of the tail.  THen you just record a list (actually a set of tuples - you're asked for the distinct number of places) of places the tail goes, then just grab the size of that list.

## Part 2

Pretty major escalation!  Now you have a ten unit long rope, and you have to calculate the position of each piece of rope as it moves and follows the one ahead of it.

Going to put this in a new program otherwise it will just be messy.

Looks like a job for a linked list!  Bit of a rewrite of part1, but reusing some pieces

