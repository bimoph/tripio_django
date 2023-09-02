from django.urls import path
from . import views

urlpatterns = [
    path('get_kategori', views.getDataKategori),
    path('get_kota', views.getDataKota),
    path('get_kecamatan', views.getDataKecamatan),
    path('get_tempat_wisata', views.getDataTempatWisata),
    path('get_all_profile_user',views.getAllProfileUser),
    path('get_all_custom_user',views.getAllCustomUser),

    path('get_profile_user/<str:email>',views.getProfileUser),

    path('add_kategori', views.addKategori),
    path('add_kota', views.addKota),
    path('add_kecamatan', views.addKecamatan),
    path('add_tempat_wisata', views.addTempatWisata),
    path('add_foto_tambahan', views.addFotoTambahan),
    path('add_profile_user', views.addProfileUser),



    path('get_foto_tambahan_tempat_wisata/<str:id>', views.getFotoTambahanWisata),
    


    path('get_tempat_wisata_by_kecamatan/<str:kecamatan>', views.getTempatWisataByKecamatan),
    path('get_tempat_wisata_by_kota/<str:kota>', views.getTempatWisataByKota),
    path('get_tempat_wisata_by_kategori/<str:kategori>', views.getTempatWisataByKategori),

    path('get_tempat_wisata_by_kategori_kota/<str:kategori>/<str:kota>', views.getTempatWisataByKategoriKota),
    path('get_tempat_wisata_by_kategori_kecamatan/<str:kategori>/<str:kecamatan>', views.getTempatWisataByKategoriKecamatan),





    path('get_tempat_wisata_by_search_nama/<str:nama>', views.getTempatWisataBySearchNama),




]
