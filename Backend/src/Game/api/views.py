
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

from Game.models import BoardMap
from .serializers import BoardMapSerializer
from .utils import createBomb, addNeighbourCount, openNeighbourCells, getCellByPosition

class BoardMapViewSet(viewsets.ModelViewSet):
    serializer_class = BoardMapSerializer
    queryset = BoardMap.objects.all()

    def update(self, request, pk=None):

        toSetFlag = request.data.get('flag')
        gridSize = request.data.get('gridSize')
       
        if toSetFlag == 'to_destroy':
            boardMap = BoardMap.objects.all()
            try:
                boardMap.delete()
                return Response(status=HTTP_200_OK)
            except boardMap.DoesNotExist:
                return Response({
                    'error': 'Error cleaning board map',
                    'error_code': HTTP_400_BAD_REQUEST
            }, status=HTTP_400_BAD_REQUEST)
        cell = BoardMap.objects.get(id=pk)
        if toSetFlag == 'is_revealed':
            cell.is_revealed = True
            cell.save()
            if cell.is_mine == True:
                serializer = BoardMapSerializer(BoardMap.objects.all(), many=True)
                return Response({'boardMap': serializer.data, 'gameStatus': 'finished'})
            if(cell.neighbour_mine_count ==0):
                openNeighbourCells(cell.row_no, cell.column_no, gridSize)
        if toSetFlag == 'is_flagged':
            if cell.is_flagged == False:
                cell.is_flagged = True
            else:
                cell.is_flagged = False
            cell.save()
        
        revealedCells = BoardMap.objects.filter(is_revealed=True)
        flaggedCells = BoardMap.objects.filter(is_flagged=True)
        serializer = BoardMapSerializer(BoardMap.objects.all(), many=True)
        return Response({'boardMap': serializer.data, 'gameStatus': 'running', 'flaggedCells': len(flaggedCells), 'revealedCells': len(revealedCells) })

    def list(self, request):
        msg = "running"
        revealedBombs = BoardMap.objects.filter(is_revealed=True, is_mine=True)
        if len(revealedBombs) > 0:
            msg = "finished"
        serializer = BoardMapSerializer(BoardMap.objects.all(), many=True)
        return Response({'boardMap': serializer.data, "gameStatus": msg})

    def destroy(self, request, pk=None):
        boardMap = BoardMap.objects.all()
        try:
            boardMap.delete()
            return Response(status=HTTP_200_OK)
        except cell.DoesNotExist:
            return Response({
                'error': 'Error cleaning board map',
                'error_code': HTTP_400_BAD_REQUEST
        }, status=HTTP_400_BAD_REQUEST)

    def create(self, request):

        gridSize = request.data.get('gridSize')
        numberOfBombs = request.data.get('numberOfBombs')

        # Creating Cells
        for row in range(gridSize):
            for col in range(gridSize):
                bm = BoardMap(column_no=col, row_no=row, is_mine=False, is_revealed=False, is_flagged=False, neighbour_mine_count=0 )
                bm.save()
        
        # Creating Mines in Cells
        for x in range(numberOfBombs):
            createBomb(gridSize)

        # Counting Neighbour Count
        for row in range (gridSize):
            for col in range (gridSize):
                cell = getCellByPosition(row, col)
                if cell.is_mine == True:
                    addNeighbourCount(row, col, gridSize)
        
        serializer = BoardMapSerializer(BoardMap.objects.all(), many=True)
        return Response(serializer.data)

