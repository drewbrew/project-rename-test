"""Simple test app"""

from django.db import models


class Blob(models.Model):
    name = models.CharField(unique=True, max_length=50)


class Dummy(models.Model):
    blob = models.ForeignKey('blob', models.CASCADE, related_name='dummies')
    name = models.CharField(max_length=25, unique=True)
