from rest_framework import viewsets

from imagedb.images.models import Image
from imagedb.images.models import ImageLabel
from imagedb.images.serializer import ImageSerializer
from imagedb.images.serializer import ImageLabelSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# Create your views here.
class ImageLabelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ImageLabel.objects.all()
    serializer_class = ImageLabelSerializer
