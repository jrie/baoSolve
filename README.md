# baoSolve
A bao game maximum steal finder

### Description

BaoSolve is a python script which tries to determine the "best" move on provided playboards. The strategy is simple, to try to steal as much as possible playstones from the opponent player.

BaoSolve does not find the optimal strategy for a move so. In example, it does not tell you if a move provides lots of playstones to the other player to steal nor if a move would let you run out of further moves or similar. Its just greedy and focusses only on capturing as much as possible playstones from the other player.

## How it works
BaoSolve requires an input file to operate on. For now it looks for a file called "playboard.csv" which can be generated using baoGen ( https://github.com/jrie/baoGen ), another tool to create random playboards.

But you can also feed in of course any other playboard (a single one) if you follow the input format.

Basically any input must be build up like that:

First you enter the first row of fields for a player, meaning the amount of stones in a field. Then the field gets seperated by an semicolon to another field, the last one of the row must be not seperated.

The fields can be of any length per line, just they should be equal and equally for each player.

An example field with 2 playstones each, basic starting scenario (8 fields per row but can be more, but 2 rows for each player):

- EXAMPLE (fiels are not seperated by blank lines!)

2;2;2;2;2;2;2;2

2;2;2;2;2;2;2;2

2;2;2;2;2;2;2;2

2;2;2;2;2;2;2;2

Newline as divider between playboards

- EXAMPLE

## Why the output?

BaoSolve does show you the output of the possible best move for a game for each playboard provided. So it does also a little bit train on how the game works. Only the latest "best" game is shown so, means if two games have equal steals, only the latest is shown so.

## Why

baoSolve was made for the code competition 3 @ www.ngb.to


