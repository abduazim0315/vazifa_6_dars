from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"