from django.db import models

class Consumable(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()

    total_sold = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    total_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-total_sold']