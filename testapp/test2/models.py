from django.db import models


# Create your models here.
class Other(models.Model):
    blob = models.ForeignKey(
        'testapp.blob', models.DO_NOTHING, related_name='others')
    name = models.CharField(max_length=20, unique=True)
