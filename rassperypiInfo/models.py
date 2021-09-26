from accounts.models import Profiles

from django.db import models

# Create your models here.
from django.db import models
# Create your models here.

class RassperySystem(models.Model):
    class Meta:
        verbose_name ='سیستم ها(رزپری پای)'
        verbose_name_plural = 'سیستم ها(رزپری پای)'
    token=models.CharField(max_length=256, verbose_name='توکن اتصال')
    serial_rasperyPi=models.CharField(max_length=16, blank=True, null=True, verbose_name='سریال رزپری پای')
    serial_reset_password=models.CharField(max_length=12)
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE)

    def __str__(self):
        return self.serial_rasperyPi
