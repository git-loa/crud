from django.db import models

# Create your models here.

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=125)
    
    def __str__(self) -> str:
        return str(self.first_name)+ "   "+str(self.last_name)
