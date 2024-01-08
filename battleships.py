from typing import NamedTuple
import random

class Ship(NamedTuple):
    # X and Y anchored to the top-left and are 1-based indexed
    x: int
    y: int
    isHorizontal: bool
    size: int

ship_classes = {
    "carrier":    5,
    "battleship": 4,
    "cruiser":    3,
    "submarine":  3,
    "destroyer":  2
}

def canIntersect(a_start, a_stop, b_start, b_stop):
    ''' Determines whether two ranges "a" and "b" intersect. '''
    
    return a_start <= b_stop and b_start <= a_stop

def generateShips():
    ''' Place ships onto the board (logically). '''
    
    for name, size in ship_classes.items():
        # Keep generating a new ship for the currently given class...
        while True:
            isHorizontal = random.choice((True, False))
            x = 1+random.randrange(0, 8-(size if isHorizontal else 0))
            y = 1+random.randrange(0, 8-(size if not isHorizontal else 0))

            for ship in ships.values():
                horizontalIntercept = ship.isHorizontal and isHorizontal and ship.y == y and canIntersect(ship.x, ship.x+ship.size, x, x+size)
                verticalIntercept = not ship.isHorizontal and not isHorizontal and ship.x == x and canIntersect(ship.y, ship.y+ship.size, y, y+size)
                perpendicularIntercept1 = isHorizontal and not ship.isHorizontal and y in range(ship.y, ship.y+ship.size) and ship.x in range(x, x+size)
                perpendicularIntercept2 = not isHorizontal and ship.isHorizontal and ship.y in range(y, y+size) and x in range(ship.x, ship.x+ship.size)
                
                if horizontalIntercept or verticalIntercept or perpendicularIntercept1 or perpendicularIntercept2:
                    break
            # ...until it is colliding with no other existing ship
            else:
                break
        ships[name] = Ship(x, y, isHorizontal, size)

def populateBoard():
    ''' Draw O tiles where there are ships on the board. '''
    
    for name, ship in ships.items():
        if ship.isHorizontal:
            row = board[ship.y-1]
            row = row[:ship.x-1] + ("O" * ship.size) + row[ship.size+(ship.x-1):]
            board[ship.y-1] = row
        else:
            for i in range(ship.size):
                row = board[ship.y - 1 + i]
                row = row[:ship.x-1] + "O" + row[ship.x:]
                board[ship.y - 1 + i] = row

def printBoard():
    ''' Hide the O tiles before rendering the board. '''
    
    for line in board:
        # print(line) to see the ships
        print(line.replace("O", "."))

def getXY():
    ''' Unvalidated and crash prone method to retrieve coordinates. '''
    
    x, y = input("Type out the column and row like so: 3 5\n").split()
    return int(x), int(y)

def setBoardTile(x, y, char):
    ''' Update an individual tile. Use X for hit and v for miss. '''
    
    board[y-1] = board[y-1][:x-1] + char + board[y-1][x:]

def clearScreen():
    print(end="\033c")

messageLog = []

ships = {}
board = [("." * 8) for i in range(8)]
generateShips()
populateBoard()

while True:
    clearScreen()
    printBoard()

    for line in messageLog:
        print(line)
    messageLog = []

    x, y = getXY()

    if board[y-1][x-1] in "Xv":
        messageLog.append("You have already tried hitting that tile.")
    elif board[y-1][x-1] == ".":
        setBoardTile(x, y, "v")
        messageLog.append("You hit nothing.")
    else:
        setBoardTile(x, y, "X")
        messageLog.append("You hit something!")

        # Remove a tile from a ship, then check all ships to see if one of them had all their tiles cleared
        # from the board.
        for name, ship in ships.items():
            if ship.isHorizontal:
                if "O" not in board[ship.y-1][ship.x-1:ship.x+ship.size]:
                    messageLog.append("You sunk {}!".format(name.title()))
                    del ships[name]
                    break
            else:
                # Look for any live ship tile
                for ypos in range(ship.y, ship.y + ship.size):
                    if board[ypos-1][ship.x-1] == "O":
                        # If found, move onto next ship
                        break
                else: # Can't find a live ship tile, so must have been sunk
                    messageLog.append("You sunk {}!".format(name.title()))
                    del ships[name]
                    break
