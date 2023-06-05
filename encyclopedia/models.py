from django.db import models

# Create your models here.

class enteries(models.Model):
    title = models.CharField(max_length=255)
