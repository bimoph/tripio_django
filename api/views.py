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
def getFotoTambahanWisata (request):
    FotoTambahanWisatas = FotoTambahanWisata.objects.all()
    serializer = FotoTambahanWisataSerializer(FotoTambahanWisatas, many=True)
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


# 4. Buat api buat get data dari tempat wisata by lokasi
# 5. Buat api buat get data dari tempat wisata by kategori
# 6. Buat api buat login
# 7. fitur search kalo sempet gua lagi nyoba juga ini
# 8. Kalo user dah jadi buat database buat nyimpen data TempatWisata (Get dan Post)

@api_view(['GET'])
def getTempatWisataByKecamatan (request, kecamatan):
    TempatWisatas = TempatWisata.objects.filter(kecamatan= kecamatan)
    serializer = TempatWisataSerializer(TempatWisatas, many=True)
    return Response(serializer.data)