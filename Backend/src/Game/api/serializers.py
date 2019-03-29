from rest_framework import serializers

from Game.models import BoardMap

class BoardMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMap
        fields = ('__all__')

    def create(self, request):
        

        print(request.method)
        print(request.data) # remove later on
        
        gridSize = request.data.get('gridSize')
        numberOfBombs = request.data.get('numberOfBombs')

        # Creating Cells
        for row in range(gridSize):
            for col in range(gridSize):
                bm = BoardMap(column_no=col, row_no=row, is_mine=False, is_revealed=False, is_flagged=False, neighbour_mine_count=0 )
                bm.save()
        return bm
        
        # # Creating Bombs in Cells
        # for x in range(numberOfBombs):
        #     createBomb(gridSize)

        # # Counting Neighbour Count
        # for row in range (gridSize):
        #     for col in range (gridSize):
        #         cell = getCellByPosition(row, col)
        #         if cell.is_mine == True:
        #             addNeighbourCount(row, col, gridSize)
        
        # return Response(status=HTTP_201_CREATED)
