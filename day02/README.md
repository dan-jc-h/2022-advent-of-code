# day02

<https://adventofcode.com/2022/day/2>

## Day 2 Part 1

Input is a text file of pairs of numbers e.g.:

````text
A Y
B X
C Z
````

Each pair representing the result in a rock-paper-scissors
game.  Each pair has a predetermined score and there are only nine possibilities:

They play `A`, `B` or `C` - for their Rock, Paper, Scissors

You play `X`, `Y` or `Z` - for your Rock, Paper, Scissors

Scoring: you get a 1 for playing rock, 2 for paper and 3 for scissors, **and** you get 0 for a loss, 3 for a tie and 6 for a win

Here are all the possibilities:

````text
    AX -> 1 for rock + 3 for tie = 4
    AY -> 2 for paper + 6 for win = 8
    AZ -> 3 for scissors + 0 for loss = 3
    BX -> 1 for rock + 0 for loss = 1
    BY -> 2 for paper + 3 for tie = 5 
    BZ -> 3 for scissors + 6 for win = 9
    CX -> 1 for rock + 6 for win = 7
    CY -> 2 for paper + 0 for loss = 2
    CZ -> 3 for scissors + 3 for tie = 6
````

Desired output is total score of all the rounds.

## Day 2 part 2

Problem now restated...

The X, Y, Z now mean lose, draw and win, respectively.  Scoring doesn't change.

Now you have to

  1. read the first character, to determine what the other player played,
  1. read the second character to determine the round outcome
  1. determine what you need to play to get the outcome,
  1. finally add the score for this round to the total score

I think this is only a minor change, the scoring dict just needs to be updated:

````text
    AX -> other plays rock, you lose, you must have played scissors -> 3
    AY -> other plays rock, you draw, you must have played rock -> 4
    AZ -> other plays rock, you win, you must have played paper -> 8
    BX -> other plays paper, you lose, you must have played rock -> 1
    BY -> other plays paper, you draw, you must have played paper -> 5
    BZ -> other plays paper, you win, you must have played scissors -> 9
    CX -> other plays scissors, you lose, you must have played paper -> 2
    CY -> other plays scissors, you draw, you must have played scissors -> 6
    CZ -> other plays scissors, you win, you must have played rock -> 7
````
