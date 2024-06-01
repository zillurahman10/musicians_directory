from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from musician.models import Musician
from django.forms.widgets import NumberInput

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    release_date = models.DateField()
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])
    