from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    # rating = models.DecimalField(max_digits=3, decimal_places=1)
    # duration = models.IntegerField()  # in minutes
    # image_url = models.URLField()

# Create your models here.
