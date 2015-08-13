from django.db import models
from django.contrib.postgres.fields import HStoreField

# Create your models here.
class Scan(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    attributes = HStoreField()
    def __str__(self):
        return self.name + '-->' + str( self.attributes )
