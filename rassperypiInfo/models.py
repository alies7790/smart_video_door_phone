from accounts.models import Profiles

from django.db import models

# Create your models here.
from django.db import models
# Create your models here.

class RassperySystem(models.Model):
    class Meta:
        verbose_name ='سیستم ها(رزپری پای)'
        verbose_name_plural = 'سیستم ها(رزپری پای)'
    token=models.CharField(max_length=256,unique=True, verbose_name='توکن اتصال')
    serial_rasperyPi=models.CharField(max_length=16,unique=True ,blank=True, null=True, verbose_name='سریال رزپری پای')

    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    online=1
    offline=2
    type_status_online=(
        (online,'سیستم متصل است'),
        (offline,'سیستم آفلاین است'),
    )
    online_status = models.IntegerField(choices=type_status_online, default=2, verbose_name='وضعیت درخواست')
    def __str__(self):
        return self.serial_rasperyPi
