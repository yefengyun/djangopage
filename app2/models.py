from django.db import models


# Create your models here.
class Host(models.Model):
    HostName = models.CharField(max_length=256)
    IP = models.GenericIPAddressField()

    class Meta:
        db_table = 'host'
