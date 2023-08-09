from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Kategori (models.Model):
    nama = models.CharField(max_length=20, unique= True)
    icon = models.CharField(max_length=30, default='')

class Kota (models.Model):
    nama = models.CharField(max_length=30, unique= True)
    is_locked = models.BooleanField(default=False)

class Kecamatan (models.Model):
    kota = models.ForeignKey(Kota, on_delete=models.CASCADE)
    nama = models.CharField(max_length=30, unique= True, default='')

class TempatWisata (models.Model):
    kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE)
    kategori = models.ManyToManyField(Kategori)
    nama = models.CharField(max_length=50)
    link_gmap = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    deskripsi_singkat = models.TextField(blank=True, null=True)
    deskripsi_lengkap = models.TextField(blank=True, null=True)
    foto = models.ImageField(blank=True, null=True, upload_to="images/")
    
class FotoTambahanWisata(models.Model):
    tempatWisata = models.ForeignKey(TempatWisata, on_delete=models.CASCADE)
    foto = models.ImageField(blank=True, null=True, upload_to="images/")
