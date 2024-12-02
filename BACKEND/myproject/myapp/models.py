from django.db import models

class ProductInfo(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.product} - {self.color}"
