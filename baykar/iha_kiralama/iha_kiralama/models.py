from django.db import models

from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser

class IHA(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    agirlik = models.FloatField()
    kategori = models.CharField(max_length=100)
    class Meta:
        db_table="iha"


class IHAUSER(models.Model):
    isim = models.CharField(max_length=20)
    soyisim = models.CharField(max_length=20)
    mail = models.CharField(max_length=150)
    telefon = models.CharField(max_length=50)
    kullaniciAdi = models.CharField(max_length=20)
    sifre=models.CharField(max_length=20)
    
    class Meta:
        db_table="ihauser"


class MyUser(AbstractUser):
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=50)
    mail = models.EmailField(max_length=150)
    telefon = models.CharField(max_length=20)
    kullanici_adi = models.CharField(max_length=50, unique=True)
    sifre = models.CharField(max_length=128)
    # Ekstra alanları burada tanımlayabilirsiniz
    
    USERNAME_FIELD = 'kullanici_adi'
    REQUIRED_FIELDS = ['isim', 'soyisim', 'mail', 'telefon']
