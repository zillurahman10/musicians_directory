from django.db import models
# from album.models import Album

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    # album = models.ForeignKey(Album, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    