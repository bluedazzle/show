from django.db import models


# Create your models here.

class Host(models.Model):
    host = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    icp = models.CharField(max_length=20)

    def __unicode__(self):
        return self.host
