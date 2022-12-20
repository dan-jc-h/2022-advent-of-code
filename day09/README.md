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

## Implementation

I think this can be down with out and array, just tracking coordinates of the head and then updating coordinates of the tail.  THen you just record a list (actually a set of tuples - you're asked for the distinct number of places) of places the tail goes, then just grab the size of that list.
