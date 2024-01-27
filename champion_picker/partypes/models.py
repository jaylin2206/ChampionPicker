from django.db import models

# Create your models here.


class Partype(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    info = models.CharField(max_length=300, unique=True, null=True)


