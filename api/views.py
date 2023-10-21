from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import viewsets, status
from users.models import ProfileUser

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
def getComment(request, tempat_wisata):
    comments = Comment.objects.filter(tempat_wisata=tempat_wisata)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getReply(request, comment):
    replies = Reply.objects.filter(comment=comment)
    serializer = ReplySerializer(replies, many=True)
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


@api_view(['GET'])
def getProfileUserByUser(request, pk_user):
    pk_user = int(pk_user)    
    email = CustomUser.objects.get(id=pk_user).email
    prim_key = int()
    for user in CustomUser.objects.all():
        if user.email == email:
            prim_key = user.id
            break
    ProfileUsers = ProfileUser.objects.filter(user=prim_key)
    serializer = ProfileUserSerializer(ProfileUsers, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def addComment(request):
    serializer = Comment(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def addReply(request):
    serializer = Reply(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

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

@api_view(['POST'])
def incrementLikedComment(request):
    try:
        comment_id = request.data.get('id')
        if comment_id is None:
            return Response({'message': 'Please provide a comment ID in the request body'}, status=status.HTTP_400_BAD_REQUEST)
        
        instance = Comment.objects.get(id=int(comment_id))
    except Comment.DoesNotExist:
        return Response({'message': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)

    instance.liked += 1
    authorUser = ProfileUser.objects.get(user=instance.author.id)
    authorUser.review_disukai += 1
    authorUser.save()
    instance.save()
    return Response({'message': 'Liked attribute updated successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def incrementLikedReply(request):
    try:
        comment_id = request.data.get('id')
        if comment_id is None:
            return Response({'message': 'Please provide a comment ID in the request body'}, status=status.HTTP_400_BAD_REQUEST)
        
        instance = Reply.objects.get(id=int(comment_id))
    except Reply.DoesNotExist:
        return Response({'message': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)

    instance.liked += 1
    authorUser = ProfileUser.objects.get(user=instance.author.id)
    authorUser.review_disukai += 1
    authorUser.save()
    instance.save()
    return Response({'message': 'Liked attribute updated successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllComment(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllReply(request):
    replies = Reply.objects.all()
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)