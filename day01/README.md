# day01

<https://adventofcode.com/2022/day/1>

## Day 1 Part 1

Input is a text file of numbers, one number per line with a blank line delineating groups.  
Each line represents the calories in one snack carried by an elf, and each group of numbers
between blank lines is one elf's inventory.  

Desired output is the total of the largest group.

... this looks like a job for `awk`, because `awk` doesn't get enough love.

## Day 1 Part 2

Oh, so now that I used `awk` part 2 wants me to do something that's hard in awk...
get the sum of the calories carried by the _top three_ elves.  Would have been easy in
python etc. Oh well, I'll stick with awk and spit the totals out to a text file and beat it up
with some command line stuff.
