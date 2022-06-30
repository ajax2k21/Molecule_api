from django.db import models

class Molecule(models.Model):
    LSN = models.BigIntegerField()
    sdf = models.CharField(max_length=100000)


    #def __str__(self):
    #    return self.LSN