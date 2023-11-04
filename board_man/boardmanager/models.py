from django.db import models


# Create your models here.

class Board(models.Model):
    macAddress = models.CharField(max_length=17)
    OPEN = 'O'
    CLOSED = 'C'
    
    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (CLOSED, 'Closed')
    )

    INTERNAL = 'I'
    EXTERNAL = 'E'

    WHERE_CHOICES = (
        (INTERNAL, 'Internal'),
        (EXTERNAL, 'External')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    where = models.CharField(max_length=1, choices=WHERE_CHOICES)
    defects = models.TextField()
    actions = models.TextField()

    def __str__(self):
        return self.macAddress + self.status + self.where + self.defects + self.actions