from django.db import models
from django.utils.timezone import now

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200, primary_key=True)
    souce = models.CharField(max_length=200)
    date = models.DateTimeField(default=now)

class Stock(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    