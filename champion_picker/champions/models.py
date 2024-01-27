from django.db import models

from classes.models import Class
from partypes.models import Partype

# Create your models here.


class Champion(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    alias = models.CharField(max_length=20, unique=True)
    title = models.CharField()
    blurb = models.CharField()
    classes = models.ManyToManyField(Class, blank=True)
    partype_id = models.ForeignKey(Partype, on_delete=models.PROTECT)


class Skin(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    champion_id = models.ForeignKey(Champion, on_delete=models.PROTECT)
