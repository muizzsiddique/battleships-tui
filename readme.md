# Battleships TUI 0.2

## Where are we now:
- Boards are auto generated
- One-player only, you may only guess the computer's ships
- There is no win or lose condition, just infinite turn counts
- Command line-style of input with no input validation
- Ships are maintained in data classes (`typing.NamedTuple`) and are managed by the game

## Goals:
1. TUI navigation to move across board (rather than typing out coordinates like B6)
2. Arbitrary ship sizes and shapes (probably through a .conf file)
  - Could store reference to a tile's respective ship object in the tile

---

### Ship classes:
- Carrier = 5
- Battleship = 4
- Cruiser = 3
- Submarine = 3
- Destroyer = 2
