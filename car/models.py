from django.db import models
from brand.models import BrandModel
# Create your models here.

class CarModel(models.Model):
    image = models.ImageField(upload_to='car/media/uploads/', blank=True, null= True)
    name = models.CharField(max_length = 100)
    price = models.CharField(max_length = 50)
    brand = models.ForeignKey(BrandModel, on_delete = models.CASCADE)
    description = models.TextField(blank=True, null= True)
    quantity = models.IntegerField(blank=True, null= True)
    def __str__(self): 
        return f'{self.name}'
    
class Comment(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f'Comments by {self.name}'