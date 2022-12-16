# day05

<https://adventofcode.com/2022/day/5>

## Day 5 Part 1

This concerns taking a representatino fo several stacks of boxs and then applying some operations to there
where the operations move boxes from one stack to another.

Biggest initial problem is to just parse the representation of the starting state of the stacks of boxes.  
The initial stack representation looks like this:

````text
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
````

So you need to read these and then kind of rotate it and get these into lists.


After that (separated by two carriage returns) it's just a bunch of moves which can be pretty easily trasnlated to stack operatinos like pop, push etc.

````text
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
````

## Day 5 Part 2

