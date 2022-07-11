import hashlib

from accounts.models import Profiles

from django.db import models

# Create your models here.
from django.db import models
# Create your models here.

class RassperySystem(models.Model):
    class Meta:
        verbose_name ='سیستم ها(رزپری پای)'
        verbose_name_plural = 'سیستم ها(رزپری پای)'
    token_connect_rassperypi=models.CharField(max_length=256,unique=True, verbose_name='توکن اتصال')
    serial_rasperyPi=models.CharField(max_length=16,unique=True ,verbose_name='سریال رزپری پای')
    hash_serial_rassperyPi=models.CharField(max_length=64,null=True,blank=True,verbose_name='hash سریال رزپری پای')
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    online=1
    offline=2
    type_status_online=(
        (online,'سیستم متصل است'),
        (offline,'سیستم آفلاین است'),
    )
    rassperyPi4=0
    rassperyPIZero=1
    a_type_rassperyPi = (
        (rassperyPi4, 'رزپری پای4'),
        (rassperyPIZero, 'رزپری پای صفر'),
    )
    type_rassperyPi=models.IntegerField(choices=a_type_rassperyPi, verbose_name='نوع رزپری پای')
    address=models.TextField(verbose_name='آدرس محل نصب')
    online_status = models.IntegerField(choices=type_status_online, default=2, verbose_name='وضعیت درخواست')
    title=models.CharField(max_length=80,verbose_name='عنوان رزری پای')
    def save(self, *args, **kwargs):
        self.hash_serial_rassperyPi = hashlib.sha256(self.serial_rasperyPi.__str__().encode('utf-8')).hexdigest()
        # Call the original save method
        super(RassperySystem, self).save(*args, **kwargs)
    def __str__(self):
        return self.serial_rasperyPi
