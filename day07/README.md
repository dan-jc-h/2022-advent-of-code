# day07

<https://adventofcode.com/2022/day/7>

## Day 7 Part 1

Here you basically build a representation fo a file system, so it's a tree problem.

### Couple of design considerations

    * Link to parent directory - I have a link to the parent directory in each directory node.  Given the nature of the exercise in part 1 I don't think this was required.
    * Directory and file node types - Could have used a single "Node" class to represent either directory of File, but I used separate File and Dir classes

### The Actual Exercise

Parsing and building the tree was kind of fun.  And routines to print etc. and otherwise traverse worked well.  There's obioulsy a lot of fragility here because there's just not a lot of error checking.  But it works OK.

I had a hard time getting the actual answer - it seemed like a weird question... add up size of all directories, _as long as they are less than 100,000 bytes_ - huh?  But it's OK, I grew to accept it.