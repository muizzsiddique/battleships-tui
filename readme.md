# Battleships TUI 0.2

> Ship classes:
> - Carrier = 5
> - Battleship = 4
> - Cruiser = 3
> - Submarine = 3
> - Destroyer = 2

## Where are we now:
- Boards are auto generated
- One-player only, you may only guess the computer's ships
- There is no win or lose condition, just infinite turn counts
- Command line-style of input with no input validation
- Ships are maintained in data classes (`typing.NamedTuple`) and are managed by the game

## Goals:
-[ ] TUI navigation over board (rather than typing out coordinates like B6)
-[ ] Arbitrary ship sizes and shapes (probably through a .conf file)
  - The grid might contain references to the ship that has a tile there