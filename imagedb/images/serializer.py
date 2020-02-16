from rest_framework import serializers

from django.conf import settings

from imagedb.aws_utils import get_signed_urls_from_s3_object
from imagedb.images.models import Image
from imagedb.images.models import ImageLabel


class ImageLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLabel
        fields = ['id', 'label', 'confidence', 'image']


class ImageSerializer(serializers.ModelSerializer):
    # serializer method field for custom fields like presigned s3 url
    s3_url = serializers.SerializerMethodField()

    # include labels from image
    labels = ImageLabelSerializer(many=True, read_only=True)

    # signed url from s3 bucket
    def get_s3_url(self, obj):
        return get_signed_urls_from_s3_object(obj.file_name, settings.AWS_BUCKET_NAME)

    class Meta:
        model = Image
        fields = ['id', 'image', 'file_name', 'uploaded_at', 's3_url', 'labels']
