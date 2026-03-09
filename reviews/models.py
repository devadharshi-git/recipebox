from django.db import models
from recipes.models import Recipe
from django.contrib.auth.models import User

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.recipe}"