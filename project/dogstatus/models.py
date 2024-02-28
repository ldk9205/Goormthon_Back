# Create your models here.
from django.db import models
from django.conf import settings

class Dog(models.Model):
    petName = models.CharField(max_length=255)
    petSize = models.CharField(max_length=255)
    petAge = models.CharField(max_length = 255)
    petPersonality = models.CharField(max_length=255)
    tripConcept = models.CharField(max_length=255)

