from django.db import models
from catalog.models import TempatWisata
from users.models import CustomUser
# Create your models here.

class Comment(models.Model):
    tempat_wisata = models.ForeignKey(TempatWisata, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    liked = models.IntegerField(default=0)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    liked = models.IntegerField(default=0)