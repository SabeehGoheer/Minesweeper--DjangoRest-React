import random
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

from Game.models import BoardMap

def getCellByPosition(row, col):
    try:
        cell = BoardMap.objects.get(column_no=col, row_no = row)
        return cell
    except cell.DoesNotExist:
        return Response({
            'error': 'Invalid Cell Position',
            'error_code': HTTP_400_BAD_REQUEST
        }, status=HTTP_400_BAD_REQUEST)

def createBomb(gridSize):
        row = random.randint(0, gridSize-1)
        col = random.randint(0, gridSize-1)
        cell = getCellByPosition(row, col)
        if(cell.is_mine == True):
            createBomb(gridSize)
        else:
            cell.is_mine = True
            cell.save()

def addNeighbourCount(row, col, gridSize):
    # Above Row
    if row-1 >= 0:
        if col-1 >= 0:
            cell = getCellByPosition(row-1, col-1)
            if cell.is_mine == False:
                cell.neighbour_mine_count += 1
                cell.save()

        cell = getCellByPosition(row-1, col)
        if cell.is_mine == False:
            cell.neighbour_mine_count += 1
            cell.save()

        if gridSize > col+1:
            cell = getCellByPosition(row-1, col+1)
            if cell.is_mine == False:
                cell.neighbour_mine_count += 1
                cell.save()

    # Same Row
    if col-1 >= 0:
        cell = getCellByPosition(row, col-1)
        if cell.is_mine == False:
            cell.neighbour_mine_count += 1
            cell.save()

    if gridSize > col+1:
        cell = getCellByPosition(row, col+1)
        if cell.is_mine == False:
            cell.neighbour_mine_count += 1
            cell.save()

    # Below Row
    if gridSize > row+1:

        if col-1 >= 0:
            cell = getCellByPosition(row+1, col-1)
            if cell.is_mine == False:
                cell.neighbour_mine_count += 1
                cell.save()

        cell = getCellByPosition(row+1, col)
        if cell.is_mine == False:
            cell.neighbour_mine_count += 1
            cell.save()

        if gridSize > col+1:
            cell = getCellByPosition(row+1, col+1)
            if cell.is_mine == False:
                cell.neighbour_mine_count += 1
                cell.save()

def openNeighbourCells(row, col, gridSize):
    # Above Row
    if row-1 >= 0:
        if col-1 >= 0:
            cell = getCellByPosition(row-1, col-1)
            openNeighbourCellsHelper(cell, gridSize)

        cell = getCellByPosition(row-1, col)
        openNeighbourCellsHelper(cell, gridSize)

        if gridSize > col+1:
            cell = getCellByPosition(row-1, col+1)
            openNeighbourCellsHelper(cell, gridSize)

    # Same Row
    if col-1 >= 0:
        cell = getCellByPosition(row, col-1)
        openNeighbourCellsHelper(cell, gridSize)

    if gridSize > col+1:
        cell = getCellByPosition(row, col+1)
        openNeighbourCellsHelper(cell, gridSize)

    # Below Row
    if gridSize > row+1:

        if col-1 >= 0:
            cell = getCellByPosition(row+1, col-1)
            openNeighbourCellsHelper(cell, gridSize)

        cell = getCellByPosition(row+1, col)
        openNeighbourCellsHelper(cell, gridSize)

        if gridSize > col+1:
            cell = getCellByPosition(row+1, col+1)
            openNeighbourCellsHelper(cell, gridSize)

def openNeighbourCellsHelper(cell, gridSize):
    if cell.is_mine == False and cell.is_flagged == False and cell.is_revealed == False:
        cell.is_revealed = True
        cell.save()
        if(cell.neighbour_mine_count == 0): # Check if this is not the boundary condition
            openNeighbourCells(cell.row_no, cell.column_no, gridSize)