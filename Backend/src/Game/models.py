from django.db import models

class BoardMap(models.Model):
    column_no = models.IntegerField(null=False) 
    row_no = models.IntegerField(null=False) 
    is_mine = models.BooleanField(default=True)
    is_revealed =  models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    neighbour_mine_count = models.IntegerField(null=False) 

    

