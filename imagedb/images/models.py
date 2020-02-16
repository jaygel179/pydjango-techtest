from time import time
from django.db import models


def user_directory_path(_, filename):
    return f'{round(time())}/{filename}'


class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    file_name = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ImageLabel(models.Model):
    image = models.ForeignKey(Image, related_name='labels', on_delete=models.CASCADE)
    label = models.CharField(max_length=255, db_index=True)
    confidence = models.FloatField()
