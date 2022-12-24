# day11

<https://adventofcode.com/2022/day/11>

## Day 11 Part 1

Monkeys throwing stuff... the big challenge here might be so parse the monkey rules.

Once you do manage to parse the rules OK, it should be not too bad.

Looks like we need an array of monkey objects, the objects need to contain a list of objects being thrown around and the rules for processing them.

Should be very object-y

## Day 11 Part 2

This part removes a requirement to divide the "worry factor" by three, and runs the simulation over 10000 rounds(!).  The results is that "worry factor" explodes to huge values.  One solution is to mod the worry factor with the least Common Multiple (or  the 
product of all the divisors) of all the divisors the monkeys use the to make their decision on where to throw items.

This could easily have all been rolled into one, but I was being lazy.
