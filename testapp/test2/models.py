from django.db import models

from simple_history import register


# Create your models here.
class Other(models.Model):
    blob = models.ForeignKey(
        'testapp.blargh', models.DO_NOTHING, related_name='others')
    name = models.CharField(max_length=20, unique=True)


register(Other)
