from django.db import models
from catalog.models import TempatWisata
from users.models import CustomUser
from django.utils import timezone

class Comment(models.Model):
    tempat_wisata = models.ForeignKey(TempatWisata, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    liked = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE) # masukkin id comment -> reply belongs to a comment
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    liked = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
