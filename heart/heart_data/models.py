from django.db import models

class Heart_data(models.Model):
    name = models.TextField(max_length=255)
    age = models.FloatField(max_length=255)
    sex = models.FloatField(max_length=255)
    cp = models.FloatField(max_length=255)
    trestbps = models.FloatField(max_length=255)
    chol = models.FloatField(max_length=255)
    thalach = models.FloatField(max_length=255)
    oldpeak = models.FloatField(max_length=255)
    ca = models.FloatField(max_length=255)
    thal = models.FloatField(max_length=255)
    target = models.FloatField(max_length=255)
    
# Create your models here.
