from django.db import models

# Create your models here.


class Calculation(models.Model):
    """
    Model for storing calculation history in the Database
    """
    expression = models.CharField(max_length=255)
    result = models.FloatField()

    def __str__(self):
        return f"{self.expression} = {self.result}"

    objects = models.Manager()
