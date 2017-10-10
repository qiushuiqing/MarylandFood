# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MFcountry(models.Model):
  author = models.ForeignKey('auth.User', default='')
  country= models.CharField(max_length=150)
  description= models.CharField(max_length=100)

  def __str__(self):
        return self.country
  
  # Create your models here.
class MFrestaurant(models.Model):
  author = models.ForeignKey('auth.User', default='')
  restaurant= models.CharField(max_length=150)
  description= models.CharField(max_length=100)
  country = models.ForeignKey(MFcountry, on_delete=models.CASCADE)
  
  def __str__(self):
        return self.restaurant