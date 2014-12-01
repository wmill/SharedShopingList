from django.db import models

# Create your models here.

class ShoppingItem(models.Model):
  name = models.CharField(max_length=200)
  
