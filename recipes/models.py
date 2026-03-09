from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    rating = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.title
