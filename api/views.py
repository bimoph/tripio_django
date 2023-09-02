from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

@api_view(['GET'])
def getDataKategori (request):
    kategoris = Kategori.objects.all()
    serializer = KategoriSerializer(kategoris, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDataKota (request):
    kotas = Kota.objects.all()
    serializer = KotaSerializer(kotas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDataKecamatan (request):
    kecamatans = Kecamatan.objects.all()
    serializer = KecamatanSerializer(kecamatans, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDataTempatWisata (request):
    TempatWisatas = TempatWisata.objects.all()
    serializer = TempatWisataSerializer(TempatWisatas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAllProfileUser (request):
    profileusers = ProfileUser.objects.all()
    serializer = ProfileUserSerializer(profileusers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAllCustomUser (request):
    customusers = CustomUser.objects.all()
    serializer = CustomUserSerializer(customusers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFotoTambahanWisata(request, id):
    FotoTambahanWisatas = FotoTambahanWisata.objects.filter(tempatWisata=int(id))
    serializer = FotoTambahanWisataSerializer(FotoTambahanWisatas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProfileUser(request, email):
    prim_key = int()
    for user in CustomUser.objects.all():
        if user.email == email:
            prim_key = user.id
            break
    ProfileUsers = ProfileUser.objects.filter(user=prim_key)
    serializer = ProfileUserSerializer(ProfileUsers, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def get

@api_view(['POST'])
def addProfileUser(request):
    serializer = ProfileUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addKategori(request):
    serializer = KategoriSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addKota(request):
    serializer = KotaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addKecamatan(request):
    serializer = KecamatanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addTempatWisata(request):
    serializer = TempatWisataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addFotoTambahan(request):
    serializer = FotoTambahanWisataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# 4. filter tempat n kategori
@api_view(['GET'])
def getTempatWisataByKategoriKecamatan (request, kategori, kecamatan):
    TempatWisatas = TempatWisata.objects.filter(kategori= kategori, kecamatan=kecamatan)
    serializer = TempatWisataSerializer(TempatWisatas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTempatWisataByKategoriKota (request, kategori, kota):
    kecamatans = Kecamatan.objects.filter(kota=kota)
    list_kecamatan = [entry for entry in kecamatans]
    list_tempat_wisata = list()
    for objek_kecamatan in list_kecamatan:
        print(objek_kecamatan.nama)
        list_tempat_wisata += TempatWisata.objects.filter(kecamatan= objek_kecamatan.nama, kategori=kategori)
    serializer = TempatWisataSerializer(list_tempat_wisata, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTempatWisataByKecamatan (request, kecamatan):
    TempatWisatas = TempatWisata.objects.filter(kecamatan= kecamatan)
    serializer = TempatWisataSerializer(TempatWisatas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTempatWisataByKota (request, kota):
    kecamatans = Kecamatan.objects.filter(kota=kota)
    list_kecamatan = [entry for entry in kecamatans]
    list_tempat_wisata = list()
    for objek_kecamatan in list_kecamatan:
        print(objek_kecamatan.nama)
        list_tempat_wisata += TempatWisata.objects.filter(kecamatan= objek_kecamatan.nama)
    serializer = TempatWisataSerializer(list_tempat_wisata, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTempatWisataByKategori (request, kategori):
    TempatWisatas = TempatWisata.objects.filter(kategori= kategori)
    serializer = TempatWisataSerializer(TempatWisatas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTempatWisataBySearchNama (request, nama):
    TempatWisatas = TempatWisata.objects.filter(nama__icontains= nama)
    serializer = TempatWisataSerializer(TempatWisatas, many=True)
    return Response(serializer.data)

