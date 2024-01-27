from django.db import models

# Create your models here.


class Class(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    info = models.CharField(max_length=300, unique=True, null=True)
