from django.db import models

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=160, default="UCD", null=True)
    url = models.CharField(max_length=500, null=True)