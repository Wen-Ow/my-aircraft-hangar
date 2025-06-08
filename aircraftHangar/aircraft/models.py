from django.db import models

# Create your models here.
class Aircraft(models.Model):
    tail_number = models.CharField(max_length=20, unique=True)
    aircraft_type = models.ForeignKey('AircraftType', on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='aircrafts')
    manufacturer = models.CharField(max_length=100)
    condition = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True, default="images/default.png")
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AircraftType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name