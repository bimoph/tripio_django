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
