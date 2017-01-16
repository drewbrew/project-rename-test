"""Simple test app"""

from django.db import models

from simple_history import register


class Blargh(models.Model):
    name = models.CharField(unique=True, max_length=50)


class Dummy(models.Model):
    blob = models.ForeignKey('blargh', models.CASCADE, related_name='dummies')
    name = models.CharField(max_length=25, unique=True)

for model in [Blargh, Dummy]:
    register(model)
