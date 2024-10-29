from django.db import models

class Fruit(models.Model):
    print('Fruit Created')
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)