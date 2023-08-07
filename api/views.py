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
