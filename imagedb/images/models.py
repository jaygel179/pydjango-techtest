from time import time
from rest_framework.exceptions import ValidationError

from django.db import models
from django.conf import settings

from imagedb.aws_utils import detect_labels_from_image_using_aws_rekognition
from imagedb.aws_utils import upload_file_to_s3


def _detect_and_save_image_labels(image):
    labels = detect_labels_from_image_using_aws_rekognition(image.file_name, settings.AWS_BUCKET_NAME)
    labels_to_save = [
        ImageLabel(image=image, label=label['Name'], confidence=label['Confidence'])
        for label in labels
    ]
    ImageLabel.objects.bulk_create(labels_to_save, 100)


def user_directory_path(_, filename):
    return f'{round(time())}/{filename}'


class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    file_name = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # override save button to not save the image from db
    def save(self, *args, **kwargs):
        # raise validation error if no image selected
        if not self.image:
            raise ValidationError('File not found!', 404)

        # set filename for future references
        self.file_name = self.image.name

        upload_file_to_s3(self.image, self.file_name, settings.AWS_BUCKET_NAME)

        # remove image so it wont get saved from db
        self.image = None

        super(Image, self).save(*args, **kwargs)

        # detect image label
        # making sure the image is saved for us to create ImageLabels later
        _detect_and_save_image_labels(self)


class ImageLabel(models.Model):
    image = models.ForeignKey(Image, related_name='labels', on_delete=models.CASCADE)
    label = models.CharField(max_length=255, db_index=True)
    confidence = models.FloatField()
