from rest_framework import serializers
from catalog.models import *
from users.models import *
from review.models import *

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'


class KotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kota
        fields = '__all__'


class KecamatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kecamatan
        fields = '__all__'


class TempatWisataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempatWisata
        fields = '__all__'
        

class FotoTambahanWisataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoTambahanWisata
        fields = '__all__'


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class CommentLikeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['liked']