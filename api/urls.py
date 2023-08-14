from django.urls import path
from . import views

urlpatterns = [
    path('get_kategori', views.getDataKategori),
    path('get_kota', views.getDataKota),
    path('get_kecamatan', views.getDataKecamatan),
    path('get_tempat_wisata', views.getDataKategori),

    path('add_kategori', views.addKategori),
    path('add_kota', views.addKota),
    path('add_kecamatan', views.addKecamatan),
    path('add_tempat_wisata', views.addTempatWisata),

    path('get_tempat_wisata_by_kecamatan/<str:kecamatan>', views.getTempatWisataByKecamatan)

]
