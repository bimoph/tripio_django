from django.urls import path
from . import views

urlpatterns = [
    path('get_kategori', views.getDataKategori),
    path('get_kota', views.getDataKota),
    path('get_kecamatan', views.getDataKecamatan),
    path('get_tempat_wisata', views.getDataKategori),


]
