from django.db import models
from car.models import CarModel
from django.contrib.auth.models import User
# Create your models here.

class PurchaseClass(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.car} by {self.user}'