from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Kategori)
admin.site.register(Kota)
admin.site.register(Kecamatan)
admin.site.register(TempatWisata)
