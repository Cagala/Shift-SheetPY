import pygsheets

def getPointCell(Cell:pygsheets.Cell):
    getCell = Cell[0].label
    number = len(getCell)-1
    pointCell = "D"+getCell[-number:] if getCell[0] == "B" else "I"+getCell[-number:]
    return pointCell