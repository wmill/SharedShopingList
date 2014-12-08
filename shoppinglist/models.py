from django.db import models
from django.contrib import admin

from django.contrib.auth.models import User

# Create your models here.

class ShoppingItem(models.Model):
  name = models.CharField(max_length=400)
  user = models.ForeignKey(User)

  def __str__(self):
    return self.name



admin.site.register(ShoppingItem)