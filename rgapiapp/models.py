from django.db import models
import jsonfield
# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=100)
    steps = jsonfield.JSONField()