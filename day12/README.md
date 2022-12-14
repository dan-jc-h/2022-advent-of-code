# day12

<https://adventofcode.com/2022/day/12>

## Day 12 Part 1

Looks like we're doing some graph traversing!

This ended up as a pretty straightforward BFS search job, _BUT_ - i got majorly
stuck one this one and beat my head against if for a while.  The problem was that
I screwed up accessing a list I was using as a queue.  I had to add things to one
end of a queue and then remove them from the other... FIFO.  I screwed up and was
adding to then grabbing from the same end, so it was LIFO
(more of a stack than a queue).  (It seems to me that this
screwed me up at some point in the past as well.)

In python `list.pop()` takes from the end of the list, and `list.append()` adds
to the end, this is what I was doing... e.g.

````python
    q = list[]
    # add some things to the queue
    q.append(7)
    q.append(8)
    q.append(2)
    # get something from the queue
    x = q.pop()
    # x will equal 2
````

But I wanted to add to one end and remove from the other.  You can still do
this with pop, but you have to specify that you want to take from the front,
with `pop(0)`... e.g.

````python
    q = list[]
    # add some things to the queue
    q.append(7)
    q.append(8)
    q.append(2)
    # get something from the queue
    x = q.pop(0)
    # x will equal 7
````

This could have been avoided by defining a `list.first()` and `list.last()`,
or `list.head()` and `list.tail()`, functions.  Or using some module that defines
queue operations of which I suspect there are many.

## Day 12 Part 2

Once I finally had Part 1 working, part 1 took less than 5 minutes.  You need to calculate
the shortest path from all the points at 'a' altitude, and my routine to find
the shortest path already took a start point as an optional parameter, so it 
was very easy to loop over the grid and calculate the distance from all possible
locations then just grab the smallest of those values.  I think it took longer to write this
description than to code and run this part.
